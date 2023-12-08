#!/usr/bin/env python3
import json
from flask import Flask, render_template, request, jsonify
from init_llm import qa, pull_model
import subprocess

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
    subprocess.run(['python', 'ingest.py'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
