"""KOFT"""
import random  # Import the 'random' module for generating random numbers.


class Grid:
    def __init__(self, x1, x2, y1, y2):
        """
        Initializes a Grid instance with specified coordinates.

        Args:
            x1 (int): The starting x-coordinate of the grid.
            x2 (int): The ending x-coordinate of the grid.
            y1 (int): The starting y-coordinate of the grid.
            y2 (int): The ending y-coordinate of the grid.

        Raises:
            AssertionError: If x2 is not greater than x1 or y2 is not greater than y1.
        """
        assert x2 > x1 and y2 > y1  # Check if the coordinates are valid.
        self.x1 = x1  # Initialize the starting x-coordinate.
        self.x2 = x2  # Initialize the ending x-coordinate.
        self.y1 = y1  # Initialize the starting y-coordinate.
        self.y2 = y2  # Initialize the ending y-coordinate.
        self.subgrids = []  # Initialize an empty list to store subgrid instances.

    def random(self):
        """
        Generates a random subgrid within the current grid's coordinates.

        If the current grid has no subgrids, it randomly divides itself into four subgrids,
        each with different coordinates.
        If subgrids already exist, selects a random subgrid and recursively generates a random
        subgrid within that subgrid.
        """
        if not self.subgrids:  # If there are no existing subgrids.
            x = self.x1 + round(
                random.random() * (self.x2 - self.x1), 2
            )  # Generate a random x-coordinate.
            y = self.y1 + int(
                random.random() * (self.y2 - self.y1)
            )  # Generate a random y-coordinate.
            four = [
                (self.x1, x, self.y1, y),
                (x, self.x2, self.y1, y),
                (self.x1, x, y, self.y2),
                (x, self.x2, y, self.y2),
            ]  # Define four different sets of coordinates for subgrids.
            for a, b, c, d in four:
                if a != b and c != d:
                    subgrid = Grid(a, b, c, d)  # Create a new subgrid instance.
                    self.subgrids.append(
                        subgrid
                    )  # Add the subgrid to the list of subgrids.
        else:  # If subgrids already exist.
            random.choice(
                self.subgrids
            ).random()  # Choose a random subgrid and generate a random subgrid within it.

    def flatten(self):
        """
        Returns a flattened list of subgrid coordinates.

        If the current grid has no subgrids, returns an empty list.
        If subgrids exist, recursively flattens them and returns a list of tuples representing
        their coordinates.

        Returns:
            list: A list of tuples representing subgrid coordinates.
        """
        if not self.subgrids:  # If there are no existing subgrids.
            return []  # Return an empty list.

        result = []  # Initialize an empty list to store flattened subgrid coordinates.
        for subgrid in self.subgrids:  # For each subgrid instance.
            if not subgrid.subgrids:  # If the subgrid has no subgrids of its own.
                result.append(
                    (subgrid.x1, subgrid.x2, subgrid.y1, subgrid.y2)
                )  # Append its coordinates to the result list.
            else:  # If the subgrid has its own subgrids.
                result.extend(
                    subgrid.flatten()
                )  # Recursively flatten its subgrids and extend the result list.

        return result  # Return the flattened subgrid coordinates.


def random_scenario(
    number_of_nodes: int, t_start: float, t_end: float, approx_order_of_communities: int
) -> list[list]:
    """
    Generate a random scenario of communities over time and space.

    Args:
        number_of_nodes (int): Total number of nodes.
        t_start (float): Start time of the scenario.
        t_end (float): End time of the scenario.
        approx_order_of_communities (int): Approximate number of communities to generate.

    Returns:
        List of communities_to_add, where each community is represented as [nodes, t_start_comm, t_end_comm].
    """
    width = t_end - t_start
    height = number_of_nodes

    # Create a grid and generate random communities
    grid = Grid(0, width, 0, height)
    for _ in range(approx_order_of_communities):
        grid.random()

    rectangles = grid.flatten()
    communities_to_add = []

    for comm in rectangles:
        t_start_comm, t_end_comm, v_start_comm, v_end_comm = comm
        if v_end_comm >= v_start_comm + 2:
            nodes = list(range(int(v_start_comm), int(v_end_comm)))
            communities_to_add.append([nodes, t_start_comm, t_end_comm])

    return communities_to_add
