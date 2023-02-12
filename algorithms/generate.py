import numpy as np


# Generate Random Instances using capacity mean and standard deviation
def generate_instances(n, p, capacity_mean, capacity_stddev):
    # Generate 2D positions for n nodes
    nodes = np.random.rand(n, 2)
    # Generate capacities for clusters
    capacities = np.random.normal(capacity_mean, capacity_stddev, p)
    return nodes, capacities


# Generate Random Weights using weight mean and standard deviation
def generate_weights(n, weight_mean, weight_stddev):
    # Generate weights for n nodes
    weights = np.random.normal(weight_mean, weight_stddev, n)
    return weights
