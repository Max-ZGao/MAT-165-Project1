from ConvexHull import ConvexHull
import numpy as np

class CrossingFreePartition:

    # partition is an array of np.array of points of dimension n
    def __init__(self, partition):

        self.dimension = 0
        self.is_valid = False # if this is a valid partition
        self.convexhulls = []
        self.partition = partition

        for arr in partition:
            
            for point in arr:
                if self.dimension == 0:
                    self.dimension = len(point)
                assert self.dimension == len(point)
                assert(self.dimension > 0)
            
            new_convexhull = ConvexHull(np.array(arr))

            for hull in self.convexhulls:
                if hull.get_intersection(new_convexhull) != None:
                    return 

            self.convexhulls.append(new_convexhull)
        
        self.is_valid = True
            

    
    def is_equal(self, partition):
        if len(partition.convexhulls) != len(self.convexhulls):
            return False

