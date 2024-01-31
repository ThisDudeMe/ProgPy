#TODO: UPPGIFT: q = (1,1) p = (2,2) TODO: CALCULATE LENGTH OF LINE

from turtle import distance
import numpy as np


q = np.array([1,1])
p = np.array([2.2])


d = np.linalg.norm(q-p)

print(d)
