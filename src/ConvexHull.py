import numpy as np
from Surface import Surface

class ConvexHull:


    # points is a np array of size (p, n)
    # p is the number of points
    # n is the dimensions
    def __init__(self, points):

        _, self.dimension = points.shape

        self.surfaces = []
        self.points = points

        if len(points) < self.dimension:
            self.surfaces = [Surface(points)]

        joint_surfaces = []
        if self.dimension == 2:
            for x in range(len(points)):
                for y in range(x):
                    joint_surfaces.append(Surface(np.array([points[x], points[y]])))
        elif self.dimension == 3:
            for x in range(len(points)):
                for y in range(x):
                    for z in range(y):
                        joint_surfaces.append(Surface(np.array([points[x], points[y], points[z]])))

        for surface1 in joint_surfaces:

            intersect = False
            
            for surface2 in joint_surfaces:
                
                share_point = False
                for p1 in surface1.points:
                    for p2 in surface2.points:
                        if np.array_equal(p1, p2):
                            share_point = True

                if share_point == True:
                    continue

                if surface1.is_intersecting(surface2):
                    intersect = True
                    break
            
            if intersect == False:
                self.surfaces.append(surface1)
                
        return


    # checks if a point is contained in the convex hull
    def contains_point(self, point):

        assert self.dimension == len(point)


        max_loc = 1e10
        random_point = np.random.uniform(-max_loc, max_loc, size=(self.dimension))
        line = Surface(np.array([point, random_point]))
        
        count = 0
        for s in self.surfaces:
            if s.is_intersecting(line):
                count += 1
        return (count%2)==1
        

    def get_intersection(self, convexhull):

        points = []
        if len(self.points) > self.dimension:
            for p in convexhull.points:
                if self.contains_point(p):
                    points.append(p)

        if len(convexhull.points) > convexhull.dimension:
            for p in self.points:
                if convexhull.contains_point(p):
                    points.append(p)

        for surface1 in convexhull.surfaces:
            for surface2 in self.surfaces:
                intersection = surface1.get_intersection(surface2)
                for p in intersection:
                    points.append(p)
                    

        if len(points) == 0:
            return None
            
        return ConvexHull(np.array(points))
