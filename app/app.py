from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from constants import BASE_URL, model, embeddings_model_name, PERSIST_DIRECTORY, target_source_chunks, CHROMA_SETTINGS
from ingest import process_documents, does_vectorstore_exist, persist_directory

app = Flask(__name__)
CORS(app)

embeddings = Ollama(model=embeddings_model_name)
db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
llm = Ollama(model=model, base_url=BASE_URL)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query')
    
    if query:
        response = "".join(llm.stream(query))
        return jsonify({"query": query, "response": response})
    else:
        return jsonify({'error': 'Invalid query'}), 400

@app.route('/embed', methods=['POST'])
def embed_documents():
    if does_vectorstore_exist(persist_directory):
        # Update and store locally vectorstore
        print(f"Appending to existing vectorstore at {persist_directory}")
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
        collection = db.get()
        texts = process_documents([metadata['source'] for metadata in collection['metadatas']])
        print(f"Creating embeddings. May take some minutes...")
        db.add_documents(texts)
    else:
        # Create and store locally vectorstore
        print("Creating new vectorstore")
        texts = process_documents()
        print(f"Creating embeddings. May take some minutes...")
        db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)
    db.persist()
    db = None

    return(f"Ingestion complete!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
