import numpy as np


# Split data into training and test sets
def split_data(nodes, weights, train_ratio=0.7):
    """
    Splits data into training and validation sets.

    Parameters:
        nodes (np.ndarray): Array of nodes to split.
        weights (np.ndarray): Array of weights to split.
        train_ratio (float, optional): Ratio of training data to total data. Defaults to 0.7.

    Returns:
        tuple: A tuple containing training nodes, training weights, validation nodes, validation weights.
    """
    n = nodes.shape[0]
    indices = np.arange(n)
    np.random.shuffle(indices)
    train_indices = indices[:int(n * train_ratio)]
    val_indices = indices[int(n * train_ratio):]
    return nodes[train_indices], weights[train_indices], nodes[val_indices], weights[val_indices]
