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
            self.convexhulls.append(new_convexhull)

        self.is_valid = True


    def is_distance_1_from(self, crossing_partition):
        for convexhull1 in self.convexhulls:
            for convexhull2 in crossing_partition.convexhulls:
                if self.are_convexhulls_distance_1(convexhull1, convexhull2):
                    return True
        return False
            
    def are_convexhulls_distance_1(self, convexhull1, convexhull2):
        for point1 in convexhull1.points:
            for point2 in convexhull2.points:
                distance = np.linalg.norm(point1 - point2)  # 计算两点之间的欧几里得距离
                if distance == 1:
                    return True
        return False
            