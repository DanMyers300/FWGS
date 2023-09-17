from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='static')

@app.route('/')
def index():
    return render_template('ner.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['user_message']
    # Here, you can add your chatbot logic to generate responses
    # For now, let's just echo the user's message
    bot_response = "You said: " + user_message
    return jsonify({"bot_response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
