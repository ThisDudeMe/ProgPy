'''import numpy as np
from colorama import Fore as Color

k = 3
nk = 5

#horizontal |
row = 8

#vertical ---
column = 5

klassification = np.zeros((row, column))
klassification[:, 1] = [9, 40, 50, 60, 10, 70, 60, 25]
klassification[:, 2] = [9, 20, 50, 90, 25, 70, 10, 80]
# red == 0 blue == 1
klassification[:, 3] = [9, 0, 1, 1, 0, 1, 0, 1]
klassification[0, 4] = k
klassification[0, 5] = nk

y1 = 20
y2 = 35

for i in range(row):
    x1 = klassification[i, 1]
    x2 = klassification[i, 2]

    distance = np.sqrt((x2-x1)**2+(y2-y1)**2)
    klassification[i, 4] = distance


for i in range(row):
    x1 = klassification[i, 1]
    x2 = klassification[i, 2]
    
    distance = np.sqrt((x2-x1)**2+(y2-y1)**2)
    klassification[i, 5] = distance

    print((klassification[0, 4]), "K IS 3", end=' ')
    print((klassification[0, 5]), "K IS ", end=' ')

for i in range(row):

    if k == 3:

        print(Color.RED + str(klassification[0, 4]), end=' ')
        if klassification[i, 2] == 0:
            print(Color.RED + str(klassification[i, 4]), end=' ')
        elif klassification[i, 2] == 1:
            print(Color.MAGENTA + str(klassification[i, 4]), end=' ')

    elif k == 5:

        print(Color.RED + str(klassification[0, 5]), end=' ')
        if klassification[i, 2] == 0:
            print(Color.RED + str(klassification[i, 5]), end=' ')
        elif klassification[i, 2] == 1:
            print(Color.MAGENTA + str(klassification[i, 5]), end=' ')


k = 3

#horizontal |
row = 7

#vertical ---
column = 4

klassification = np.zeros((row, column))
klassification[:, 0] = [40, 50, 60, 10, 70, 60, 25]
klassification[:, 1] = [20, 50, 90, 25, 70, 10, 80]

# red == 0 blue == 1
klassification[:, 2] = [0, 1, 1, 0, 1, 0, 1]

for i in range(row):
    x1 = klassification[i, 0]
    x2 = klassification[i, 1]
    y1 = 20
    y2 = 35
    
    distance = np.sqrt((x2-x1)**2+(y2-y1)**2)
    klassification[i, 3] = distance


print(klassification)
'''