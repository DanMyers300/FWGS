from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from constants import BASE_URL, model, embeddings_model_name, PERSIST_DIRECTORY, target_source_chunks

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

@app.route('/embed')
def embed_documents():  
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
