from app import app

@app.route('/')
@app.route('/index')
def index() -> str:
    return "Hello World!"

@app.route('/_test____conn', methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def test_conn() -> str:
    return "OK"
