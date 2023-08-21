"""Module for generating edges"""
# Import necessary functions and classes from modules
from mosaic_benchmark.edge_generation_helper import (
    create_stable_backbone_outside,
    simulate_poisson_process,
    create_stable_backbone_inside,
)
from mosaic_benchmark.mosaic_community import Mosaic


# Define a function to find the intersection time interval between two mosaics
def time_intersection(mosaic1: Mosaic, mosaic2: Mosaic):
    """
    Finds the time interval of intersection between two mosaics.

    Args:
        mosaic1 (Mosaic): First mosaic community.
        mosaic2 (Mosaic): Second mosaic community.

    Returns:
        tuple: A tuple containing start and end times of the intersection.
    """
    # If there's no overlap between the mosaics' time intervals, return (0, 0)
    if mosaic1.t_end <= mosaic2.t_start or mosaic2.t_end <= mosaic1.t_start:
        return 0, 0
    else:
        # Determine the overlapping time interval
        start = max(mosaic2.t_start, mosaic1.t_start)
        end = min(mosaic1.t_end, mosaic2.t_end)
        return start, end


# Define a function for generating temporal edges between communities across mosaics
def outside_temporal_edges(
    mosaic1: Mosaic, mosaic2: Mosaic, alpha: float, beta: float, lambda_out: float
):
    """
    Generates temporal edges connecting communities across two mosaics
    Args:
        mosaic1 (Mosaic): First mosaic community.
        mosaic2 (Mosaic): Second mosaic community.
        alpha (float): Parameter influencing the edge generation.
        beta (float): Parameter influencing the edge generation.
        lambda_out (float): Intensity parameter for Poisson process.

    Returns:
        list: A list of tuples representing generated temporal edges (u, v, t).
    """
    stream = []
    # Find the intersection time interval between the two mosaics
    start, end = time_intersection(mosaic1, mosaic2)
    # Generate edges if there is a non-zero intersection interval
    if end != start:
        edges = create_stable_backbone_outside(
            mosaic1.nodes, mosaic2.nodes, alpha, beta
        )
        # Generate temporal edges using Poisson process and extend the edge stream
        stream = [
            (u, v, t)
            for (u, v) in edges
            for t in simulate_poisson_process(lambda_out, start, end)
        ]
    return stream


# Define a function for generating temporal edges within a mosaic community
def inside_temporal_edges(mosaic: Mosaic, alpha: float, lambda_in: float):
    """
    Generates temporal edges within a given mosaic community.

    Args:
        mosaic (Mosaic): A mosaic community.
        alpha (float): Parameter influencing the edge generation.
        lambda_in (float): Intensity parameter for Poisson process.

    Returns:
        list: A list of tuples representing generated temporal edges (u, v, t).
    """
    # Generate stable backbone edges within the community
    edges = create_stable_backbone_inside(mosaic.nodes, alpha)
    # Generate temporal edges using Poisson process and extend the edge stream
    stream = [
        (u, v, t)
        for (u, v) in edges
        for t in simulate_poisson_process(lambda_in, mosaic.t_start, mosaic.t_end)
    ]
    return stream
