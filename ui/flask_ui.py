#!/usr/bin/env python3
from flask import Flask, render_template, request
from langchain_setup import qa
import subprocess

app = Flask(__name__)

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

@app.route("/run_setup", methods=["GET", "POST"])
def run_setup():
    if request.method == "POST":
        try:
            subprocess.run(["python3", "langchain_setup.py"], check=True)
            message = "Setup script executed successfully!"
        except subprocess.CalledProcessError as e:
            message = f"Error executing setup script: {e}"
        
        return render_template("setup_result.html", message=message)
    
    return render_template("run_setup.html")

if __name__ == "__main__":
    app.run(debug=True)
