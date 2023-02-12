import gurobipy as gp
from algorithms import *
import time

def solve_model(nodes, capacities, weights, lambda_param, model_type):
    start = time.time()
    n = nodes.shape[0]
    p = len(capacities)

    # Create gurobi model
    model = gp.Model(model_type)

    # Create decision variables
    x = {}
    y = {}

    # Update decision variables as mentioned in the problem statement
    for i in range(n):
        for j in range(p):
            x[i, j] = model.addVar(vtype=gp.GRB.BINARY, name=f'x[{i},{j}]')
        y[i] = model.addVar(vtype=gp.GRB.BINARY, name=f'y[{i}]')

    # Set objective function
    obj = gp.quicksum(euclidean_distance(nodes[i], nodes[j]) * x[i,j] for i in range(n) for j in range(p))
    obj += lambda_param * gp.quicksum(capacities[j]*y[j] for j in range(p))
    obj -= lambda_param * gp.quicksum(weights[i]*x[i,j] for i in range(n) for j in range(p))
    
    model.setObjective(obj, gp.GRB.MINIMIZE)

    # Add constraints
    for i in range(n):
        model.addConstr(gp.quicksum(x[i,j] for j in range(p)) == 1, name=f'assign[{i}]')

    model.addConstr(gp.quicksum(y[j] for j in range(p)) <= p, name='num_clusters')

    for i in range(n):
        for j in range(p):
            model.addConstr(x[i,j] <= y[j], name=f'x_c[{i},{j}]')

    # Solve model
    model.optimize()
    # Extract solution
    clusters = []
    for j in range(p):
        cluster = [i for i in range(n) if x[i,j].X > 0.5]
        clusters.append(cluster)
    end = time.time()
    return clusters, end-start, model.ObjVal