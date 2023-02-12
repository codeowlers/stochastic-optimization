import numpy as np
# Split data into training and test sets
def split_data(nodes, weights, train_ratio=0.7):
    n = nodes.shape[0]
    indices = np.arange(n)
    np.random.shuffle(indices)
    train_indices = indices[:int(n * train_ratio)]
    val_indices = indices[int(n * train_ratio):]
    return nodes[train_indices], weights[train_indices], nodes[val_indices], weights[val_indices]
