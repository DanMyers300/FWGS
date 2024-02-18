import os
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from constants import (
    BASE_URL,
    model,
    embeddings_model_name,
    PERSIST_DIRECTORY,
    target_source_chunks,
    CHROMA_SETTINGS,
)
from ingest import process_documents, does_vectorstore_exist, persist_directory

app = Flask(__name__)
CORS(app)

app.secret_key = os.urandom(24)

embeddings = OllamaEmbeddings(model=embeddings_model_name, base_url=BASE_URL)
db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
llm = Ollama(model=model, base_url=BASE_URL)

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
)

UPLOAD_FOLDER = "data/loading"
ALLOW_EXTENSIONS = {"txt", "pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    """Display main page"""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Chat with the model"""
    data = request.get_json()
    query = data.get("query")

    if query:
        res = qa(query)
        answer, docs = res["result"], res["source_documents"]
        serialized_docs = [doc.__dict__ for doc in docs]
        return jsonify(
            "answer", {"query": query, "answer": answer, "documents": serialized_docs}
        )
    else:
        return jsonify({"error": "Invalid query"}), 400


def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOW_EXTENSIONS


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    """Uploads a file to the server."""
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("embed_documents"))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """


@app.route("/embed", methods=["GET", "POST"])
def embed_documents():
    """Embeds documents and creates a new vectorstore."""
    if does_vectorstore_exist(persist_directory):
        print(f"Appending to existing vectorstore at {persist_directory}")
        db = Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings,
            client_settings=CHROMA_SETTINGS,
        )
        collection = db.get()
        texts = process_documents(
            [metadata["source"] for metadata in collection["metadatas"]]
        )
        print("Creating embeddings. May take some minutes...")
        db.add_documents(texts)
    else:
        print("Creating new vectorstore")
        texts = process_documents()
        print("Creating embeddings. May take some minutes...")
        db = Chroma.from_documents(
            texts, embeddings, persist_directory=persist_directory
        )
    db.persist()
    db = None

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
