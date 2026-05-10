## ⚙️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector DB | FAISS (Facebook AI Similarity Search) |
| UI | Gradio |
| Language | Python |

## 🚀 How to Run

### Option 1 — Google Colab (Recommended)
1. Open the notebook in Google Colab
2. Run all cells in order
3. Upload your documents in the UI
4. Start asking questions!

### Option 2 — Run Locally
```bash
git clone https://github.com/AdarshVaggu/rag-chatbot
cd rag-chatbot
pip install -r requirements.txt
python app.py
```

## 📁 Supported File Types
- 📄 PDF (.pdf)
- 📝 Text files (.txt)
- 📊 CSV files (.csv)

## ✨ Features
- Upload any PDF, TXT, or CSV document
- Automatic text chunking with overlap
- Semantic similarity search using FAISS
- Answers strictly from uploaded documents
- Handles unknown queries gracefully
- Clean Gradio web UI

## ⚠️ Limitations
- Scanned PDFs (image-based) may not extract text properly
- Very large documents may take longer to process
- Requires active internet connection for Gemini API calls

## 📈 Suggestions for Scaling
- Replace FAISS with **Pinecone** or **Weaviate** for cloud-scale vector search
- Add **user authentication** for multi-user support
- Use **async processing** for handling large files
- Deploy on **Hugging Face Spaces** or **Google Cloud Run** for production
- Add support for **Word documents (.docx)** and **web URLs**

## 👨‍💻 Built By
Adarsh Vaggu — AI Internship Assignment
