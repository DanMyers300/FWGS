#!/usr/bin/env python3
import json
import subprocess
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from utilities import pull_model

from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import Ollama

from utilities import BASE_URL, model, embeddings_model_name, persist_directory, target_source_chunks

app = Flask(__name__)
socketio = SocketIO(app)

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

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
