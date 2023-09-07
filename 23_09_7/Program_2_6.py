import numpy as np

t = int(input('Antal år? '))
lam = np.log(2.0) / 5730
n0 = 100
rest = n0 * np.exp(-lam * t)
print("result ", rest)
