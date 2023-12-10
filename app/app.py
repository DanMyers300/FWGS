#!/usr/bin/env python3
import os
import json
import subprocess
from flask import Flask, render_template, request, jsonify
from llm import qa, pull_model
from ingest import delete_vectorstores

app = Flask(__name__)

class DocumentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Document):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

app.json_encoder = DocumentEncoder

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_question():
    query = request.form.get("query")
    if not query.strip():
        return jsonify({"error": "Please enter a non-empty query"})

    res = qa(query)
    answer, docs = res["result"], res["source_documents"]

    # Serialize Document objects
    serialized_docs = [doc.__dict__ for doc in docs]

    return jsonify({"query": query, "answer": answer, "documents": serialized_docs})

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
    app.run(host='0.0.0.0', port=5000, debug=True)
