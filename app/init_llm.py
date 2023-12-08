#!/usr/bin/env python3
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
import chromadb
import os
import requests

model = os.environ.get("MODEL", "llama2:7b-chat")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))

from constants import CHROMA_SETTINGS

def pull_model(model):
    url = "http://localhost:11434/api/pull"
    data = {
        "name": model
    }

    response = requests.post(url, json=data)

    # Check the response status
    if response.status_code == 200:
        print("Model pulled.")
    else:
        print(f"Failed to pull model. Status code: {response.status_code}")

# Initialize components outside of the route handler
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
callbacks = [StreamingStdOutCallbackHandler()]
llm = Ollama(model=model, callbacks=callbacks)

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
)
