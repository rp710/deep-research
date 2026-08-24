# 🔎 Deep Research

An AI-powered multi-agent research assistant that transforms a research question into a structured, evidence-informed report.

The system uses specialized AI agents to clarify the user's intent, plan web searches, perform research concurrently, synthesize the findings, and deliver the final report through the web interface and optional email/Pushover notification.

---

## ✨ Features

* 🧠 **Research clarification** — asks three targeted questions before research begins
* 🗺️ **Automatic research planning** — converts a question into multiple web-search queries
* 🌐 **Web research** — uses the OpenAI Agents SDK `WebSearchTool`
* ⚡ **Parallel searching** — executes independent searches concurrently using `asyncio`
* 📝 **AI report generation** — synthesizes research into a detailed Markdown report
* 📊 **Structured outputs** — uses Pydantic models for reliable agent responses
* 📬 **Report delivery** — supports email delivery
* 🔔 **Pushover fallback** — can send notifications instead of email
* 💻 **Gradio interface** — interactive browser-based research application
* 🎨 **Custom UI** — custom CSS and JavaScript for the research interface
* ☁️ **Render-ready** — can be deployed as a web service

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │       User          │
                         │  Research Question  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Gradio UI        │
                         │      app.py         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Clarifier Agent    │
                         │                     │
                         │ Generates 3 focused │
                         │ clarification Qs    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Research Manager   │
                         │ research_manager.py │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Planner Agent     │
                         │                     │
                         │ Generates search    │
                         │ queries + reasons   │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                         ▼                     ▼
                 ┌───────────────┐     ┌───────────────┐
                 │ Search Agent  │ ... │ Search Agent  │
                 │ Web Search    │     │ Web Search    │
                 └───────┬───────┘     └───────┬───────┘
                         │                     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Writer Agent     │
                         │                     │
                         │ Research synthesis  │
                         │ + Markdown report   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Email Agent     │
                         │                     │
                         │ Email / Pushover    │
                         └─────────────────────┘
```

---

## 🔄 Research Flow

### 1. User submits a question

The user enters a research question through the Gradio interface.

Example:

```text
What are the most promising AI agent frameworks in 2026?
```

---

### 2. Clarification

Before performing expensive research, the Clarifier Agent generates exactly three questions designed to improve the research brief.

It considers factors such as:

* Scope
* Geography
* Time period
* Intended audience
* Comparison criteria
* Desired depth
* Intended use

The agent returns a structured Pydantic object:

```python
class ClarifyingQuestions(BaseModel):
    questions: list[str]
```

This reduces ambiguity before research begins.

---

### 3. Research planning

The Planner Agent receives the refined research question and creates a collection of web searches.

Each search contains:

```python
class WebSearchItem(BaseModel):
    reason: str
    query: str
```

The complete plan is represented by:

```python
class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
```

The number of searches can be configured with:

```text
HOW_MANY_SEARCHES
```

---

### 4. Parallel web research

The Research Manager creates one search task for every planned query.

Instead of executing them sequentially, the project uses:

```python
await asyncio.gather(*tasks)
```

Conceptually:

```text
Search 1 ─┐
Search 2 ─┤
Search 3 ─┤──► Run concurrently
Search 4 ─┤
Search 5 ─┘
```

Each search is handled by the Search Agent.

The Search Agent has access to:

```python
WebSearchTool()
```

and is configured to require tool usage.

---

### 5. Report synthesis

Once the searches finish, their outputs are passed to the Writer Agent.

The Writer Agent receives:

```text
Original research question
+
Search results
```

and produces:

```python
class ReportData(BaseModel):
    short_summary: str
    markdown_report: str
    follow_up_questions: list[str]
```

The final report is written in Markdown.

---

### 6. Report delivery

The generated report is passed to the Email Agent.

The Email Agent uses a function tool:

```python
send_email_tool()
```

Depending on configuration:

```text
USE_EMAIL=true
        ↓
      SMTP
```

or:

```text
USE_EMAIL=false
        ↓
     Pushover
