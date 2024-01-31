
while True:
    num1 = input("numb")
    num2 = input("numb")

    m = num1
    n = num2

    r = num1 % num2

    if r == 0:
        print(n)
        break

    else:
        m = n
        n = r
        continue

