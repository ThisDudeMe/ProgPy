from email import iterators
import random

class MyIterator:

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
       self.current += 1

       if self.current > 6:
           raise StopIteration
       return self.current
    
