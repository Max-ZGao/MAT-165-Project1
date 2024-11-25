import numpy as np

class Surface:


    # points is a numpy array of dimension (n, n)
    def __init__(self, points):

        a, b = points.shape
        
        #assert(b <= a, "A surface needs <=n points of n dimension")
        #assert(b <= 2, "Only dimension 2 is implemented currently")
        
        self.num_points = a
        self.dimention = b
        self.points = points


    def is_intersecting(self, surface):
        for i in range(self.num_points):
            for j in range(surface.num_points):
                if do_intersect(self.points[i], self.points[(i + 1) % self.num_points],
                                surface.points[j], surface.points[(j + 1) % surface.num_points]):
                    return True
        return False


#helper function 
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    return 1 if val > 0 else 2  # clock or counterclock wise

def on_segment(p, q, r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

# check if two line intersect.
def do_intersect(point1_start, point1_end, point2_start, point2_end):
    o1 = orientation(point1_start, point1_end, point2_start)
    o2 = orientation(point1_start, point1_end, point2_end)
    o3 = orientation(point2_start, point2_end, point1_start)
    o4 = orientation(point2_start, point2_end, point1_end)

    if o1 != o2 and o3 != o4:
        return True

    # if collinear
    if o1 == 0 and on_segment(point1_start, point2_start, point1_end):
        return True
    if o2 == 0 and on_segment(point1_start, point2_end, point1_end):
        return True
    if o3 == 0 and on_segment(point2_start, point1_start, point2_end):
        return True
    if o4 == 0 and on_segment(point2_start, point1_end, point2_end):
        return True

    return False
