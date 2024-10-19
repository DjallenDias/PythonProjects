from flask import Flask

app = Flask(__name__)

# When we use the rout with a '/´ at the end, as below
# that url is treated as a folder

@app.route("/projects/")
def projects():
    return "The project page"

# And without a '/' at the end, it's like a file
# index.html or smth

@app.route("/about")
def about():
    return "The about page"