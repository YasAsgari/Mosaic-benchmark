"""KOFT"""
import random
from mosaic_benchmark.mosaic_community import Mosaic
class Grid:
    def __init__(self, x1, x2, y1, y2):
        assert x2 > x1 and y2 > y1
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.subgrids = []

    def random(self):
        if not self.subgrids:
            x = self.x1 + int(random.random()* (self.x2 - self.x1))
            y = self.y1 +int(random.random() * (self.y2 - self.y1))
            four = [
                    (self.x1, x, self.y1, y),
                    (x, self.x2, self.y1, y),
                    (self.x1, x, y, self.y2),
                    (x, self.x2, y, self.y2)
                ]
            for a, b, c, d in four:
                if a != b and c != d:
                    subgrid = Grid(a, b, c, d)
                    self.subgrids.append(subgrid)
        else:
            random.choice(self.subgrids).random()

    def flatten(self):
        if not self.subgrids:
            return
        result = []
        for subgrid in self.subgrids:
            if not subgrid.subgrids:
                result.append((subgrid.x1, subgrid.x2, subgrid.y1, subgrid.y2))
            else:
                result.extend(subgrid.flatten())

        return result
    
def convert_rectangle_to_Mosaic(rectangle: list[int])->Mosaic:
    pass
def random_scenario(width: float, height:int, number=24):
    grid = Grid(0, width, 0, height)
    for i in range(number): grid.random()
    rectangles = grid.flatten()
    mosaics=[convert_rectangle_to_Mosaic(rect) for rect in rectangles]
    return mosaics
