import matplotlib.pyplot as plt
import random

def get_cluster_nodes(clusters, nodes):
    cluster_nodes = []
    for cluster in clusters:
        cluster_node_values = [nodes[index] for index in cluster]
        cluster_nodes.append(cluster_node_values)
    return cluster_nodes


def plot_clusters(clusters, nodes):
    def random_color():
        return [random.random() for _ in range(3)]

    clusters = get_cluster_nodes(clusters, nodes)

    colors = [random_color() for _ in range(len(clusters))]
    for i, cluster in enumerate(clusters):
        x = [point[0] for point in cluster]
        y = [point[1] for point in cluster]
        plt.scatter(x, y, c=[colors[i]])

    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()

