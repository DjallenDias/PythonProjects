from pathlib import Path
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# <variable_name> - this say to us that the url will give us a variable with that name
# <int:variable_name> - the int: berofe, says us the type

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id: int):
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"
