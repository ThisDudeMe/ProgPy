from flask import Flask, jsonify, request
from Database_Manager import *

app = Flask(__name__)
db_handler = DatabaseManager()

@app.route("/books", methods=["GET"])
def destination_handler_GET():
    db_handler.connect_to_database()
    user_input = request.args.to_dict()  

    if user_input:
        result = db_handler.filter_books(user_input)
    else:
        result = db_handler.show_all_books()

    db_handler.disconnect_from_database()
    return jsonify(result)

from flask import Flask, request, jsonify
from Database_Manager import DatabaseManager

@app.route("/books", methods=["POST"])
def add_book():
    db_handler.connect_to_database()
    book_data = (
        request.json.get('title'),
        request.json.get('author'),
        request.json.get('summary'),
        request.json.get('genre')
    )
    db_handler.add_book(book_data)
    db_handler.disconnect_from_database()
    return jsonify({"message": "Book added successfully"}), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def edit_book(book_id):
    db_handler.connect_to_database()
    updated_data = (
        request.json.get('title'),
        request.json.get('author'),
        request.json.get('summary'),
        request.json.get('genre')
    )
    db_handler.edit_book(book_id, updated_data)
    db_handler.disconnect_from_database()
    return jsonify({"message": "Book updated successfully"}), 200

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    db_handler.connect_to_database()
    db_handler.remove_book(book_id)
    db_handler.disconnect_from_database()
    return jsonify({"message": "Book deleted successfully"}), 200

@app.route("/reviews", methods=["POST"])
def add_review():
    db_handler.connect_to_database()
    review_data = (
        request.json.get('book_id'),
        request.json.get('user'),
        request.json.get('rating'),
        request.json.get('review_text')
    )
    db_handler.add_review(review_data)
    db_handler.disconnect_from_database()
    return jsonify({"message": "Review added successfully"}), 201

@app.route("/reviews", methods=["GET"])
def show_all_reviews():
    db_handler.connect_to_database()
    reviews = db_handler.show_all_reviews()
    db_handler.disconnect_from_database()
    return jsonify(reviews), 200

@app.route("/reviews/<int:book_id>", methods=["GET"])
def show_reviews_by_book(book_id):
    db_handler.connect_to_database()
    reviews = db_handler.show_review_by_book(book_id)
    db_handler.disconnect_from_database()
    return jsonify(reviews), 200

@app.route("/top_books", methods=["GET"])
def show_top_books():
    db_handler.connect_to_database()
    top_books = db_handler.show_top_books()
    db_handler.disconnect_from_database()
    return jsonify(top_books), 200

@app.route("/author/<author_name>", methods=["GET"])
def show_author_info(author_name):
    db_handler.connect_to_database()
    author_info = db_handler.show_author_info(author_name)
    db_handler.disconnect_from_database()
    return jsonify(author_info), 200

if __name__ == '__main__':
    app.run(debug=True)


