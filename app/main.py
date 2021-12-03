
from flask import Flask, json, render_template, request, jsonify, redirect
from flask.helpers import url_for
import requests
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    result = request.args['result'] if 'result' in request.args else '{"std_output" : "nada"}'
    return render_template('index.html', result=result)


@ app.route('/send_code', methods=['POST'])
def send_code():
    code_solved = requests.post(
        "http://127.0.0.1:4000/compile", json={"code": request.form['code']})
    return render_template('index.html', result=code_solved.json())


if __name__ == '__main__':
    app.run(debug=True)
