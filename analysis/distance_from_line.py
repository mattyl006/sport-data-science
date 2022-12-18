import numpy as np
from numpy.linalg import norm

def distance_from_line(p1, p2, p3):
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)
    return norm(np.cross (p2 - p1, p1 - p3)) / norm(p2 - p1)