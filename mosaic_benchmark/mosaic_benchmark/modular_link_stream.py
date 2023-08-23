"""The unifier of all codes in the library"""
import itertools
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mosaic_benchmark.mosaic_community import Mosaic
from mosaic_benchmark.edge_generator import outside_temporal_edges, inside_temporal_edges
from mosaic_benchmark.visualisation_helper import visualize_mosaics
from mosaic_benchmark.scenario_checker import (check_nodes_validity, 
                                                 check_time_validity,
                                                 check_overlapping_scenario)
from mosaic_benchmark.snapshot_scenario_helper import divide_interval, divide_nodes
from mosaic_benchmark.random_scenario_helper import random_scenario
# Define a class for managing a modular link stream
class ModularLinkStream:
    """Class to create the linkstream"""

    def __init__(self, number_of_nodes: int, t_start: float, t_end: float):
        """
        Initialize the ModularLinkStream class.

        Parameters:
        - number_of_nodes: Total number of nodes in the network.
        - t_start: Starting time of the link stream.
        - t_end: Ending time of the link stream.
        """
        # Validate input parameters
        assert t_start >= 0, "Starting time should be non-negative"
        assert t_end > t_start, "Ending time should be greater than starting time"

        # Initialize attributes
        self.t_start = t_start
        self.t_end = t_end
        self.number_of_nodes = number_of_nodes
        self.number_of_communities = 0
        self.communities = {}
        self.temporal_edges = []
        self.nodes=list(range(self.number_of_nodes))

    def add_community(self, nodes: list, t_start: float, t_end: float):
        """
        Add a community to the link stream.

        Parameters:
        - nodes: List of nodes in the community.
        - t_start: Starting time of the community.
        - t_end: Ending time of the community.
        """
        # Create a new Mosaic object representing the community to be added
        new_mosaic = Mosaic(nodes, t_start, t_end)
        # Check if the provided nodes are within the valid range of node IDs
        if not check_nodes_validity(nodes, self.number_of_nodes):
            raise ValueError("Nodes are not in range")        
        # Check if the provided time range is within the valid overall time range
        if not check_time_validity(t_start, t_end, self.t_start, self.t_end):
            raise ValueError("Time is not in range")
        # Check if the new community overlaps with existing communities
        if check_overlapping_scenario(self.communities, new_mosaic):
            raise ValueError('Communities are overlapping; cannot add')
        # Increment the count of communities and add the new community to the dictionary
        self.number_of_communities += 1
        self.communities[f"c{self.number_of_communities}"] = new_mosaic

    def remove_community(self, label: str):
        """
        Remove a community from the link stream.

        Parameters:
        - label: Label of the community to be removed.
        """
        if label in self.communities:
            self.number_of_communities -= 1
            self.communities.pop(label, None)
        else:
            raise ValueError("Label is not present")

    def generate_edges(
        self, alpha: float, beta: float, lambda_in: float, lambda_out: float
    ):
        """
        Generate temporal edges between communities and within communities.

        Parameters:
        - alpha: Parameter for edge generation.
        - beta: Parameter for edge generation.
        - lambda_in: Parameter for internal edge generation.
        - lambda_out: Parameter for external edge generation.
        """
        self.temporal_edges.clear()

        # Generate edges between different communities
        for mosaic1, mosaic2 in itertools.combinations(self.communities.values(), 2):
            self.temporal_edges.extend(
                outside_temporal_edges(mosaic1, mosaic2, alpha, beta, lambda_out)
            )

        # Generate edges within each community
        for mosaic in self.communities.values():
            self.temporal_edges.extend(inside_temporal_edges(mosaic, alpha, lambda_in))

    def clear_edges(self):
        """Clear the list of temporal edges."""
        self.temporal_edges.clear()

    def export(self, address: str):
        """
        Export the link stream data to files.

        Parameters:
        - address: Address for exporting data.
        """
        # Convert temporal edges to DataFrame and export as CSV
        edge_stream_dataframe = pd.DataFrame(
            self.temporal_edges, columns=["node1", "node2", "time"]
        )
        edge_stream_dataframe.to_csv(address + "-edges.csv", index=False)

        # Export communities as a NumPy array
        np.save(address + "-communities.npy", self.communities)

    def plot(self, axis=None):
        """
        Plot the communities using a visualization helper.

        Parameters:
        - ax: Axes object for plotting (optional).
        """
        if axis is None:
            _, axis = plt.subplots(nrows=1, ncols=1, figsize=(8, 6), dpi=200)
        visualize_mosaics(self.t_start, self.t_end, self.number_of_nodes,self.communities, axis)

    def empty_mosaics(self, gamma: float):
        """
        Empties communities in M with a given probability gamma.

        Args:
            gamma (float): Probability of emptying a community (0 <= gamma <= 1).

        Raises:
            AssertionError: If gamma is not within the valid range [0, 1].

        Returns:
            None
        """
        assert 0 <= gamma <= 1, "Gamma must be a probability in the range [0, 1]."

        communities_to_remove = []

        for comm in self.communities:
            if random.random() < gamma:
                communities_to_remove.append(comm)

        for comm in communities_to_remove:
            self.communities.pop(comm, None)
            print(f'Community {comm} has been emptied!')

    def clear_communities(self):
        """
        Clears all communities in the object and resets the community count.

        Args:
            self: The instance of the object.

        Returns:
            None
        """
        self.communities.clear()             # Clear the communities dictionary
        self.number_of_communities = 0    # Reset the count of communities

    def rewiring_noise(self, eta: float):
        """
        Rewire temporal edges in the network with a given probability.

        Args:
            eta (float): The probability of rewiring an edge, within the range [0, 1].

        Returns:
            None
        """
        # Validate the range of eta
        assert 0 <= eta <= 1, "Eta must be a probability in the range [0, 1]."
        # Determine indices of edges to be rewired based on eta
        selected = np.where(np.random.uniform(size=len(self.temporal_edges)) <= eta)[0]
        # Iterate through selected edges and apply rewiring
        for i in selected:
            # Generate a new time for the rewired edge
            new_time = np.random.uniform(self.t_start, self.t_end)
            # Generate distinct nodes for rewiring
            random_edge = tuple(random.sample(self.nodes, 2))
            while random_edge[0] == random_edge[1]:
                random_edge = tuple(random.sample(self.nodes, 2))
            # Assign nodes for rewiring
            node1, node2 = random_edge
            # Apply rewiring by updating temporal_edges
            self.temporal_edges[i] = [node1, node2, new_time]
        # Print the number of edges rewired
        print(f'{len(selected)} edges rewired!')   
    def random_scenario(self,approx_order_of_communities:int):
        """
        Generate random scenarios for community partitions and add them to the instance.
        This method generates partitions of communities based on a specified time range,
        and adds each community with its associated nodes and time range to the instance.

        Args:
            approx_order_of_communities: it gives an approximate number of communities

        Returns:
            None
        """
        partitions = random_scenario(self.number_of_nodes, self.t_start, self.t_end, approx_order_of_communities)  # Generate random community partitions
        for community in partitions:
            nodes, start, end = community
            self.add_community(nodes, start, end)  # Add each community to the instance
        print(f'{len(partitions)} communities added!')
    def snap_shot_scenario(self, number_of_slices: int, fixed: bool = True):
        """
        Generate a scenario by partitioning time intervals and nodes into communities.
        Args:
            number_of_slices (int): The number of time intervals to divide the scenario into.
            fixed (bool, optional): If True, evenly divides time intervals; if False, varies interval length. Default is True.
        Returns:
            None
        """
        # Divide time interval based on specified number of slices and fixed interval option
        intervals = divide_interval(self.t_start, self.t_end, number_of_slices, fixed)
        # Iterate over generated time intervals
        for (start, end) in intervals:
            # Divide available nodes into partitions
            partitions = divide_nodes(self.number_of_nodes)
            # Iterate over node partitions
            for nodes in partitions:
                # Add a community using the partitioned nodes, within the current time interval
                self.add_community(nodes, start, end)
