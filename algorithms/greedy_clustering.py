import time

def greedy_clustering(nodes, capacities, weights):
    start = time.time()
    n = nodes.shape[0]
    p = len(capacities)

    # Create a list to store the clusters
    clusters = [[] for _ in range(p)]

    # Create a list to store the remaining capacities of each cluster
    remaining_capacities = capacities.copy()

    # Sort the nodes by their weights in descending order
    node_weights = [(node, weight) for node, weight in enumerate(weights)]
    node_weights.sort(key=lambda x: x[1], reverse=True)

    # Greedily assign each node to a cluster with enough capacity
    for node, weight in node_weights:
        for j in range(p):
            if remaining_capacities[j] >= weight:
                clusters[j].append(node)
                remaining_capacities[j] -= weight
                break
    end = time.time()
    # Return the list of clusters, each represented by a list of node indices
    return clusters, end - start
