from application import app
from flask import render_template


@app.route("/")
@app.route("/index")

def index():
    return render_template('index.html')


@app.route("/home")

def home():
    return "<h1>This is my Home Page :)</h1>"


@app.route("/<name>")

def user(name):
    return f"Hello {name}"
