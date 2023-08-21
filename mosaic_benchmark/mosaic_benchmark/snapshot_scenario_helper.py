"""Helper for snapshot scenario generation"""
def divide_interval(t_start: float, t_end: float, number_of_slices: int) -> list[tuple[float, float]]:
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

    Example:
        divide_interval(0.0, 10.0, 5) returns [(0.0, 2.0), (2.0, 4.0), (4.0, 6.0), (6.0, 8.0), (8.0, 10.0)]
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
