"""Helper for snapshot scenario generation"""
import random
import numpy as np
def divide_interval_equal(t_start: float, t_end: float, number_of_slices: int) -> list[tuple[float, float]]:
    """
    Divides a given time interval into specified slices.

    Args:
        t_start (float): The start time of the interval.
        t_end (float): The end time of the interval.
        number_of_slices (int): The number of slices to divide the interval into.

    Returns:
        list[tuple[float, float]]: A list of tuples representing the divided intervals.
            Each tuple contains a start time and an end time.

    Raises:
        AssertionError: If the number of slices is not a positive integer.
    """
    # Ensure that the number of slices is a positive integer
    assert number_of_slices > 0, "Number of slices can't be zero or negative"

    # Calculate the length of the entire interval
    interval_length = t_end - t_start
    # Calculate the length of each individual slice
    slice_length = interval_length / number_of_slices
    # Initialize a list to store the resulting intervals
    intervals = []
    # Iterate through each slice and determine its start and end points
    for i in range(number_of_slices):
        start = t_start + i * slice_length
        # Calculate the end point of the current slice
        # For all but the last slice, it's the start point plus the slice length
        # For the last slice, it's the same as the overall interval's end point
        end = start + slice_length if i < number_of_slices - 1 else t_end
        # Add the interval to the list of intervals
        intervals.append((start, end))
    # Return the list of divided intervals
    return intervals
def divide_interval_varying(t_start: float, t_end: float, number_of_slices: int) -> list[tuple[float, float]]:
    """
    Divides the given interval [t_start, t_end] into subintervals using random middle points.
    
    Args:
        t_start (float): The start of the interval.
        t_end (float): The end of the interval.
        number_of_slices (int): The desired number of subintervals.

    Returns:
        list[tuple[float, float]]: A list of tuples representing the subintervals.
    """
    # Ensure that the number of slices is a positive integer
    assert number_of_slices > 0, "Number of slices can't be zero or negative"
    
    # Generate random middle points within the interval [t_start, t_end]
    middle_points = np.random.uniform(low=t_start, high=t_end, size=number_of_slices - 1).round(2)
    intervals = []
    intervals.append((t_start, middle_points[0]))  # First subinterval
    # Generate subintervals between adjacent middle points
    for start, end in zip(middle_points[:-1], middle_points[1:]):
        intervals.append((start, end))  
    intervals.append((middle_points[-1], t_end))  # Last subinterval
    return intervals

def divide_interval(t_start: float, t_end: float, number_of_slices: int, fixed: bool = True) -> list[tuple[float, float]]:
    """
    Divides the given interval [t_start, t_end] into a specified number of slices, generating sub-intervals.

    Args:
        t_start (float): The start value of the interval.
        t_end (float): The end value of the interval.
        number_of_slices (int): The desired number of sub-intervals.
        fixed (bool, optional): If True, divides the interval into equal sub-intervals using divide_interval_equal(),
                               otherwise uses divide_interval_varying(). Defaults to True.

    Returns:
        list[tuple[float, float]]: A list of tuples representing the generated sub-intervals.

    Note:
        This function delegates the division process to either divide_interval_equal() or divide_interval_varying()
        based on the 'fixed' parameter value.
    """
    if fixed:
        intervals = divide_interval_equal(t_start, t_end, number_of_slices)
    else:
        intervals = divide_interval_varying(t_start, t_end, number_of_slices)
    return intervals

def divide_nodes(number_of_nodes: int) -> list:
    """
    Generates random partitions of a range of nodes.

    Args:
        number_of_nodes (int): The total number of nodes to be partitioned.

    Returns:
        list: A list of partitions, where each partition is represented as a list of node indices.
    """

    # Ensure that the input is valid
    assert number_of_nodes > 0, "Number of nodes should be positive"
    
    # Initialize the list with the starting index of the first partition
    partition_indices = [0]

    # Generate partition indices
    while partition_indices[-1] < number_of_nodes - 1:
        if partition_indices[-1] < number_of_nodes - 3:
            # Generate a random ending index for the partition within a certain range
            last_index = random.randint(partition_indices[-1] + 2, number_of_nodes)       
            # Adjust the last index if it exceeds the total number of nodes
            if last_index > number_of_nodes - 2:
                last_index = number_of_nodes
        else:
            # For the last partition, cover the remaining nodes
            last_index = number_of_nodes 
        # Add the generated partition index to the list
        partition_indices.append(last_index)
    # Create partitions based on the generated indices
    partitions = [list(range(partition_indices[i], partition_indices[i + 1])) for i in range(len(partition_indices) - 1)]
    return partitions
