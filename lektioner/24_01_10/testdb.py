import sqlite3
import tkinter as tk
from tkinter import filedialog
import os


class DatabaseManager:

    def connect_to_database(self):

        self.file_location = os.path.dirname(os.path.abspath(__file__))
        self.data_base = os.path.join(self.file_location, "Book_Reviews.db")

        if not os.path.exists(self.data_base):
            self.root = tk.Tk()
            self.root.withdraw()
            self.data_base = filedialog.askopenfilename(title = "Select Database File", filetypes = [("SQLite Database Files", "*.db")])
            self.root.destroy()

            if self.data_base:
                self.connection = sqlite3.connect(self.data_base)
            
            else:
                print("File was not found!")
                exit()

        else:
            self.connection = sqlite3.connect(self.data_base)

        self.cursor = self.connection.cursor()
        return self.cursor
    
    def disconnect_from_database(self):
       
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

    def show_all_books(self):
        self.query = "SELECT * FROM Books"
        self.cursor.execute(self.query)
        self.result = self.cursor.fetchall()
        return self.result

    def filter_books(self, user_input):
        query = "SELECT * FROM Books"
        conditions = []
        parameters = []

        
        for category in ["BookID", "Title", "Author", "Summary", "Genre"]:
            if category.lower() in user_input:
                if category == "BookID":  
                    conditions.append(f"{category} = ?")
                    parameters.append(int(user_input[category.lower()]))
                else:
                    conditions.append(f"{category} LIKE ?")
                    parameters.append(f"%{user_input[category.lower()]}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()

    def select_book_ID(self, user_input):
        self.query = f"SELECT * FROM Books WHERE BookID = {user_input} "
        self.cursor.execute(self.query)
        return self.cursor.fetchall()

    def add_book(self, book_data):
        query = "INSERT INTO Books (Title, Author, Summary, Genre) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, book_data)
        self.connection.commit()

    
    def edit_book(self, book_id, updated_data):
        query = "UPDATE Books SET Title = ?, Author = ?, Summary = ?, Genre = ? WHERE BookID = ?"
        self.cursor.execute(query, updated_data + (book_id,))
        self.connection.commit()

    def remove_book(self, book_id):
        query = "DELETE FROM Books WHERE BookID = ?"
        self.cursor.execute(query, (book_id,))
        self.connection.commit()

    def add_review(self, review_data):
        query = "INSERT INTO Reviews (BookID, User, Rating, ReviewText) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, review_data)
        self.connection.commit()

    def show_all_reviews(self):
        query = "SELECT * FROM Reviews"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_review_by_book(self, book_id):
        query = "SELECT * FROM Reviews WHERE BookID = ?"
        self.cursor.execute(query, (book_id,))
        return self.cursor.fetchall()

    def show_top_books(self, limit=10):
        query =     """
                        SELECT Books.BookID, Books.Title, AVG(Reviews.Rating) as AverageRating
                        FROM Books
                        JOIN Reviews ON Books.BookID = Reviews.BookID
                        GROUP BY Books.BookID
                        ORDER BY AverageRating DESC
                        LIMIT ?
                    """
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()

    def show_author_info(self, author):
        query = """
        SELECT Author, Title, AVG(Reviews.Rating) as AverageRating
        FROM Books
        LEFT JOIN Reviews ON Books.BookID = Reviews.BookID
        WHERE Author = ?
        GROUP BY Books.BookID
        """
        self.cursor.execute(query, (author,))
        return self.cursor.fetchall()








