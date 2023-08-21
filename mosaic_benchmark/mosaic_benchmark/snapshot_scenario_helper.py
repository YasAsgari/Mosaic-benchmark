"""Helper for snapshot scenario generation"""
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
