"""Class helping to make each community"""
class Mosaic:
    """
    Represents a mosaic with a collection of nodes and a specified time range.

    Attributes:
        nodes (list): A list containing nodes that belong to the mosaic.
        t_start (float): The starting time of the mosaic.
        t_end (float): The ending time of the mosaic.
    """

    def __init__(self, nodes: list, t_start: float, t_end: float) -> None:
        """
        Initializes a Mosaic instance with the provided nodes and time range.

        Args:
            nodes (list): A list of nodes to be included in the mosaic.
            t_start (float): The starting time of the mosaic.
            t_end (float): The ending time of the mosaic.
        """
        assert t_end>t_start, 'Ending time should be greater than starting time'
        assert len(nodes)>0, 'Mosaic can not be empty'
        assert t_start>=0, 'starting time should be positive'
        self.nodes = nodes
        self.t_start = t_start
        self.t_end = t_end

    def __repr__(self):
        return f'Nodes: {str(self.nodes)} Time:({self.t_start},{self.t_end})'
    def __call__(self):
        return f'Nodes: {str(self.nodes)} Time:({self.t_start},{self.t_end})'
        