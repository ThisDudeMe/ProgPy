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
        self.cursor.execute("SELECT * FROM Books")
        self.result = self.cursor.fetchall()
        return self.result

    def filter_books(self):
        query = "SELECT * FROM Books"
        

        

    def select_book_ID(self):
        pass

    def add_book(self):    
        pass
    
    def edit_book(self):
        pass

    def remove_book(self):
        pass

    def add_review(self):
        pass

    def show_all_reviews(self):
        pass

    def show_review_by_book(self):
        pass

    def show_top_books(self):
        pass

    def show_author_info(self):
        pass

DatabaseManager()