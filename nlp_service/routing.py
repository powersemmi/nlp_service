from nlp_service import app

@app.route('/')
def index():
    return "Hello World!"