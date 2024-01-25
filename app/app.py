from ollama import Client
from flask import Flask, render_template

from langchain.chains import RetrievalQA
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama

from constants import BASE_URL, model, embeddings_model_name, PERSIST_DIRECTORY, target_source_chunks

app = Flask(__name__)
client = Client(host=BASE_URL)

embeddings = Ollama(model=embeddings_model_name)
db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
llm = Ollama(model=model, base_url=BASE_URL)

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
)

# Without langchain
def chat_generator():
    stream = client.chat(
        model='llama2',
        messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
        stream=True,
        context=True,
    )
    for chunk in stream:
        yield chunk['message']['content']

# With langchain
def handle_chat(data):
    query = data.get('query')
    if query:
        res = qa(query)
        answer, docs = res["result"], res["source_documents"]

        serialized_docs = [doc.__dict__ for doc in docs]

        return {"query": query, "answer": answer, "documents": serialized_docs}

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chat')
def chat():
    return handle_chat(request.args)

@app.route('/embed')
def embed_documents():  
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
