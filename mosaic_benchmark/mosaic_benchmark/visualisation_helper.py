"""Helper for visualisation"""
import random
from matplotlib.patches import Rectangle
from mosaic_benchmark.mosaic_community import Mosaic

def visualize_mosaics(t_start: float, t_end: float, number_of_nodes: int, communities: dict[str, Mosaic], axis):
    """
    Visualizes mosaic communities on the given axis using colored rectangles.

    Args:
        t_start (float): The start time of the visualization.
        t_end (float): The end time of the visualization.
        number_of_nodes (int): The total number of nodes.
        communities (dict[str, Mosaic]): A dictionary containing community names as keys
                                         and corresponding Mosaic instances as values.
        axis: The matplotlib axis to visualize the mosaics on.
    """
    # Calculate visualization parameters
    width = t_end - t_start
    height = number_of_nodes
    
    # Generate a colormap for communities
    colormap = generate_colormap(communities)
    
    # Draw background rectangle for the entire time range
    background_rect = Rectangle(
        (t_start, -0.5),
        width,
        height,
        fill=True,
        facecolor='#D3D3D3',  # Light gray
        edgecolor="black",
        lw=0,
    )
    axis.add_patch(background_rect)
    
    # Draw rectangles for each node in each mosaic community
    for comm, mosaic in communities.items():
        width = mosaic.t_end - mosaic.t_start
        height = 1
        
        for node in mosaic.nodes:
            node_rect = Rectangle(
                (mosaic.t_start, node - 0.5),
                width,
                height,
                fill=True,
                facecolor=colormap[comm],
                edgecolor="black",
                lw=0,
            )
            axis.add_patch(node_rect)
    
    # Configure visualization settings
    axis.plot([0,0], [1,1])
    axis.set_aspect("equal")  # Maintain aspect ratio for clarity
    axis.axis("off")  # Hide axis labels and ticks

def generate_random_color():
    """
    Generates a random RGB color tuple.

    Returns:
        tuple: A tuple representing an RGB color.
    """
    return tuple(random.random() for _ in range(3))

def generate_colormap(communities):
    """
    Generates a colormap for communities using random colors.

    Args:
        communities: A list of community names.

    Returns:
        dict: A dictionary mapping community names to corresponding random color tuples.
    """
    return {comm: generate_random_color() for comm in communities}
