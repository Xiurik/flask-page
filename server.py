from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<h1>Hello, Xiurik!</h1>"

@app.route("/template")
def template():
    return render_template('index/index.html')
