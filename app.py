from flask import Flask, request, jsonify
from extrato import Extrato
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)

@app.route('/')
def index():
    return 'teste get'

@app.route('/pdf', methods=['POST'])
def post():
    try:
        pdf_file = request.files['file[]']
        words_filter = request.form
        extrato = Extrato(pdf_file, words_filter)
        return extrato

    except Exception as e:
        return e


if __name__ == "__main__":
    app.run(debug=True)