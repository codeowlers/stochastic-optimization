import time
import numpy as np
import math

def kmcc_clustering(nodes, capacities, weights):
    start = time.time()
    p = len(capacities)
    n = len(nodes)
    clusters = np.zeros(n, dtype=int)
    center_nodes = np.zeros((p, 2))
    total_weight = np.zeros(p)
    # Initialize clusters randomly
    for i in range(n):
        clusters[i] = np.random.randint(0, p)
    # Repeat until convergence
    for _ in range(100):
        # Reset center nodes and total weights
        center_nodes = np.zeros((p, 2))
        total_weight = np.zeros(p)
        for i in range(n):
            center_nodes[clusters[i]] += nodes[i] * weights[i]
            total_weight[clusters[i]] += weights[i]
        # Calculate the mean position of each cluster
        for i in range(p):
            center_nodes[i] /= total_weight[i]
        # Assign each node to the closest center
        for i in range(n):
            min_distance = math.inf
            min_cluster = None
            for j in range(p):
                distance = np.linalg.norm(nodes[i] - center_nodes[j])
                if distance < min_distance and total_weight[j] + weights[i] <= capacities[j]:
                    min_distance = distance
                    min_cluster = j
            if min_cluster is not None:
                clusters[i] = min_cluster
                total_weight[min_cluster] += weights[i]
    # Return the index of nodes in each cluster
    result = []
    for i in range(p):
        result.append(np.where(clusters == i)[0])
    # Calculate the within-cluster sum of squares (WCSS) 
    wcss = 0.0
    for i in range(n):
        wcss += np.linalg.norm(nodes[i] - center_nodes[clusters[i]]) ** 2

    end = time.time()
    # Return the list of clusters, each represented by a list of node indices
    return result, end - start, wcss

