import numpy as np

class Surface:


    # points is a numpy array of dimension (n, n)
    def __init__(self, points):

        a, b = points.shape
        assert(a == b, "A surface needs n points of n dimension. Input needs to be size n x n")
        assert(a == 2, "Only dimension 2 is implemented currently")
        
        self.dimension = a
        self.points = points


    def is_intersecting(self, surface):

        # TO DO
        return False


