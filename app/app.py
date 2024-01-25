from ollama import Client
from utilities import BASE_URL, model, embeddings_model_name, persist_directory, target_source_chunks
from flask import Flask, render_template
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

app = Flask(__name__)
client = Client(host='http://localhost:11434')
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
callbacks = [StreamingStdOutCallbackHandler()]
llm = Ollama(model=model, callbacks=callbacks, base_url=BASE_URL)

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
)

def chat_generator():
    stream = client.chat(
        model='llama2',
        messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
        stream=True,
        context=True,
    )
    for chunk in stream:
        yield chunk['message']['content']

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chat')
def chat():

@app.route('/embed')
def embed_documents():  
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
