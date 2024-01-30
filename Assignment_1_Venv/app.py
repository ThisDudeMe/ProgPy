from flask import Flask, jsonify, request
from Database_Manager import *

app = Flask(__name__)
db_handler = DatabaseManager()

@app.route("/books", methods = ["GET"])
def destination_handler_GET():

    db_handler.connect_to_database()
    user_input = request.args

    if not user_input:
        result = db_handler.show_all_books()
        db_handler.disconnect_from_database()
        return jsonify(result)
    
    else:
        
        for i in user_input:
            if i == 
