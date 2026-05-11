# 📚 RAG Chatbot — Agentic RAG System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-green)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-red)
![HuggingFace](https://img.shields.io/badge/Deployed-HuggingFace%20Spaces-yellow)

An AI-powered chatbot that answers questions **strictly based on your uploaded documents** using Retrieval Augmented Generation (RAG). No hallucinations — if the answer isn't in the documents, it says so.

🚀 **Live Demo:** [Click here to try it](https://huggingface.co/spaces/AdarshVaggu/rag-chatbot)

---

## 🏗️ Architecture
---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector DB | FAISS (Facebook AI Similarity Search) |
| UI | Gradio |
| Hosting | Hugging Face Spaces |
| Language | Python 3.10 |

---

## ✨ Features

- 📄 Upload any PDF, TXT, or CSV document
- 🔪 Automatic text chunking with overlap
- 🔍 Semantic similarity search using FAISS
- 🤖 Answers strictly from uploaded documents only
- ❌ Handles unknown queries gracefully — no hallucinations
- 💬 Conversation memory
- 🌐 Clean Gradio web UI — works in any browser

---

## 🚀 How to Run

### Option 1 — Use Live App (No setup needed!)
👉 [https://huggingface.co/spaces/AdarshVaggu/rag-chatbot](https://huggingface.co/spaces/AdarshVaggu/rag-chatbot)

### Option 2 — Run Locally
```bash
# Clone the repo
git clone https://github.com/AdarshVaggu/rag-chatbot
cd rag-chatbot

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY="your-key-here"

# Run the app
python app.py
```

### Option 3 — Google Colab
Open in Colab, install requirements, and run `app.py` cell by cell.

---

## 📁 Supported File Types

| Format | Extension |
|--------|-----------|
| PDF | .pdf |
| Text | .txt |
| CSV | .csv |

---

## 🗂️ Project Structure
---

## 💡 How It Works

1. **Upload** your documents (PDF, TXT, or CSV)
2. **Processing** — text is extracted, chunked into 300-word pieces
3. **Embeddings** — each chunk is converted to a vector using Sentence Transformers
4. **Storage** — vectors stored in FAISS index for fast search
5. **Query** — your question is converted to a vector
6. **Retrieval** — top 4 most similar chunks are found
7. **Answer** — Gemini reads the chunks and answers your question

---

## ⚠️ Limitations

- Scanned PDFs (image-based) may not extract text properly
- Very large documents may take longer to process
- FAISS index is in-memory — documents need re-uploading per session
- Requires active Gemini API key

---

## 📈 Future Improvements

- Replace FAISS with Pinecone or Weaviate for persistent storage
- Add OCR support for scanned PDFs
- Support Word (.docx) and web URLs
- Add user authentication for multi-user support
- Deploy with Docker for production use

---

## 👨‍💻 Author

**Adarsh Vaggu**
- GitHub: [@AdarshVaggu](https://github.com/AdarshVaggu)

---
