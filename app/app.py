#!/usr/bin/env python3
import os
import json
import subprocess
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from utilities import pull_model
from utilities import delete_vectorstores

from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import Ollama

BASE_URL = os.environ.get('BASE_URL', 'http://localhost:11434')
model = os.environ.get("MODEL", "llama2:7b-chat")
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS", 4))

app = Flask(__name__)
socketio = SocketIO(app)

class DocumentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Document):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

app.json_encoder = DocumentEncoder

embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
callbacks = [StreamingStdOutCallbackHandler()]
llm = Ollama(model=model, callbacks=callbacks, base_url=BASE_URL)

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('ask')
def handle_ask(data):
    query = data.get('query')
    if query:
        res = qa(query)
        answer, docs = res["result"], res["source_documents"]

        serialized_docs = [doc.__dict__ for doc in docs]

        socketio.emit('answer', {"query": query, "answer": answer, "documents": serialized_docs})

@app.route('/init', methods=['POST'])
def init():
    pull_model()
    return jsonify({"result": "Model pulled."})

@app.route('/ingest', methods=['POST'])
def ingest():
    try:
        subprocess.run(['python', 'ingest.py'])
        return jsonify({'status': 'success', 'message': 'Ingestion completed successfully'})
    except Exception as e:
        error_message = f'Error during ingestion: {str(e)}'
        print(error_message)
        return jsonify({'status': 'error', 'message': error_message}), 500

@app.route('/cleardb', methods=['POST'])
def clear_chromadb_route():
    return delete_vectorstores()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
