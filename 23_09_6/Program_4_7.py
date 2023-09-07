def inputJudgeScore(judgeNumber):
    while True:
        try:
            judgeScore = float(input(f"Input score for Judge {judgeNumber} between 0 and 10: "))
            if 0 <= judgeScore <= 10:
                return judgeScore
            else:
                print("Invalid input. Please enter a score between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a correct number.")

def createJudgeFunctions(judgeCount):
    judgeFunctions = []

    for i in range(1, judgeCount + 1):
        def judgeTemplate(judgeNumber):
            while True:
                try:
                    judgeScore = inputJudgeScore(judgeNumber)
                    if 0 <= judgeScore <= 10:
                        return judgeScore
                    else:
                        print("Invalid input. Please enter a score between 0 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a correct number.")

        judgeFunctions.append(judgeTemplate(i))

    return judgeFunctions

def calculate(judgeScores):
    if len(judgeScores) < 3:
        print("There must be a minimum of 3 judges to calculate the results.")
        return None

    judgeScores.sort()
    judgeScores = judgeScores[1:-1]

    difficulty = 2.0

    averageScore = sum(judgeScores) / len(judgeScores)

    finalScore = averageScore * 3 * difficulty
    return finalScore

def Start():
    judgeCount = int(input("How many judges?: "))
    
    if judgeCount < 3:
        print("There must be a minimum of 3 judges.")
        return
    
    judgeFunctions = createJudgeFunctions(judgeCount)
    judgeScores = []

    for i, judgeFunction in enumerate(judgeFunctions, 1):
        score = judgeFunction()
        print(f"Judge {i} scored: {score}")
        judgeScores.append(score)

    finalScore = calculate(judgeScores)
    
    if finalScore is not None:
        print(f"The final diving score is: {finalScore:.2f}")

Start()