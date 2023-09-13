from sympy import false

def is_prime(x):

    if (x > 1):
        divisor = 2

        for i in range(divisor, x):
            if(x % i) == 0:
                return False
    else:

         return False
    
    return True
    

    
    