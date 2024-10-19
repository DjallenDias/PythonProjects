from flask import Flask
from markupsafe import escape

# We use escape() to protect from injection attacks

app = Flask(__name__)

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}!"