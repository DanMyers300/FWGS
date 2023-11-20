#!/usr/bin/env python3
from flask import Flask, render_template, request
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
import chromadb
import os
import time

app = Flask(__name__)

model = os.environ.get("MODEL", "llama2")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))

from constants import CHROMA_SETTINGS

# Initialize components outside of the route handler
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
callbacks = [
    StreamingStdOutCallbackHandler()
]  # Streaming callback always active for simplicity
llm = Ollama(model=model, callbacks=callbacks)
qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask_question():
    query = request.form.get("query")
    if query.strip() == "":
        return render_template("index.html", result="Please enter a non-empty query.")

    res = qa(query)
    answer, docs = res["result"], res["source_documents"]

    return render_template("index.html", query=query, answer=answer, documents=docs)


if __name__ == "__main__":
    app.run(debug=True)
