import ollama
from ollama import Client
from flask import Flask, render_template

app = Flask(__name__)
client = Client(host='http://localhost:11434')

def chat_generator():
    stream = client.chat(
        model='llama2',
        messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
        stream=True,
    )
    for chunk in stream:
        yield chunk['message']['content']

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/pull')
def pull():
    ollama.pull('llama2')
    return 'Pulled model'

@app.route('/chat')
def chat():
    message_content = ''.join(chat_generator())
    app.logger.info(message_content)
    return message_content

@app.route('/embed')
def embed_documents():  
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
