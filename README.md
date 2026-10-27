ScoutAI — Your Real-Time AI Research Assistant

Search Smarter. Compare Faster. Decide Better.

ScoutAI is an AI-powered research assistant designed to help users discover information across the web, compare findings from different sources, and turn research into clear, actionable insights.

Instead of manually browsing multiple websites, users can ask a question in natural language and use ScoutAI to research topics, summarize findings, compare alternatives, and organize information in one place.

«Project status: Update this README to distinguish implemented features from planned features before publishing your repository.»

Table of Contents

- "Problem Statement" (#problem-statement)
- "Proposed Solution" (#proposed-solution)
- "Key Features" (#key-features)
- "Target Users" (#target-users)
- "How ScoutAI Works" (#how-scoutai-works)
- "Technical Architecture" (#technical-architecture)
- "Technology Stack" (#technology-stack)
- "TinyFish API Integration" (#tinyfish-api-integration)
- "Getting Started" (#getting-started)
- "API Key Setup" (#api-key-setup)
- "Running ScoutAI" (#running-scoutai)
- "Example Use Cases" (#example-use-cases)
- "Future Enhancements" (#future-enhancements)
- "Security and Privacy" (#security-and-privacy)
- "Limitations" (#limitations)
- "Contributing" (#contributing)
- "License" (#license)

Problem Statement

Finding reliable information online can be time-consuming. Users often need to visit multiple websites, compare conflicting information, identify useful sources, and manually prepare summaries or reports.

Traditional search engines provide links, but users still have to perform much of the research and comparison themselves.

ScoutAI aims to simplify this process by combining AI-powered reasoning, web research, and workflow orchestration in a single assistant.

Proposed Solution

ScoutAI uses a Large Language Model (LLM), an agent workflow built with LangGraph, and the TinyFish API to support web-based research.

The system is designed to:

1. Understand the user's research question.
2. Identify relevant information to investigate.
3. Retrieve information from web sources using TinyFish.
4. Organize and summarize the retrieved information using an LLM.
5. Present useful findings with source links where available.
6. Help users compare alternatives and make informed decisions.

The goal is to make online research faster, more organized, and easier to understand.

Key Features

1. AI-Powered Research

Ask questions in natural language and receive structured responses based on the research workflow.

2. Real-Time Web Research

Use the TinyFish API to search the web or retrieve information from relevant websites, depending on the selected TinyFish endpoint.

3. Smart Comparison Engine

Compare products, services, travel options, technologies, and other alternatives in a structured format.

4. Research Summarization

Turn lengthy information into concise summaries, key points, and actionable insights.

5. Source-Based Results

Include links to the pages used during research whenever the API returns them. Users can open the original pages to review the information.

6. Research Report Generation

Planned enhancement: Generate downloadable research reports in PDF format.

7. Research Memory

Planned enhancement: Save previous research sessions and allow users to continue their work later using persistent storage.

8. Specialized Research Workflows

Planned enhancement: Add dedicated workflows for academic research, travel planning, product comparisons, market analysis, and competitor research.

Target Users

User Group| Use Cases
Students and Researchers| Assignments, research projects, academic studies, and topic exploration
Travelers| Travel options, routes, prices, and comparisons
Working Professionals| Reports, industry research, and decision support
Consumers and Online Shoppers| Comparing products, features, prices, and alternatives
Startups and Entrepreneurs| Market research, competitor analysis, industry trends, and business opportunities

How ScoutAI Works

The planned research workflow follows this sequence:

1. User Query: The user submits a research question through the Streamlit interface.
2. Workflow Orchestration: LangGraph manages the steps required to process the query.
3. LLM Reasoning: Groq provides access to a supported language model for understanding the question and generating responses.
4. Web Research: The TinyFish API retrieves relevant information from the web.
5. Result Processing: The application organizes retrieved information and prepares it for the LLM.
6. Final Response: ScoutAI presents a summary and source links when available.
7. Optional Output: Future versions can generate reports and save research sessions.

Technical Architecture

                    USER
                      |
                      v
              Streamlit Frontend
                      |
                      v
             Python Application
                      |
                      v
              LangGraph Workflow
                      |
              +-------+-------+
              |               |
              v               v
         Groq LLM        TinyFish API
              |               |
              |         Web Research
              |               |
              +-------+-------+
                      |
                      v
             Result Processing
                      |
                      v
          Summary + Source Links
                      |
                      v
              Streamlit UI

Architecture Components

- Frontend: Streamlit provides the user interface.
- Backend: Python handles application logic and API integration.
- Agent Orchestration: LangGraph organizes the research workflow into nodes and transitions.
- Language Model: Groq API provides hosted LLM inference.
- Web Research: TinyFish API provides web search, page retrieval, or website automation capabilities depending on the endpoint used.
- Persistence: LangGraph checkpointing and optional database storage can support saved sessions.

Technology Stack

Technology| Purpose
Python| Core application development
LangGraph| Agent workflow orchestration
LangChain| LLM integration and related utilities
Groq API| Hosted language model inference
TinyFish API| Web research and information retrieval
Streamlit| Interactive frontend
python-dotenv| Loading environment variables
SQLite (optional)| Persistent local storage
ReportLab (planned)| PDF report generation

TinyFish API Integration

TinyFish is an important component of ScoutAI because it enables the application to gather information from external websites rather than relying only on the language model's existing knowledge.

Official resources:

- TinyFish website: https://www.tinyfish.ai/
- TinyFish developer platform: https://agent.tinyfish.ai/
- TinyFish documentation: https://docs.tinyfish.ai/
- TinyFish API examples: https://github.com/tinyfish-io/tinyfish-cookbook

Integration Workflow

1. Create a TinyFish account.
2. Generate an API key from the TinyFish developer platform.
3. Store the key in the project's ".env" file.
4. Read the key securely in the Python backend.
5. Send a request to the appropriate TinyFish endpoint.
6. Process the response and pass useful results into the research workflow.
7. Present the final response to the user.

Example: TinyFish Web Search API

The following is a minimal Python example for testing the TinyFish Search endpoint.

import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TINYFISH_API_KEY")

if not api_key:
    raise ValueError("TINYFISH_API_KEY is missing from .env")

response = requests.get(
    "https://api.search.tinyfish.ai",
    params={"query": "LangGraph AI agent tutorials"},
    headers={"X-API-Key": api_key},
    timeout=60,
)

response.raise_for_status()
print(response.json())

This example demonstrates a standalone search request. The response structure and available results depend on the current TinyFish API.

Other TinyFish Capabilities

Depending on the endpoint and account access, TinyFish also provides APIs for fetching webpage information and running website automation tasks.

These capabilities can support future ScoutAI features such as extracting product details, comparing information across websites, and researching specific web pages.

Important: A successful standalone API test does not automatically mean that TinyFish is fully integrated into the LangGraph workflow. The application must call the tool during the actual research process.

Getting Started

Prerequisites

Install the following before running the project:

- Python 3.10 or another Python version supported by your installed dependencies.
- Git.
- A code editor such as Visual Studio Code.
- A Groq API key.
- A TinyFish API key.

An internet connection is required for hosted API calls.

1. Clone the Repository

Replace "YOUR_GITHUB_USERNAME" with your GitHub username.

git clone https://github.com/YOUR_GITHUB_USERNAME/ScoutAI.git
cd ScoutAI

If your repository has a different name, replace "ScoutAI" with that repository name.

2. Create a Virtual Environment

On Windows:

python -m venv venv1

Activate it:

venv1\Scripts\activate

3. Install Dependencies

If the repository contains "requirements.txt", run:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

If you are setting up a minimal prototype from scratch, these packages may be required:

python -m pip install langgraph langchain langchain-groq streamlit python-dotenv requests

Use the project's actual "requirements.txt" as the primary dependency list. You do not need "langchain-openai" merely to use "ChatGroq".

API Key Setup

ScoutAI uses API keys to authenticate requests to external services. You must create your own keys; do not copy another developer's keys.

A. Get a Groq API Key

1. Open https://console.groq.com/keys
2. Sign in or create an account.
3. Create a new API key.
4. Copy the key and keep it private.

Groq's official quickstart is available at https://console.groq.com/docs/quickstart.

B. Get a TinyFish API Key

1. Open https://agent.tinyfish.ai/
2. Sign in or create an account.
3. Navigate to the API key section of the developer platform.
4. Generate a key if your account supports it.
5. Copy the key and keep it private.

Refer to the official documentation for current account requirements and usage limits: https://docs.tinyfish.ai/.

C. Create the ".env" File

Create a file named ".env" in the root of your project, in the same directory as your backend Python file.

Add the following lines:

GROQ_API_KEY=your_actual_groq_api_key
TINYFISH_API_KEY=your_actual_tinyfish_api_key

Replace the placeholder values with the keys you generated.

Do not include quotation marks unless your configuration specifically requires them. Do not add spaces around the equals sign.

Your project structure might look like this:

ScoutAI/
├── langgraph_backend.py
├── streamlit_frontend.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

Your actual structure may differ depending on the implementation.

D. Load Environment Variables in Python

In the backend, load the ".env" file before initializing the API clients.

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env")

if not TINYFISH_API_KEY:
    raise ValueError("TINYFISH_API_KEY is missing from .env")

This code loads the values and checks that both keys exist. It does not, by itself, make API requests.

For a LangGraph application using Groq, the language model can be initialized separately:

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="YOUR_SUPPORTED_GROQ_MODEL",
    temperature=0,
)

Replace the model placeholder with a model ID currently supported by your Groq account. The "ChatGroq" integration reads "GROQ_API_KEY" from the environment.

E. Protect Your API Keys with ".gitignore"

Create or update ".gitignore" in the repository root:

.env
.env.*
!.env.example

venv/
venv1/
.venv/

__pycache__/
*.py[cod]

.streamlit/secrets.toml

This prevents common local secret files and generated files from being tracked by Git.

You can also create ".env.example" as a template for other developers:

GROQ_API_KEY=replace_with_your_groq_api_key
TINYFISH_API_KEY=replace_with_your_tinyfish_api_key

The example file contains placeholders only. Never put actual API keys in ".env.example", source code, screenshots, or this README.

Running ScoutAI

1. Activate the Virtual Environment

venv1\Scripts\activate

2. Test API Key Loading

Run this command from the project root:

python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Groq key loaded:', bool(os.getenv('GROQ_API_KEY'))); print('TinyFish key loaded:', bool(os.getenv('TINYFISH_API_KEY')))"

The output should show "True" for each configured key. This checks whether the environment variables are loaded; it does not verify that the keys are valid.

3. Test TinyFish Separately

Save the TinyFish example above as "test_tinyfish.py", then run:

python test_tinyfish.py

If the request fails, check your API key, network connection, endpoint, and the latest TinyFish documentation.

4. Run the Backend Test

If the project contains a backend test script, run it from the terminal before launching the frontend.

For example:

python test_backend.py

Use the actual test filename in your repository. If no test script exists, create one that imports the graph and invokes it with a sample message.

5. Launch the Streamlit Interface

Once the backend and API integrations have been tested:

python -m streamlit run streamlit_frontend.py

Streamlit will display a local URL in the terminal. Open that URL in your browser.

Example Use Cases

Academic Research

Query: "Compare LangGraph and traditional chain-based LLM applications."

Expected workflow: research relevant documentation, organize the differences, and summarize findings with source links.

Travel Research

Query: "Compare travel options from Delhi to Goa for my selected dates."

Expected workflow: gather information from relevant sources and compare available options. Availability and prices should be verified against the original provider because they can change.

Product Comparison

Query: "Compare three laptops for programming under my budget."

Expected workflow: retrieve relevant product pages, extract available specifications, and organize the comparison.

Market Research

Query: "Analyze the major competitors in the AI research assistant market."

Expected workflow: investigate relevant websites, identify recurring themes, and summarize competitor positioning.

These are intended use cases. Their actual performance depends on the connected APIs, workflow implementation, and available source information.

Scalability and Feasibility

ScoutAI is designed around modular components so that research workflows and tools can be added independently.

Potential improvements include:

- Adding specialized research agents for different domains.
- Using persistent storage for saved projects.
- Caching repeated research queries where appropriate.
- Introducing retry handling, request timeouts, and error reporting.
- Generating downloadable PDF reports.
- Adding authentication and per-user data isolation before multi-user deployment.
- Deploying the frontend and backend using an appropriate hosting platform.

API rate limits, usage costs, latency, and provider terms must be considered before scaling.

Future Enhancements

- Deep Research mode with multiple research steps.
- Cross-source fact checking and conflicting-claim detection.
- Structured comparison tables.
- PDF research reports.
- Saved research projects and conversation history.
- Gmail integration for searching and summarizing emails, with user authorization.
- Research planning and task reminders.
- Additional data sources and specialized research tools.

Planned enhancements should be marked as complete only after they have been implemented and tested.

Security and Privacy

- Keep API keys in environment variables or a secure secret manager.
- Never commit ".env" files or credentials to GitHub.
- Revoke and replace a key immediately if it is accidentally exposed.
- Avoid sending sensitive personal or business information to third-party APIs unless necessary and authorized.
- Review the privacy policies and usage terms of external API providers.
- Require explicit user confirmation before adding high-impact actions such as sending emails or submitting forms.
- Treat web page content as untrusted input and validate data before using it in automated workflows.

Limitations

- AI-generated summaries may contain errors or omit important details.
- Web sources may be outdated, incomplete, inaccessible, or inconsistent.
- Source links do not guarantee that every statement in a response is correct.
- API availability, pricing, rate limits, and model access can change.
- Results depend on the quality of the search query and the information returned by external services.
- Features that have not been implemented or tested may not be available in the current version.

Users should review important information against original sources before making consequential decisions.

Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Commit your changes with a clear message.
5. Open a pull request describing the improvement.

Please do not include API keys, private data, or other credentials in pull requests.

License

A license has not yet been specified. Add a "LICENSE" file before distributing the project if you want to define the permissions and conditions under which others can use, modify, or redistribute it.

---

ScoutAI — Search Smarter. Compare Faster. Decide Better.

Built with Python, LangGraph, Groq, TinyFish, and Streamlit.
