from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from dotenv import load_dotenv
import sqlite3
import requests
import os 
from pathlib import Path

# Backend file ke same folder se .env load karo
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# Key print kiye bina check karo
print("ENV file found:", env_path.is_file())
print("Groq key loaded:", bool(os.getenv("GROQ_API_KEY")))

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

print("Tinyfish key loaded:", bool(os.getenv("TINYFISH_API_KEY")))

#2. Tools
@tool
def tinyfish_search(query:str) -> str:
    """GENERAL RULES:
- Only search and read. NEVER click "Book", "Pay", "Reserve" or enter personal or payment details.
- If a cookie banner, login popup, app-download popup or ad overlay appears, dismiss it and continue.
- If a CAPTCHA appears, stop and return {"error": "captcha_blocked"}.
- If the page fails to load or the requested data is not found, return {"error": "not_found"} instead of guessing.
- Never invent prices, times or ratings. Only report what is visible on the page.
- Always include the exact page URL in "source_url" for every item.
- Prices must be returned as numbers (no commas or symbols) with a separate "currency" field.
- Return ONLY valid JSON. No explanations, no markdown.

TASK: Search flights.
Steps:
1. Enter origin: {origin_city} ({origin_code}), destination: {dest_city} ({dest_code}).
2. Set trip type: {one-way / round-trip}. Departure date: {depart_date}. Return date: {return_date or "N/A"}.
3. Set passengers: {adults} adult(s), {children} child(ren). Class: {economy}.
4. Click search and wait until results fully load (including "load more" if present).
5. Sort by price (lowest first). Collect the first 8 results.
6. Also note the single fastest flight and the best-rated or "best" option if the site labels one.

Return JSON:
{
  "searched_at": "",
  "flights": [
    {
      "airline": "", "flight_number": "",
      "departure_time": "", "arrival_time": "", "duration": "",
      "stops": 0, "layover_airports": [],
      "baggage_included": "", "refundable": true/false/"unknown",
      "price": 0, "currency": "", "source_url": ""
    }
  ],
  "cheapest_index": 0, "fastest_index": 0,
  "price_trend_note": "e.g. 'prices lower on nearby dates' if the site shows it, else null"
      """
    response = requests.get(
        "https://api.search.tinyfish.ai",
        headers={"X-API-Key": os.getenv("TINYFISH_API_KEY")},
        params={"query": query},
        timeout=30
    )
    response.raise_for_status()
    return response.json()


tools = [tinyfish_search]
llm_with_tools = llm.bind_tools(tools)

# 3. State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# 4. Nodes
def chat_node(state: ChatState):
    """LLM node that may answer or request a tool call."""
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)

# 5. Checkpointer
conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

# 6. Graph
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node",tools_condition)
graph.add_edge('tools', 'chat_node')

chatbot = graph.compile(checkpointer=checkpointer)

# 7. Helper
def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_threads)