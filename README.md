# 🤖 RAG Chatbot with Gemini and LangChain

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask natural language questions. The system extracts content from the PDFs, embeds them using HuggingFace models, stores them in a Chroma vector database, and uses Google's Gemini (via LangChain) to generate context-aware answers.

---

## 🚀 Features

- 📁 Upload and process multiple PDF documents
- 🧠 Retrieve relevant chunks using vector similarity
- 🤖 Generate intelligent answers using **Gemini LLM**
- 💬 Chat-style Streamlit interface
- 🗂 View and download chat history
- 🧪 Inspect ChromaDB matches in real time

---

## 🧰 Tech Stack

| Component   | Technology                            |
| ----------- | ------------------------------------- |
| Frontend    | Streamlit                             |
| Backend     | Python                                |
| LLM         | Gemini (via `langchain-google-genai`) |
| Vector DB   | ChromaDB                              |
| Embeddings  | HuggingFace (`all-mpnet-base-v2`)     |
| PDF Parsing | PyPDFLoader                           |
| Framework   | LangChain                             |
| Deployment  | Local / Streamlit Cloud               |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gvignesh575/rag_chatbot_gemini.git
cd rag-chatbot-gemini
```

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install Dependencies

   pip install -r requirements.txt

4. Set up Environment Variables

   Create a .env file in the root directory and add your Gemini API key:
   GOOGLE_API_KEY=your_actual_key_here

5. ▶️ Running the App

   streamlit run index.py
