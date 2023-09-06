from flask import Flask, request, jsonify
from extrato import Extrato
from flask_cors import CORS
from excel import Excel

app = Flask(__name__) 
CORS(app)

@app.route('/')
def index():
    return 'teste get'

@app.route('/pdf2excel', methods=['POST'])
def post():
    try:
        pdf_file = request.files['file[]']
        words_filter = request.form
        extrato, list_words, infos = Extrato(pdf_file, words_filter)
        print('passou daqui')
        excel_file = Excel(extrato, list_words, infos)
        return excel_file

    except Exception as e:
        return e


if __name__ == "__main__":
    app.run(debug=True)