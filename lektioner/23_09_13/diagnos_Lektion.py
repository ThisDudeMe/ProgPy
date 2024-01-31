from isPrime_Lektion import is_prime

n = int(input("number input"))


if n<=99:
    for i in range(2, n+1):
        if is_prime(i):
            print(1, end = ', ')

else:
    print("nONONONONNNON")