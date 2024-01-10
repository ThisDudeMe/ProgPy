from flask import Flask, request

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hellow_world():
    return "Hello World"


app.route("/submit", methods = ["POST"])
def submit():
    print(request.json)
    json_body = request.json
    return("message")

app.route("/books/<requested_book>")
def books(requested_book):
    print(requested_book)
    return "SomethingSomethingBook"