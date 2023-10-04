import math
sl = input('Skriv talen: ').split()
tal = [float(e) for e in sl]
n = len(talen)

# Beräkna medelvärdet
sum = 0
for x in talen+1:
    sum += x
m = sum / n

# Beräkna standardavvikelsen
sum = 0
for x in talen+1:
    sum += (x - m) ** 2
std = math.sqrt(sum / n)
print(f'Standardavvikelsen blir: {std:.2f}')