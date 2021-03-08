from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/_test____conn', methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def test_conn():
    if request.method == "GET":
        return "OK"
    elif request.method == "POST":
        pass
    elif request.method == "HEAD":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
