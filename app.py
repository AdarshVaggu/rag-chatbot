import os
import faiss
import pickle
import numpy as np
import pandas as pd
import gradio as gr
from google import genai
from sentence_transformers import SentenceTransformer

GEMINI_API_KEY = "your-api-key-here"
client = genai.Client(api_key=GEMINI_API_KEY)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

current_index = None
current_chunks = []

def process_uploaded_files(files):
    global current_index, current_chunks
    if not files:
        return "Please upload at least one file."
    documents = []
    for file in files:
        filepath = file.name
        filename = os.path.basename(filepath)
        ext = os.path.splitext(filename)[1].lower()
        try:
            if ext == ".txt":
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()
            elif ext == ".pdf":
                import PyPDF2
                text = ""
                with open(filepath, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text += page.extract_text() + "\n"
            elif ext == ".csv":
                df = pd.read_csv(filepath)
                text = "Data from " + filename + ":\n"
                for _, row in df.iterrows():
                    text += " | ".join([str(col) + ": " + str(val) for col, val in row.items()]) + "\n"
            else:
                continue
            documents.append({"filename": filename, "content": text})
        except Exception as e:
            print("Error loading " + filename + ": " + str(e))
    if not documents:
        return "No supported files found. Please upload PDF, TXT, or CSV files."
    all_chunks = []
    for doc in documents:
        words = doc["content"].split()
        start = 0
        chunk_id = 0
        while start < len(words):
            chunk = " ".join(words[start:start+300])
            all_chunks.append({"text": chunk, "source": doc["filename"], "chunk_id": chunk_id})
            start += 250
            chunk_id += 1
    texts = [c["text"] for c in all_chunks]
    embeddings = embedding_model.encode(texts, show_progress_bar=False)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype("float32"))
    current_index = index
    current_chunks = all_chunks
    filenames = [doc["filename"] for doc in documents]
    return "Processed " + str(len(documents)) + " file(s): " + ", ".join(filenames) + ". Created " + str(len(all_chunks)) + " chunks. Ask away!"

def chat(user_message, history):
    global current_index, current_chunks
    if current_index is None:
        return "Please upload your documents first!"
    query_embedding = embedding_model.encode([user_message]).astype("float32")
    distances, indices = current_index.search(query_embedding, 4)
    relevant_chunks = []
    for i, idx in enumerate(indices[0]):
        relevant_chunks.append({
            "text": current_chunks[idx]["text"],
            "source": current_chunks[idx]["source"],
            "score": float(distances[0][i])
        })
    context = "\n".join(["[From " + c["source"] + "]: " + c["text"] for c in relevant_chunks])
    sources = list(set([c["source"] for c in relevant_chunks]))
    prompt = "You are a helpful document assistant. Answer ONLY based on the context below.\n\nCONTEXT FROM DOCUMENTS:\n" + context + "\n\nCURRENT QUESTION: " + user_message + "\n\nINSTRUCTIONS:\n- Answer ONLY from the context provided\n- If answer not found, say: I dont have information about this in the provided documents.\n- Be concise and helpful\n- Mention which document(s) you used\n\nANSWER:"
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    answer = response.text
    return answer + "\n\nSources: " + ", ".join(sources)

with gr.Blocks(title="RAG Chatbot") as demo:
    gr.Markdown("# Document Q&A Chatbot")
    gr.Markdown("Upload your documents (PDF, TXT, CSV) and ask questions about them!")
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Step 1 - Upload Documents")
            file_upload = gr.File(label="Upload PDF, TXT, or CSV", file_types=[".pdf", ".txt", ".csv"], file_count="multiple")
            upload_btn = gr.Button("Process Documents", variant="primary")
            upload_status = gr.Textbox(label="Status", interactive=False, lines=3)
            upload_btn.click(fn=process_uploaded_files, inputs=[file_upload], outputs=[upload_status])
        with gr.Column(scale=2):
            gr.Markdown("### Step 2 - Ask Questions")
            gr.ChatInterface(fn=chat, examples=["Give me a summary", "What are the main topics?", "What is the most important information?"])
    gr.Markdown("Built with Gemini + FAISS + Sentence Transformers")

if __name__ == "__main__":
    demo.launch()
