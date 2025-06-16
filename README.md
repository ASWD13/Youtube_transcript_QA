# YouTube-RAG-QA

**A browser-based RAG application leveraging YouTube transcripts, semantic retrieval (FAISS), and real-time LLM responses.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-brightgreen?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-RAG-yellow?style=flat-square)
![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-orange?style=flat-square)

---

## 🚀 Overview

YouTube-RAG-QA is a full-stack generative AI application packaged as a **Chrome extension**. It allows users to **ask natural language questions about any YouTube video**, powered by:

- Transcript-based retrieval (using `youtube-transcript-api`)
- Semantic chunking and vector storage (via FAISS)
- LLM-powered answering (via Groq + Meta's LLaMA-3)
- Real-time communication with a Python backend (FastAPI)

### 🔍 Use Case

Ever watched a long YouTube video and wished you could just ask, "What's this about?"  
This tool extracts the transcript (if available), chunks and embeds it, and uses an LLM to answer your question accurately using only the video content.

---

## 🛠️ Tech Stack

| Layer       | Technology                      |
|-------------|----------------------------------|
| Frontend    | HTML, CSS, JavaScript (Chrome Extension) |
| Backend     | FastAPI (Python)                |
| LLM Access  | GroqCloud API (LLaMA 3 - 70B)   |
| RAG Engine  | LangChain + FAISS               |
| Transcript  | youtube-transcript-api          |
| Embeddings  | HuggingFace Sentence Transformers |

---

## 📦 Setup Instructions (Local)

### 1. Clone the repo

```bash
git clone https://github.com/ASWD13/youtube-RAG-QA.git
```

### 2. Create a .env file

```
GROQ_API_KEY=your_groqcloud_api_key
```

### 3. Install requirements
```
pip install -r requirements.txt
```

### 4. Run the backend
```
python main.py
```
## 🧩 Using the Chrome Extension

1. Open Chrome and go to chrome://extensions
2. Turn on Developer mode (top right)
3. Click Load unpacked
4. Select the extension folder inside this repo
5. You should now see the extension in your toolbar

### To use:

1. Paste a YouTube URL (make sure it contains a transcript — auto or manual)
2. Type your question
3. Wait for a response from the AI (response time varies depending on transcript length)

## ⚠️ Limitations

1. YouTube videos without transcripts will not work
2. Multi-language transcript support is not implemented
3. LLM responses may take a few seconds
