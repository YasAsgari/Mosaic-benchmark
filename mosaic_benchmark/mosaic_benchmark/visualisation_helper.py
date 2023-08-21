"""Helps to visualize the linkstream communities"""
import random
from matplotlib.patches import Rectangle
from mosaic_benchmark.mosaic_community import Mosaic


def visualize_mosaics(communities: dict[str, Mosaic], axis):
    """
    Visualize mosaic communities on the given axis using colored rectangles.

    Args:
        communities (dict[str, Mosaic]): A dictionary containing community names as keys
                                         and corresponding Mosaic instances as values.
        axis: The matplotlib axis to visualize the mosaics on.
    """
    colormap = generate_colormap(communities)

    for comm, mosaic in communities.items():
        width = mosaic.t_end - mosaic.t_start
        height = 1

        for node in mosaic.nodes:
            rect = Rectangle(
                (mosaic.t_start, node - 0.5),
                width,
                height,
                fill=True,
                facecolor=colormap[comm],
                edgecolor="black",
                lw=1,
            )
            axis.add_patch(rect)
    axis.axvline(x=0, color="black")  # Draw a vertical line at x=0
    axis.invert_yaxis()
    axis.set_aspect("equal")
    axis.axis("off")


def generate_random_color():
    """
    Generate a random RGB color tuple.

    Returns:
        tuple: A tuple representing an RGB color.
    """
    return tuple(random.random() for _ in range(3))


def generate_colormap(communities):
    """
    Generate a colormap for communities using random colors.

    Args:
        communities: A list of community names.

    Returns:
        dict: A dictionary mapping community names to corresponding random color tuples.
    """
    return {comm: generate_random_color() for comm in communities}
