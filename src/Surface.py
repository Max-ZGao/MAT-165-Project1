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
                # add module to prevent index out of range
                if do_intersect(self.points[i], self.points[(i + 1) % self.num_points],
                                surface.points[j], surface.points[(j + 1) % surface.num_points]):
                    return True
        return False

    def get_intersection(self, surface):
        if not self.is_intersecting(surface):
            return []

        if surface.num_points == 1:
            return [surface.points[0]]
        if self.num_points == 1:
            return [self.points[0]]
        
        x1, y1 = self.points[0][0], self.points[0][1]
        x2, y2 = self.points[1][0], self.points[1][1]
        x3, y3 = surface.points[0][0], surface.points[0][1]
        x4, y4 = surface.points[1][0], surface.points[1][1]
    
        # Calculate the determinants
        det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        
        # If det is zero, the lines are parallel
        if det == 0:
            return None
    
        # Calculate intersection point
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det
    
        return np.array([[px, py]])


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

# check if two line segment intersect.
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
