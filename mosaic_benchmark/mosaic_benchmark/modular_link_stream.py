"""The unifier of all codes in the library"""
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mosaic_benchmark.mosaic_community import Mosaic
from mosaic_benchmark.edge_generator import outside_temporal_edges, inside_temporal_edges
from mosaic_benchmark.visualisation_helper import visualize_mosaics


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

    def add_community(self, nodes: list, t_start: float, t_end: float):
        """
        Add a community to the link stream.

        Parameters:
        - nodes: List of nodes in the community.
        - t_start: Starting time of the community.
        - t_end: Ending time of the community.
        """
        self.number_of_communities += 1
        self.communities[f"c{self.number_of_communities}"] = Mosaic(
            nodes, t_start, t_end
        )

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
        # %%
        visualize_mosaics(self.communities, axis)
