from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")


app = FastAPI()
embeddings = HuggingFaceEmbeddings()

class Query(BaseModel):
    url: str
    question: str

def create_db_from_youtube_video_url(video_url):
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)
    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    chat = ChatGroq(api_key=groq_api_key, 
    model="llama3-70b-8192", 
    temperature=0)


    system_template = """You are a helpful assistant that can answer questions about YouTube videos based on the transcript: {docs}

Only use the factual information from the transcript to answer the question.
If you don't have enough information, say "I don't know"."""

    system_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_prompt = HumanMessagePromptTemplate.from_template("Answer the following question: {question}")
    chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(question=query, docs=docs_page_content)
    return response.strip()

@app.post("/ask")
def ask_question(data: Query):
    try:
        db = create_db_from_youtube_video_url(data.url)
        answer = get_response_from_query(db, data.question)
        return {"response": answer}
    except Exception as e:
        return {"error": str(e)}
