# Context Managers in Python
# --------------------------
# A context manager is a simple “protocol” (or interface) that your object needs to follow
# in order to support the "with" statement. It consists of two magic methods:
# __enter__() and __exit__().

# The most common use case of context managers is file handling.

# Example of using a context manager for file handling:

with open('example.txt', 'w') as file:
    file.write('Hello, World!')  # Write to the file
# After the block, the file is automatically closed, no need to explicitly call file.close()

# Creating a custom context manager:
# You can create a custom context manager using a class that defines __enter__() and __exit__() methods.

class MyContextManager:
    def __enter__(self):
        print("Enter the context!")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit the context!")
        # Can handle exceptions here if needed

# Using the custom context manager:

with MyContextManager() as manager:
    print("Inside the with statement!")

# Output:
# Enter the context!
# Inside the with statement!
# Exit the context!

# The __enter__ method is called when execution enters the context of the with statement
# and it returns an object which is bound to the variable after 'as'.
# The __exit__ method is called when execution leaves the context. Any exception that happens
# inside the with block is passed to the __exit__ method. If __exit__ returns False, the exception
# is re-raised, otherwise, it's suppressed.

