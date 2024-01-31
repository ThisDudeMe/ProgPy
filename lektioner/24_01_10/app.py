from flask import Flask, request

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello world"


@app.route("/submit", methods=["POST"])
def submit():
    print(request.json)
    json_body = request.json
    print(json_body["title"])
    # Databaslogik
    return {"message": "Data submitted successfully!"}

@app.route("/books/<requested_book>")
def books(requested_book):
    print(requested_book)
    return "Lorem ipsum"

@app.route("/books")
def get_books():
    print(request.args)
    return "Lorem ipsum"





