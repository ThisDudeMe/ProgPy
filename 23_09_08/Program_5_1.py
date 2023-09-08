
from numpy import empty


def Calculate():
    
    try:
        while True:
            userInput = str(input("write your text")).lower()
            content = len(userInput)
            if content > 0:
                print("sdsd")

    except Exception as e:
        e = "problem"
        print(e)