# Agentic‑AI‑Langgraph 🚀

A lightweight yet powerful framework for building **agentic AI workflows** using LangGraph and Streamlit.  
This project demonstrates how to orchestrate a language‑model‑driven AI agent with backend logic and a simple frontend UI.

---

## 🔹 Features

- LangGraph‑based backend (`backend.py`) for agent workflow orchestration  
- Streamlit frontend (`frontend.py`) for easy user interaction  
- Clear separation between backend processing and UI  
- Designed for local testing and easy extension

---

## 🛠️ Getting Started

Follow these steps to set up and run the project:

### 1. Clone or download the project
git clone https://github.com/Rahul-153/Agentic-AI-Langgraph.git
cd Agentic-AI-Langgraph

Or download the ZIP and extract it.

⸻

### 2. Create a virtual environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate.bat  # Windows


⸻

### 3. Install dependencies

pip install -r requirements.txt

Ensure requirements.txt includes LangGraph, Streamlit, and any necessary LLM packages.

⸻

### 4. Start the backend

Open one terminal tab:

python backend.py


⸻

### 5. Launch the frontend

In another tab:

streamlit run frontend.py

Your app will be available at http://localhost:8501.

⸻

✅ Usage
	1.	Interact via the frontend UI
	2.	Frontend sends prompts to the backend agent
	3.	LangGraph processes inputs and generates responses
	4.	Results are displayed in the UI

⸻

🧠 Extending the Project

To customize the agent:
	•	Modify backend.py to add new graph nodes, tools, or prompts
	•	Extend memory, branching, or tool capabilities
	•	Restart backend and frontend to test changes

⸻