import numpy as np

sideA = float(input("Enter the length of side a: "))
sideB = float(input("Enter the length of side b: "))
angleADegrees = float(input("Enter the angle (in degrees) between sides a and b: "))

angleARadians = np.radians(angleADegrees)

sideC = np.sqrt(sideA**2 + sideB**2 - 2 * sideA * sideB * np.cos(angleARadians))

if np.isclose(sideA, sideB) and np.isclose(sideB, sideC):
    triangleType = "Equilateral"
elif np.isclose(sideA, sideB) or np.isclose(sideB, sideC) or np.isclose(sideA, sideC):
    triangleType = "Isosceles"
else:
    triangleType = "Scalene"


print("The triangle is:", triangleType)
