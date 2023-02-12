import numpy as np


# Euclidean distance between two points p and q
def euclidean_distance(p, q):
    # Use numpy's sqrt function to calculate the square root of the sum
    # of the squared differences between the two points
    return np.sqrt(np.sum((p - q) ** 2))