```

---

## 📁 Project Structure

```text
deep-research/
│
└── deep_research/
    │
    ├── app.py
    ├── simple.py
    │
    ├── research_manager.py
    │
    ├── clarifier_agent.py
    ├── planner_agent.py
    ├── search_agent.py
    ├── writer_agent.py
    ├── email_agent.py
    │
    ├── messenger.py
    ├── styles.py
    │
    ├── requirements.txt
    └── README.md
```

### `app.py`

Main application entry point.

Responsibilities:

* Create Gradio UI
* Accept research questions
* Launch clarification
* Collect clarification answers
* Start research
* Stream progress updates
* Display the final report
* Configure the server port

---

### `research_manager.py`

The central orchestrator.

Responsibilities:

```text
Clarification
      ↓
Planning
      ↓
Search execution
      ↓
Report generation
      ↓
Notification
```

This is the most important file for understanding the application's architecture.

---

### `clarifier_agent.py`

Defines the clarification agent.

It uses:

* OpenAI Agents SDK
* Pydantic
* Structured output

Its job is to turn an ambiguous question into a better research brief.

---

### `planner_agent.py`

Creates the research plan.

Input:

```text
Research question
```

Output:

```text
Search 1
Search 2
Search 3
...
```

Each search contains both a query and its purpose.

---

### `search_agent.py`

Responsible for actual web research.

It uses the OpenAI Agents SDK's:

```python
WebSearchTool
```

The agent summarizes the results instead of returning raw search output.

---

### `writer_agent.py`

Responsible for final synthesis.

It combines the search results into:

* Short summary
* Detailed Markdown report
* Follow-up research questions

---

### `email_agent.py`

Converts the final report into an email and calls the email tool.

---

### `messenger.py`

Contains the external notification implementations.

Supported mechanisms:

* SMTP email
* Pushover

---

### `styles.py`

Contains:

* Example questions
* HTML header
* CSS
* JavaScript

This file controls the visual presentation of the Gradio application.

---

### `simple.py`

Provides a minimal version of the UI without the clarification workflow.

Useful for quickly testing the research pipeline.

---

## 🛠️ Tech Stack

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| Python            | Application language         |
| OpenAI Agents SDK | Agent orchestration          |
| OpenAI model      | LLM reasoning and generation |
| WebSearchTool     | Web research                 |
| Pydantic          | Structured agent outputs     |
| Gradio            | Web interface                |
| asyncio           | Concurrent research          |
| python-dotenv     | Environment configuration    |
| Requests          | Pushover API                 |
| SMTP              | Email delivery               |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/rp710/deep-research.git
cd deep-research
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r deep_research/requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_api_key

DEFAULT_MODEL_NAME=gpt-5.4-mini

HOW_MANY_SEARCHES=5

USE_EMAIL=false

EMAIL_ADDRESS=
EMAIL_SMTP_SERVER=
EMAIL_APP_PASSWORD=

PUSHOVER_USER=
PUSHOVER_TOKEN=
```

Never commit API keys or passwords to GitHub.

---

## ▶️ Running the Application

From the `deep_research` directory:

```bash
cd deep_research
python app.py
```

The application uses port `7860` locally unless a `PORT` environment variable is provided.

Open the local Gradio URL shown in the terminal.

---

## 🧪 Simple Version

For a minimal interface:

```bash
python simple.py
```

The simple application directly sends the question to the research pipeline without the clarification interface.

---

## 🧠 Agent Responsibilities

The system follows a specialized-agent architecture.

```text
                 Research Manager
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
  Clarifier         Planner          Writer
       │               │                │
       │               ▼                │
       │          Search Agents         │
       │               │                │
       └───────────────┴────────────────┘
                       │
                       ▼
                 Email Agent
```

Each agent has a focused responsibility rather than one large prompt attempting to perform the entire workflow.

---

## ⚡ Concurrency

The project uses Python's asynchronous programming model.

Searches are launched with:

```python
tasks = [self.search(item) for item in search_plan.searches]

results = await asyncio.gather(*tasks)
```

This is important because web searches are I/O-bound operations.

Running them concurrently can significantly reduce total waiting time compared with:

```text
Search 1 → wait
Search 2 → wait
Search 3 → wait
Search 4 → wait
```

Instead:

