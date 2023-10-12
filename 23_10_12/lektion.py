import numpy as np

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
