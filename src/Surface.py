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
        if self.dimention == 2 or surface.dimention == 2:

            for i in range(self.num_points):
                for j in range(surface.num_points):
                    # add module to prevent index out of range
                    if do_intersect(self.points[i], self.points[(i + 1) % self.num_points],
                                    surface.points[j], surface.points[(j + 1) % surface.num_points]):
                        return True
            return False
        else:
            return self.is_intersecting_3d(surface)   

    def is_intersecting_3d(self, surface):
    
        # if point 
        if self.num_points == 1 or surface.num_points == 1:
            return self._point_intersection_3d(surface)

        # if line
        if self.num_points == 2 or surface.num_points == 2:
            return self._line_intersection_3d(surface)

        # if overlap 
        if np.allclose(self.points, surface.points, atol=1e-10):
            return True

        # for each triangle in first surface
        for i in range(self.num_points - 2):
            triangle1 = np.array([
                self.points[0],
                self.points[i + 1],
                self.points[i + 2]
            ])
            
            # triangle in second surface
            for j in range(surface.num_points - 2):
                triangle2 = np.array([
                    surface.points[0],
                    surface.points[j + 1],
                    surface.points[j + 2]
                ])
                
                # check each edge of triangle1 against triangle2
                for k in range(3):
                    if self._segment_triangle_intersect(
                        triangle1[k],
                        triangle1[(k + 1) % 3],
                        triangle2
                    ):
                        return True
                        
                # check each edge of triangle2 against triangle1
                for k in range(3):
                    if self._segment_triangle_intersect(
                        triangle2[k],
                        triangle2[(k + 1) % 3],
                        triangle1
                    ):
                        return True
        
        return False

    def get_intersection(self, surface):
        # because in crossingfreepartition.py we only care about if there is an intersection or not. It is not necessary to return the intersection points. 
        # so for 3d, we just return a random point if there is an intersection
        if surface.dimention == 3 or self.dimention == 3:
            if self.is_intersecting_3d(surface):
                return [[0, 0, 0]]
 
        
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
            s1 = Surface(self.points[:1])
            s2 = Surface(self.points[1:2])
            s3 = Surface(surface.points[:1])
            s4 = Surface(surface.points[1:2])

            return s3.get_intersection(self) + s4.get_intersection(self) + s1.get_intersection(surface) + s2.get_intersection(surface)
    
        # Calculate intersection point
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det
    
        return np.array([[px, py]])



    # helper functions
    def _compute_normal(self, p1, p2, p3):
        # get the normal vector of the triangle 
        v1 = p2 - p1
        v2 = p3 - p1
        normal = np.cross(v1, v2)
        norm = np.linalg.norm(normal)
        if norm < 1e-10:  # check for degenerate triangle
            return None
        return normal / norm

    def _point_on_plane(self, point, plane_point, normal):
        # if point lies on the plane
        if normal is None:
            return False
        dist = np.dot(normal, point - plane_point)
        return abs(dist) < 1e-10

    # check if a point lies inside a triangle
    def _point_in_triangle(self, point, triangle_points):
        # First check if point is on the plane of the triangle
        normal = self._compute_normal(*triangle_points)
        if normal is None or not self._point_on_plane(point, triangle_points[0], normal):
            return False

        # barycentric coordinates
        v0 = triangle_points[1] - triangle_points[0]
        v1 = triangle_points[2] - triangle_points[0]
        v2 = point - triangle_points[0]

        dot00 = np.dot(v0, v0)
        dot01 = np.dot(v0, v1)
        dot02 = np.dot(v0, v2)
        dot11 = np.dot(v1, v1)
        dot12 = np.dot(v1, v2)

        denom = (dot00 * dot11 - dot01 * dot01)
        if abs(denom) < 1e-10:
            return False

        invDenom = 1.0 / denom
        u = (dot11 * dot02 - dot01 * dot12) * invDenom
        v = (dot00 * dot12 - dot01 * dot02) * invDenom

        return u >= -1e-10 and v >= -1e-10 and (u + v) <= 1 + 1e-10

    # check if a line segment intersects a triangle
    def _segment_triangle_intersect(self, p1, p2, triangle_points):
        normal = self._compute_normal(*triangle_points)
        if normal is None:
            return False

        # check if endpoint 
        if self._point_in_triangle(p1, triangle_points) or self._point_in_triangle(p2, triangle_points):
            return True

        # check if line is parallel to triangle
        direction = p2 - p1
        ndotu = np.dot(normal, direction)

        # if parallele
        if abs(ndotu) < 1e-10: 
            return False

        # intersection point 
        w = p1 - triangle_points[0]
        si = -np.dot(normal, w) / ndotu
        
        # Check if intersection is within segment bounds
        if si < -1e-10 or si > 1 + 1e-10:
            return False

        intersection = p1 + si * direction
        return self._point_in_triangle(intersection, triangle_points)

    def _point_intersection_3d(self, other):
        point = self.points[0] if self.num_points == 1 else other.points[0]
        surface = other if self.num_points == 1 else self

        if surface.num_points == 1:
            return np.allclose(point, surface.points[0], atol=1e-10)
        elif surface.num_points == 2:
            # if point lies on line segment
            p1, p2 = surface.points[0], surface.points[1]
            v = p2 - p1
            w = point - p1
            c1 = np.dot(w, v)
            if c1 <= 0:
                return np.allclose(point, p1, atol=1e-10)
            c2 = np.dot(v, v)
            if c2 <= c1:
                return np.allclose(point, p2, atol=1e-10)
            b = c1 / c2
            pb = p1 + b * v
            return np.allclose(point, pb, atol=1e-10)
        else:
            # if point lies in any triangle of the surface
            for i in range(surface.num_points - 2):
                triangle = np.array([
                    surface.points[0],
                    surface.points[i + 1],
                    surface.points[i + 2]
                ])
                if self._point_in_triangle(point, triangle):
                    return True
            return False

    def _line_intersection_3d(self, other):
        line = self if self.num_points == 2 else other
        surface = other if self.num_points == 2 else self

        # if either endpoint of the line intersects with the surface
        if Surface(np.array([line.points[0]])).is_intersecting_3d(surface):
            return True
        if Surface(np.array([line.points[1]])).is_intersecting_3d(surface):
            return True

        # Check line segment intersection with each triangle
        for i in range(surface.num_points - 2):
            triangle = np.array([
                surface.points[0],
                surface.points[i + 1],
                surface.points[i + 2]
            ])
            if self._segment_triangle_intersect(line.points[0], line.points[1], triangle):
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
