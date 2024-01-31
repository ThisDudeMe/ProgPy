from optparse import Values
from copy import copy
from operator import index
from os import remove
from unittest import result
import numpy as np
import sys

class this:
   
    def Start():
        

        def Input():

            judgesInfo = {}

            while True:
                userAmountOfJudge = int(input("Please type the amount of judges MUST BE MINIMUM 3!!! "))
                try:
                    if userAmountOfJudge >= 3:

                        for judgeName in range(userAmountOfJudge):
                            
                            judgeName = str(input("Please enter the judge Name. ",))
                            judgeScore = float(input(f"PleaseEnter {judgeName}`s score!"))

                            judgesInfo[judgeName] = judgeScore

                        difficulty = float(input("Please enter the difficulty "))
                        break
                    else:
                        print("Error! There must be minimum 3 judges")
                        
                except Exception:
                    print("Error: Please use numbers 0 to 9 !")

            return judgesInfo, difficulty

        def Calculate():

            inputToCalculate = Input()

            judgesInfo, difficulty = inputToCalculate

            modifying = list(judgesInfo.values())

            modifying.sort()
            modifying.pop(0)
            modifying.pop()

            toCalculate = modifying.copy()

            meanV = np.mean(toCalculate)

            result = (meanV * 3)* difficulty

            return result
    
        def Output():
            result = Calculate()
            
            print("Total score is: ", result)

            while True:

                confirmExit = float(input("Please enter any negative number to exit! OR any positive number restart! "))

                if confirmExit < 0:
                    sys.exit()
                
                else:
                    break

        Output()

    Start()