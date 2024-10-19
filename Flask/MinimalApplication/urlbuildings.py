from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# The url_for() function creates a URL for a Flask route using the function name
# letting you add parameters and avoiding the need to manually write URLs.

# url_for() function takes the name of a route function and optional parameters
# and returns the corresponding URL with the parameters included.

with app.test_request_context():
    print(url_for('index')) # out: /
    print(url_for('login')) # out /login
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))