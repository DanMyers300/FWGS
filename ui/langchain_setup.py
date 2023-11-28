#!/usr/bin/env python3
import subprocess
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
import chromadb
import os

model = os.environ.get("MODEL", "llama2:7b-chat")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))

from constants import CHROMA_SETTINGS

# Initialize components outside of the route handler
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
callbacks = [StreamingStdOutCallbackHandler()]
llm = Ollama(model=model, callbacks=callbacks)

# Run "ollama pull llama2" command
subprocess.run(["ollama", "pull", model])

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
)
