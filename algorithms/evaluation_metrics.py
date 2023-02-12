import numpy as np


# Calculate the jaccard similarity between two sets of clusters
def jaccard_similarity(clusters_1, clusters_2):
    jaccard_scores = []
    # Loop through each cluster in clusters_1
    for cluster_1 in clusters_1:
        # Check if cluster 1 is empty to avoid errors
        if len(cluster_1) == 0:
            continue
        # Create a list to store jaccard scores for each cluster in clusters_2 for each cluster in clusters_1
        jaccard_scores_per_cluster = []
        # Loop through each cluster in clusters_2
        for cluster_2 in clusters_2:
            # Check if cluster 2 is empty to avoid errors
            if len(cluster_2) == 0:
                continue
            # Calculate the union and intersection between the two clusters
            union = len(set(cluster_1).union(cluster_2))
            intersection = len(set(cluster_1).intersection(cluster_2))
            # Calculate the jaccard index as the intersection divided by the union
            jaccard_index = intersection / union
            # Append the jaccard index to jaccard_scores_per_cluster
            jaccard_scores_per_cluster.append(jaccard_index)
        # Append the maximum jaccard index between the current cluster in clusters_1 and all clusters in clusters_2
        jaccard_scores.append(max(jaccard_scores_per_cluster))
    # Return the mean of all jaccard scores
    return np.mean(jaccard_scores)


# Calculate the Rand Index between two sets of clusters
def rand_index(clusters_1, clusters_2):
    # Initialize variables to keep track of True Positives (tp),
    # True Negatives (tn), False Positives (fp), and False Negatives (fn)
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    # Get the number of data points in the sets of clusters
    n = len(clusters_1)
    for i in range(n):
        for j in range(i + 1, n):
            # If both data points are in the same cluster in both sets of clusters, increment tp
            if clusters_1[i] == clusters_1[j] and clusters_2[i] == clusters_2[j]:
                tp += 1
            # If both data points are in different clusters in both sets of clusters, increment tn
            elif clusters_1[i] != clusters_1[j] and clusters_2[i] != clusters_2[j]:
                tn += 1
            # If the data points are in the same cluster in one set of clusters and different clusters in the other,
            # increment fp
            elif clusters_1[i] == clusters_1[j] and clusters_2[i] != clusters_2[j]:
                fp += 1
            # If the data points are in different clusters in one set of clusters and the same cluster in the other,
            # increment fn
            else:
                fn += 1
    # Return the Rand Index as the ratio of the number of True Positives and
    # True Negatives to the total number of data point pairs
    return (tp + tn) / (tp + tn + fp + fn)
