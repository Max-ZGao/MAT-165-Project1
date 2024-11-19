from ConvexHull import ConvexHull

class CrossingFreePartition:

    # partition is an array of np.array of points of dimension n
    def __init__(self, partition):

        self.dimension = 0
        self.is_valid = False # if this is a valid partition
        self.convexhulls = []

        for arr in partition:
            
            for point in arr:
                if self.dimension == 0:
                    self.dimension = point.dimension
                assert(self.dimension == point.dimension)
                assert(self.dimension > 0)


            new_convexhull = ConvexHull(arr)
            
            for convexhull in self.convexhulls:
                if new_convexhull.is_intersecting(convexhull) == True:
                    return


        self.is_valid = True


    def is_distance_1_from(self, crossing_partition):
        
        return
            
            