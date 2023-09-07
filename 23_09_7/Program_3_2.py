import numpy as np

radius = float(input("Enter the radius of the circle: "))


if np.greater(radius, 0):

    circumference = 2 * np.pi * radius
    area = np.pi * radius**2

   
    print("Circumference:", circumference)
    print("Area:", area)
else:
    print("Invalid input. Radius must be greater than 0.")
