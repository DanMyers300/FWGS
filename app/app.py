#!/usr/bin/env python3
from flask import Flask, render_template, request
from init_llm import qa

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

    # Render the template without redirecting
    return render_template("index.html", query=query, answer=answer, documents=docs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
