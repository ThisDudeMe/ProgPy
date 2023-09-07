min = int(input("Enter the estimated monthly call minutes: "))

if min <= 33:
    recommendation = "Kontant"
elif min <= 66:
    recommendation = "Normal"
else:
    recommendation = "Plus"

print("You should choose the", recommendation, "subscription plan.")
