import numpy as np
from Surface import Surface

class ConvexHull:


    # points is a np array of size (p, n)
    # p is the number of points
    # n is the dimensions
    def __init__(self, points):

        _, self.dimension = points.shape

        # TO DO
        
        self.surfaces = []
        self.points = points
        return


    # checks if a point is contained in the convex hull
    def contains_point(self, point):

        assert(self.dimension == point.dimension, "ConvexHull and Point needs to be the same dimension")

        # TO DO
        
        return False
    
    
    def is_intersecting(self, convexhull):
        
        for point in convexhull.points:
            if self.contains_point(point):
                return True

        for point in self.points:
            if convexhull.contains_point(point):
                return True

        for surface1 in convexhull.surfaces:
            for surface2 in self.surfaces:
                if surface1.is_intersecting(surface2):
                    return True

        return False
        
