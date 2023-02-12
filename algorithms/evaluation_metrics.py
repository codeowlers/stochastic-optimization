import numpy as np

def jaccard_similarity(clusters_1, clusters_2):
    jaccard_scores = []
    for cluster_1 in clusters_1:
        jaccard_scores_per_cluster = []
        for cluster_2 in clusters_2:
            union = len(set(cluster_1).union(cluster_2))
            intersection = len(set(cluster_1).intersection(cluster_2))
            jaccard_index = intersection / union
            jaccard_scores_per_cluster.append(jaccard_index)
        jaccard_scores.append(max(jaccard_scores_per_cluster))
    return np.mean(jaccard_scores)

def rand_index(clusters_1, clusters_2):
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    n = len(clusters_1)
    for i in range(n):
        for j in range(i+1, n):
            if (clusters_1[i] == clusters_1[j] and clusters_2[i] == clusters_2[j]):
                tp += 1
            elif (clusters_1[i] != clusters_1[j] and clusters_2[i] != clusters_2[j]):
                tn += 1
            elif (clusters_1[i] == clusters_1[j] and clusters_2[i] != clusters_2[j]):
                fp += 1
            else:
                fn += 1

    return (tp + tn) / (tp + tn + fp + fn)
