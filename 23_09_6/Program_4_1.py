
def CheckForInput():
    userInputArray = []
    finnishedBool = False
    
    while finnishedBool == False:

        userInput = float(input("Input your number"))
        userInputArray.append((userInput))
    
        if userInput < 0:
            break

    userInputArray.sort()
    lowestValue = userInputArray[0]
    highestValue = userInputArray[-1]
    #print(" Lowest value is", lowestValue)
    #print(" Highest value is", highestValue)

CheckForInput()