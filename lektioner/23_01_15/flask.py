# Importing Flask
from flask import Flask, request

# Creating a Flask Application
app = Flask(__name__)


# Defining a Route: Basic Home Page
@app.route("/")
def home():
    return "Hello, World!"


# Defining a Route with a Variable
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User: {username}"


# Using HTTP Methods: GET and POST
# Endpoint can handle several methods. Default is GET.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login POST Request"
    else:
        return "Login Page"


# Route to handle POST request and read JSON body
@app.route("/submit-json", methods=["POST"])
def handle_json():
    # Getting JSON data from request
    data = request.json

    # You can now process data and perform actions based on the content
    # For demonstration, we'll just return the same JSON data
    return "Success!"


# Running the Flask Application
if __name__ == "__main__":
    app.run(debug=True)
