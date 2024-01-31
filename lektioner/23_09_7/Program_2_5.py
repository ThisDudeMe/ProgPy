import numpy as np
uX1 = float(input("input x1"))
uX2 = float(input("input x2"))
uY1 = float(input("input y1"))
uY2 = float(input("input y2"))

s = np.sqrt((uX1 - uX2) ** 2 + (uY1 - uY2) ** 2)

print("result is ", s)