```text
Search 1 ─┐
Search 2 ─┤
Search 3 ─┼──► concurrent execution
Search 4 ─┤
Search 5 ─┘
```

---

## 📦 Structured Outputs

The project uses Pydantic models to constrain important agent outputs.

For example:

```python
class WebSearchItem(BaseModel):
    reason: str
    query: str
```

and:

```python
class ReportData(BaseModel):
    short_summary: str
    markdown_report: str
    follow_up_questions: list[str]
```

This is preferable to relying entirely on free-form text because downstream components can work with predictable data structures.

---

## 🔍 Is This RAG?

**No — not traditional RAG.**

The architecture does not contain the typical:

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Retrieved Context
   ↓
LLM
```

Instead, it performs live agentic web research:

```text
Question
   ↓
Research Planning
   ↓
Web Search
   ↓
Search Summaries
   ↓
LLM Synthesis
   ↓
Report
```

The project is therefore better described as an:

> **Agentic Web Research System**

rather than a conventional RAG application.

---

## 🎯 Key AI Engineering Concepts Demonstrated

This project demonstrates several skills relevant to modern GenAI engineering:

### LLM Engineering

* Prompt engineering
* Structured generation
* Agent design
* Model configuration
* Context passing

### Agentic AI

* Multi-agent architecture
* Agent specialization
* Agent orchestration
* Tool calling
* Function tools
* Workflow management

### Retrieval / Research

* Web search
* Query planning
* Multi-search research
* Information synthesis

### Software Engineering

* Async Python
* Concurrency
* Modular architecture
* Environment configuration
* API integration

### Generative AI Application Development

* Gradio
* Streaming responses
* External notifications
* Structured outputs
* Deployment configuration

---

## 🚀 Potential Improvements

Several improvements could make the system substantially more production-ready.

### 1. Add source-level citations

Instead of passing only summaries between agents, preserve:

```text
Source URL
Title
Published date
Relevant passage
Claim
```

This would make the final report more verifiable.

### 2. Add a dedicated verification agent

A stronger pipeline could become:

```text
Planner
   ↓
Search
   ↓
Research
   ↓
Writer
   ↓
Fact Checker
   ↓
Final Writer
```

### 3. Add iterative research

Currently the research process follows a mostly fixed pipeline.

A more advanced system could allow the agent to decide:

```text
Are the findings sufficient?

       ├── Yes → Write report
       │
       └── No → Search again
```

### 4. Add persistent research memory

Research results could be stored in:

* PostgreSQL
* SQLite
* Vector database
* Document store

This would allow previous research to be reused.

### 5. Add observability

Track:

* Agent latency
* Token usage
* Search count
* Errors
* Cost
* Final answer quality

### 6. Add evaluation

Create a benchmark containing research questions and evaluate:

* Factual accuracy
* Citation correctness
* Search coverage
* Completeness
* Hallucination rate
* Latency
* Cost

---

## 📌 Example Use Cases

The system can be used for:

* Technology research
* Market research
* Competitive analysis
* AI/ML research
* Academic topic exploration
* Product research
* Industry analysis
* Current-events research

---

## 📈 Future Architecture

A more advanced version could look like:

```text
                         User
                          │
                          ▼
                    Clarification
                          │
                          ▼
                       Planner
                          │
                          ▼
                  Search / Retrieval
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
        Research Agent          Research Agent
              │                       │
              └───────────┬───────────┘
                          ▼
                     Synthesizer
                          │
                          ▼
                    Fact Checker
                          │
                    ┌─────┴─────┐
                    │           │
                 Correct     Incorrect
                    │           │
                    │           └──► Research Again
                    ▼
                Final Writer
                    │
                    ▼
              Citation Builder
                    │
                    ▼
               Final Report
```

---

## ⚠️ Security

Do not commit:

```text
OPENAI_API_KEY
EMAIL_APP_PASSWORD
PUSHOVER_TOKEN
```

Use environment variables or a secrets manager instead.

---

## 📄 License

Add the project's intended license here before distributing the repository.

---

## 👤 Author

Created by [rp710](https://github.com/rp710).

Repository:

https://github.com/rp710/deep-research
