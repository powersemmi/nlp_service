from flask import Flask

from app.routing import

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"
