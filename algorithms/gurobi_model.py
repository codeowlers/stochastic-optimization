import gurobipy as gp
from algorithms import *
import time


def solve_model(nodes, capacities, weights, lambda_param, model_type):
    # The function starts by importing the time module and initializing the start time
    start = time.time()
    # Get the number of nodes and clusters
    n = nodes.shape[0]
    p = len(capacities)

    # Create a Gurobi model of the specified type
    model = gp.Model(model_type)

    # Create the decision variables for each node-cluster assignment and each cluster activation
    x = {}
    y = {}

    # Update the values of the decision variables as per the problem statement
    for i in range(n):
        for j in range(p):
            x[i, j] = model.addVar(vtype=gp.GRB.BINARY, name=f'x[{i},{j}]')
        y[i] = model.addVar(vtype=gp.GRB.BINARY, name=f'y[{i}]')

    # Set the objective function to minimize the sum of euclidean distances between nodes and clusters
    # plus the lambda parameter multiplied by the sum of capacities of activated clusters
    # minus the lambda parameter multiplied by the sum of weights of nodes assigned to clusters
    obj = gp.quicksum(euclidean_distance(nodes[i], nodes[j]) * x[i, j] for i in range(n) for j in range(p))
    obj += lambda_param * gp.quicksum(capacities[j] * y[j] for j in range(p))
    obj -= lambda_param * gp.quicksum(weights[i] * x[i, j] for i in range(n) for j in range(p))

    model.setObjective(obj, gp.GRB.MINIMIZE)

    # Add constraints to enforce that each node is assigned to exactly one cluster
    for i in range(n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(p)) == 1, name=f'assign[{i}]')
    # Add constraint to enforce a limit on the number of activated clusters
    model.addConstr(gp.quicksum(y[j] for j in range(p)) <= p, name='num_clusters')
    # Add constraints to enforce that a node can only be assigned to an activated cluster
    for i in range(n):
        for j in range(p):
            model.addConstr(x[i, j] <= y[j], name=f'x_c[{i},{j}]')

    # Solve model
    model.optimize()
    # Extract solution
    clusters = []
    for j in range(p):
        cluster = [i for i in range(n) if x[i, j].X > 0.5]
        clusters.append(cluster)
    end = time.time()
    return clusters, end - start, model.ObjVal
