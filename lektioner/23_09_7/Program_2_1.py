userInputTodaysMilesCounter = float(input("How many miles your car run today?"))
userInputLastYearMilesCounter = float(input("How many miles your car run Last Year?"))
userBensinUsed = float(input("How many benisin used last year`?"))

miles = userInputTodaysMilesCounter - userInputLastYearMilesCounter
lPerM = userBensinUsed / miles

print("Your cars miles is", miles)
print("Your cars bensin usage is", lPerM)


