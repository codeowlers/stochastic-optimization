import matplotlib.pyplot as plt
import random


def get_cluster_nodes(clusters, nodes):
    cluster_nodes = []
    # Iterate over clusters
    for cluster in clusters:
        # Get values of nodes in the current cluster
        cluster_node_values = [nodes[index] for index in cluster]
        # Append the values to the list of cluster nodes
        cluster_nodes.append(cluster_node_values)
    return cluster_nodes


def plot_clusters(clusters, nodes, title):
    # Define a function to generate a random color
    def random_color():
        return [random.random() for _ in range(3)]
    # Get cluster nodes
    clusters = get_cluster_nodes(clusters, nodes)
    # Generate random colors for each cluster
    colors = [random_color() for _ in range(len(clusters))]
    # Iterate over the clusters
    for i, cluster in enumerate(clusters):
        # Get x-coordinates of nodes in the current cluster
        x = [point[0] for point in cluster]
        # Get y-coordinates of nodes in the current cluster
        y = [point[1] for point in cluster]
        # Plot the nodes using the current color
        plt.scatter(x, y, c=[colors[i]])
    # Set the title of the plot
    plt.title(title)
    # Show the plot
    plt.show()
