import numpy as np
from .gurobi_model import *
from .evaluation_metrics import *
from .generate import *
from .split_data import *


def insample_stability(clusters_reference, nodes, capacities, weights, lambda_param, num_runs=100):
    jaccard_scores = []
    for i in range(num_runs):
        # Run the clustering algorithm `num_runs` times
        clusters, _, obj_val = solve_model(nodes, capacities, weights, lambda_param, 'ccp')
        # Compute the Jaccard similarity between the obtained clusters and the reference clusters
        jaccard_scores.append(jaccard_similarity(clusters, clusters_reference))
    # Return the average Jaccard similarity
    return np.mean(jaccard_scores)


def outsample_stability(n, p, weight_mean, weight_stddev, capacity_mean, capacity_stddev, lambda_param, num_runs=10):
    rand_index_scores = []

    for i in range(num_runs):
        # Generate instances of nodes and capacities
        nodes, capacities = generate_instances(n, p, capacity_mean, capacity_stddev)
        # Generate weights for each node
        weights = generate_weights(n, weight_mean, weight_stddev)
        # Split data into training and validation sets
        nodes_train, weights_train, nodes_val, weights_val = split_data(nodes, weights)
        # Solve the clustering model on the training set
        clusters_train, _, obj_val = solve_model(nodes_train, capacities, weights_train, lambda_param, 'ccp')
        # Solve the clustering model on the validation set
        clusters_val, _, obj_val = solve_model(nodes_val, capacities, weights_val, lambda_param, 'ccp')
        # Calculate the Rand index score between the training and validation clusters
        rand_index_scores.append(rand_index(clusters_train, clusters_val))
    # Return the average Rand index score
    return np.mean(rand_index_scores)


def calculate_VSS(n, p, capacity_mean, capacity_stddev, weight_mean, weight_stddev, lambda_param, num_simulations):
    # Find the EEVS by generating multiple instances and solving the CCP for each instance
    EEVS = 0
    for i in range(num_simulations):
        nodes, capacities = generate_instances(n, p, capacity_mean, capacity_stddev)
        weights = generate_weights(n, weight_mean, weight_stddev)

        clusters, _, obj_val = solve_model(nodes, capacities, weights, lambda_param, 'ccp')
        EEVS += obj_val

    EEVS = EEVS / num_simulations

    # Generate 2D nodes and random capacities for clusters
    nodes, capacities = generate_instances(n, p, capacity_mean, capacity_stddev)
    # Generate random weight for each node
    weights = generate_weights(n, weight_mean, weight_stddev)

    clusters, _, RP = solve_model(nodes, capacities, weights, lambda_param, 'RP')

    print('RP:', RP)

    print('EEVS:', EEVS)

    # Calculate the VSS
    VSS = EEVS - RP

    return VSS
