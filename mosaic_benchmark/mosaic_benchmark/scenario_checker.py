"""Checking the scenario based on the limits"""
from mosaic_benchmark.mosaic_community import Mosaic


def check_nodes_validity(nodes: list[int], number_of_nodes: int) -> bool:
    """
    Check if all node indices are within the valid range.

    Args:
        nodes (list[int]): List of node indices to be checked.
        number_of_nodes (int): The upper bound of the valid index range.

    Returns:
        bool: True if all node indices are within the range, False otherwise.
    """

    # Iterate through each node index and use the all() function to ensure
    # that all indices are within the valid range [0, number_of_nodes].
    # If any index is outside this range, the all() function will return False.
    # Otherwise, it will return True.
    return all(0 <= node_index <= number_of_nodes for node_index in nodes)


def check_time_validity(
    t_start_community: float,
    t_end_community: float,
    t_start_linkstream: float,
    t_end_linkstream: float,
) -> bool:
    """
    Check if a community time interval is fully contained within a linkstream time interval.

    Args:
        t_start_community (float): The start time of the community interval.
        t_end_community (float): The end time of the community interval.
        t_start_linkstream (float): The start time of the linkstream interval.
        t_end_linkstream (float): The end time of the linkstream interval.

    Returns:
        bool: True if the community interval is fully contained within the linkstream interval, False otherwise.
    """
    # Return True if the community interval is fully contained within the linkstream interval
    # This is the case if both the start and end times of the community interval are within the linkstream interval.
    return (
        t_start_community >= t_start_linkstream and t_end_community <= t_end_linkstream
    )


def check_overlapping_communities(mosaic1: Mosaic, mosaic2: Mosaic) -> bool:
    """
    Check if two mosaics (community structures) overlap in time and nodes.

    Args:
        mosaic1 (Mosaic): The first mosaic to be compared.
        mosaic2 (Mosaic): The second mosaic to be compared.

    Returns:
        bool: True if there is an overlap, False otherwise.
    """
    # Check if the time intervals of the mosaics overlap
    if max(mosaic1.t_start, mosaic2.t_start) < min(mosaic1.t_end, mosaic2.t_end):
        # Check if any nodes from mosaic1 are also present in mosaic2
        return any(node in mosaic2.nodes for node in mosaic1.nodes)
    return False


def check_overlapping_scenario(
    existing_communities: dict[str, Mosaic], mosaic_to_add: Mosaic
) -> bool:
    """
    Checks for overlapping scenarios between the given 'mosaic_to_add' and existing community mosaics.

    This function iterates through each existing community's mosaic and compares it with the provided 'mosaic_to_add'
    to determine if there are any overlapping scenarios.

    Args:
        existing_communities (dict[str, Mosaic]): A dictionary containing existing community mosaics, where keys are
                                                  community names and values are corresponding mosaic instances.
        mosaic_to_add (Mosaic): The mosaic representing the scenario to be checked for overlapping.

    Returns:
        bool: True if no overlapping scenarios are found, False otherwise.
    """
    # Iterate through each existing community's mosaic and check for overlapping scenarios with 'mosaic_to_add'.
    # Returns True only if any existing community scenarios do overlap with the provided mosaic.
    return any(
        check_overlapping_communities(comm, mosaic_to_add)
        for comm in existing_communities.values()
    )
