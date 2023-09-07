sum = 0
i = 1

while True:
    term = 1 / i
    if abs(term) < 0.00001:
        break
    sum += term
    i += 1

print("The sum of the series is:", sum)