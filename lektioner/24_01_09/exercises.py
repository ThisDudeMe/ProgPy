# 2





"""

# 1
class Countdown:

    def __init__(self, start = 10):

        self.n = start

    def __iter__(self):

        return self
    
    def __next__(self):

        if self.n >= 0:
            result = self.n
            self.n -= 1

            return result
        
        else:
            raise StopIteration
        

iterator = Countdown()

for i in iterator:
    print(i)
    
    """
    

        
