import numpy as np

#Euclidean distance between two points p and q
def euclidean_distance(p, q):
    return np.sqrt(np.sum((p-q)**2))