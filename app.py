from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "Root"


@app.route('/helloworld', methods=['GET'])
def hello_world():
    return "Hello World"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello " + name

@app.route('/replace', methods=['POST'])
def replace():
    if request.method == 'POST':
        content = request.json

        text = content['text']
        word_to_replace = content['word_to_replace']
        replacement_word = content['replacement_word']

        updated_text = text.replace(word_to_replace, replacement_word)

        return jsonify({"updated_text": updated_text})

if __name__ == "__main__":
    app.run(debug=True)