# 🕵️‍♂️ Deep Research Agent with Recursive Critique

An autonomous AI agent capable of performing deep research by recursively searching the web, synthesizing information, and self-critiquing its own answers to ensure accuracy and depth.

Built with **Python**, **OpenAI GPT-4o/GPT-5**, and **Streamlit**.

## 🚀 Key Features

**Autonomy:** The agent decides *what* to search and *how many times* to search based on the query complexity.
**Recursive Research Loop:** Instead of a single search, the agent loops until it gathers sufficient information.
**Self-Correction (The "Critic"):** A secondary LLM call acts as a "Senior Editor," reviewing the draft answer. If it's too vague or lacks citations, the Critic rejects it and forces the Agent to do more research.
**Dual Interface:** Run it as a simple Command Line Tool or a full interactive Web App.

## 📂 Project Structure

```bash
├── app.py               # Streamlit Web Interface (Live "Thinking" UI)
├── main.py              # CLI Version (Terminal-based interaction)
├── clients.py           # OpenAI Client initialization
├── tools.py             # Tool logic (Web Search implementation)
├── tooldefinition.py    # JSON schemas for OpenAI function calling
└── utilty.py            # Helper functions (LLM calls, Critic logic)
```

## 🛠️ Installation

1. **Clone the repository:**

2. **Create a virtual environment:**
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Environment Variables:**
Create a `.env` file (or export variables) with your API keys:
```bash
export OPENAI_API_KEY="sk-..."
# Add any search tool keys if required (e.g., Tavily, Serper, etc.)

```



## 🏃‍♂️ Usage

### Option 1: The Web Interface (Recommended)

This launches a browser-based UI where you can see the agent's "Thought Process" (Planning, Searching, Critiquing) in real-time.

```bash
streamlit run app.py

```

### Option 2: The Command Line Interface

Best for debugging or quick text-based interactions.

```bash
python main.py

```

## 🧠 How It Works (The "Loop")

1. **Plan:** The LLM analyzes the user query and decides on search keywords.
2. **Act:** It executes the Python search tool.
3. **Observe:** It reads the search results.
4. **Draft:** It generates a preliminary answer.
5. **Critique:** The "Critic" model evaluates the draft for:
* Relevance
* Accuracy
* Citation Quality


6. **Refine:** If **Rejected**, the feedback is fed back into the loop, and the agent searches for missing details. If **Approved**, the final answer is delivered.

## 🔮 Future Roadmap

We are constantly working to make the agent smarter and more capable. Here is what is coming next:

* **[ ] Long-Term Memory:** Integrate a vector database (e.g., ChromaDB or Pinecone) so the agent can remember context across different sessions.
* **[ ] Multi-Agent Collaboration:** Split the workflow into specialized roles (e.g., a "Researcher" agent that finds data and a "Writer" agent that compiles the report).
* **[ ] Deep Content Reading:** Add a "Scraper" tool allowing the agent to visit URLs and read full articles/PDFs, rather than just relying on search snippets.
* **[ ] Local Model Support:** Add support for running local LLMs (via Ollama/Llama 3) for privacy-focused research.
* **[ ] Export Options:** specific buttons to download the final report as a `.pdf` or `.md` file.


https://github.com/user-attachments/assets/7e4377e4-bc36-411c-a301-48dc27b0fa55


  
