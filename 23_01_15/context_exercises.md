### Intermediate Exercises

1. **Custom Context Manager for Timer:**
   - Implement a custom context manager to measure the execution time of a code block. Use it to time a function or any piece of code.
2. **Resource Management:**
   - Write a context manager that manages the connection to a hypothetical database. It should open and close the connection when entering and exiting the context.

### Advanced Exercises


3. **Thread-Safe Context Manager:**
   - Design a thread-safe context manager for managing a shared resource, ensuring that the resource is accessed by only one thread at a time.

### Solutions for Intermediate Exercises

1. **Custom Context Manager for Timer:**
   ```python
   import time

   class Timer:
       def __enter__(self):
           self.start = time.time()
           return self

       def __exit__(self, *args):
           self.end = time.time()
           print(f'Elapsed time: {self.end - self.start} seconds')

   with Timer():
       time.sleep(2)  # Example code block
   ```

2. **Resource Management:**
   ```python
   class DatabaseConnection:
       def __enter__(self):
           print("Open database connection")
           return self

       def __exit__(self, exc_type, exc_val, exc_tb):
           print("Close database connection")

   with DatabaseConnection() as db:
       print("Perform database operations")
   ```

### Solutions for Advanced Exercises

3. **Thread-Safe Context Manager:**
   ```python
   import threading

   class ThreadSafeResource:
       def __init__(self):
           self.lock = threading.Lock()

       def __enter__(self):
           self.lock.acquire()
           return self

       def __exit__(self, exc_type, exc_val, exc_tb):
           self.lock.release()

   resource = ThreadSafeResource()

   def access_resource():
       with resource:
           print("Resource accessed by", threading.current_thread().name)

   thread1 = threading.Thread(target=access_resource)
   thread2 = threading.Thread(target=access_resource)
   thread1.start()
   thread2.start()
   thread1.join()
   thread2.join()
   ```