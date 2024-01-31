import math
ls = input('Skriv en vektor: ').splite()
a = [float(e) ** 2 for e in ls]
l = math.sqt(sum(a))
print(f'Längden blir: {l:0.2f}')