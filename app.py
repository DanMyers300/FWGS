from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='static')

@app.route('/')
def index():
    return render_template('ner.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['user_message']

if __name__ == '__main__':
    app.run(debug=True)
