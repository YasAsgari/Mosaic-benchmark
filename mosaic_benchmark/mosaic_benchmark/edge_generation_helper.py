"""Module providing Function for step generating edges"""
# Import necessary libraries
import numpy as np  # Library for numerical computations
import networkx as nx  # Library for creating and manipulating networks/graphs


def simulate_poisson_process(lmbda: float, t_start: float, t_end: float) -> list:
    """
    Simulates a Poisson process with a given arrival rate (lambda) within a specified time interval.

    :param lmbda: Arrival rate of edges (lambda) for the Poisson process.
    :param t_start: Start time of the community.
    :param t_end: End time of the community.
    :return: An array of arrival times of events generated by the Poisson process.
    """
    time_frame = t_end - t_start

    # Generate a random number of edges according to a Poisson distribution
    k = np.random.poisson(time_frame * lmbda)

    # Generate random arrival times for the events within the specified time interval
    arrival_times = np.random.uniform(t_start, t_end, k)
    # If no arrival times were generated, create a single random arrival time
    if len(arrival_times) == 0:
        arrival_times = np.array([np.random.uniform(t_start, t_end)])
    # Round the arrival times to two decimal places for cleaner output
    return list(arrival_times.round(2))


def create_stable_backbone_inside(nodes: list, alpha: float) -> list:
    """
    Create a stable backbone graph from a list of nodes using the Erdős-Rényi model.

    :param nodes: List of nodes to create the backbone from.
    :param alpha: Density coefficient in the range [0.5, 1].
    :return: List of edges representing the stable backbone graph.
    """
    assert (
        alpha >= 0.5 and alpha <= 1
    ), "Error: Correct range for alpha is between 0.5 and 1"
    v_c = len(nodes)  # Node size (refer to paper for explanation)
    p_in = (v_c - 1) ** (alpha - 1)  # Probability
    is_connected = False
    while not is_connected:
        # Generate an Erdős-Rényi graph which should be connected because of community's definition
        graph = nx.erdos_renyi_graph(v_c, p_in)
        if nx.is_connected(graph):
            is_connected = True
    graph.remove_edges_from(nx.selfloop_edges(graph))
    # Convert the graph's edges to a list of edges
    edges = [(nodes[u], nodes[v]) for (u, v) in graph.edges]
    return edges


def create_stable_backbone_outside(
    nodes1: list, nodes2: list, alpha: float, beta: float
) -> list:
    """
    Creates a stable bipartite graph backbone based on given parameters.

    Args:
        nodes1 (list): List of nodes in the first partition.
        nodes2 (list): List of nodes in the second partition.
        alpha (float): Density coefficient between 0.5 and 1.
        beta (float): Community identifiability coefficient between 0 and 1.

    Returns:
        list: List of edges in the created outside graph backbone.
    """
    # Check validity of alpha and beta values
    assert 0.5 <= alpha <= 1, "Error: Correct range for alpha is between 0.5 and 1"
    assert 0 <= beta <= 1, "Error: Correct range for beta is between 0 and 1"

    # Calculate number of nodes in each partition
    number_of_nodes1 = len(nodes1)
    number_of_nodes2 = len(nodes2)

    # creating mapping for labels
    label_mapping = {i: label for i, label in enumerate(nodes1 + nodes2)}
    # Calculate the probability of an edge between partitions
    p_out = beta * (((number_of_nodes1 + number_of_nodes2) - 1) ** (alpha - 1))

    # Generate a bipartite graph with specified parameters
    graph = nx.bipartite.random_graph(number_of_nodes1, number_of_nodes2, p_out)
    # Convert graph edges to a list of node pairs
    edge_list = [(label_mapping[u], label_mapping[v]) for u, v in graph.edges]

    return edge_list
