import unittest
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Surface import Surface

class TestSurface(unittest.TestCase):

    def test_no_intersection(self):
        points1 = np.array([[0, 0], [1, 0]])
        points2 = np.array([[2, 2], [3, 2]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertFalse(surface1.is_intersecting(surface2))

    def test_intersection(self):
        points1 = np.array([[0, 0], [1, 1]])
        points2 = np.array([[0, 1], [1, 0]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_collinear_no_intersection(self):
        points1 = np.array([[0, 0], [2, 2]])
        points2 = np.array([[3, 3], [4, 4]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertFalse(surface1.is_intersecting(surface2))

    def test_collinear_intersection(self):
        points1 = np.array([[0, 0], [2, 2]])
        points2 = np.array([[1, 1], [3, 3]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_shared_endpoint_intersection(self):
        points1 = np.array([[0, 0], [1, 1]])
        points2 = np.array([[1, 1], [0, 2]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_single_point_no_intersection(self):
        points1 = np.array([[0, 0]])
        points2 = np.array([[1, 1], [2, 2]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertFalse(surface1.is_intersecting(surface2))

    def test_single_point_on_edge(self):
        points1 = np.array([[1, 1]])
        points2 = np.array([[0, 0], [2, 2]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_single_point_intersecting_vertex(self):
        points1 = np.array([[1, 1]])
        points2 = np.array([[0, 0], [1, 1]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_single_point_vs_single_point_no_intersection(self):
        points1 = np.array([[0, 0]])
        points2 = np.array([[1, 1]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertFalse(surface1.is_intersecting(surface2))

    def test_single_point_vs_single_point_intersection(self):
        points1 = np.array([[0, 0]])
        points2 = np.array([[0, 0]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_polygon_with_single_point_inside(self):
        points1 = np.array([[0, 0], [2, 0], [1, 2]])
        points2 = np.array([[1, 1]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertFalse(surface1.is_intersecting(surface2))

    def test_polygon_with_single_point_on_edge(self):
        points1 = np.array([[0, 0], [2, 0], [1, 2]])
        points2 = np.array([[1, 0]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_polygon_with_single_point_on_vertex(self):
        points1 = np.array([[0, 0], [2, 0], [1, 2]])
        points2 = np.array([[0, 0]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_polygon_touching_at_edge(self):
        points1 = np.array([[0, 0], [2, 0], [1, 2]])
        points2 = np.array([[2, 0], [4, 0], [3, 2]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_polygon_touching_at_vertex(self):
        points1 = np.array([[0, 0], [2, 0], [1, 2]])
        points2 = np.array([[2, 0], [3, -1], [4, 1]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting(surface2))

    def test_3d_no_intersection_parallel_planes(self):
        points1 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        points2 = np.array([[0, 0, 1], [1, 0, 1], [0, 1, 1]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertEqual(surface1.is_intersecting_3d(surface2), False)

    def test_3d_intersection_planes(self):
        points1 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        points2 = np.array([[0, 0, 0], [1, 0, 1], [0, 1, 1]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        intersection = surface1.is_intersecting_3d(surface2)
        self.assertTrue(intersection == True)  # Should intersect in a line or points

    def test_3d_intersection_polygon_and_line(self):
        polygon_points = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        line_points = np.array([[0.5, 0.5, -1], [0.5, 0.5, 1]])
        polygon = Surface(polygon_points)
        line = Surface(line_points)
        intersection = polygon.is_intersecting_3d(line)
        self.assertTrue(intersection == True)  # Should intersect at a point

    def test_3d_intersection_polygon_and_point(self):
        polygon_points = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        point = np.array([[0.5, 0.5, 0]])
        polygon = Surface(polygon_points)
        point_surface = Surface(point)
        intersection = polygon.is_intersecting_3d(point_surface)
        self.assertTrue(intersection == True)  # Intersection is the point itself

    def test_3d_intersection_skew_planes(self):
        points1 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        points2 = np.array([[0, 0, 1], [1, 0, 1], [0, 1, -1]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        intersection = surface1.is_intersecting_3d(surface2)
        self.assertTrue(intersection == True)  # Skew planes should intersect in a line

    def test_3d_intersection_overlapping_polygon(self):
        points1 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        points2 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        intersection = surface1.is_intersecting_3d(surface2)
        self.assertTrue(intersection == True)  # Overlapping surfaces should intersect


    def test_3d_collinear_overlapping_lines(self):
        # Two overlapping line segments on the same line
        points1 = np.array([[0, 0, 0], [2, 2, 2]])  
        points2 = np.array([[1, 1, 1], [3, 3, 3]]) 
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting_3d(surface2))

    def test_3d_collinear_point_on_line(self):
        # Point lying exactly on a line segment
        line_points = np.array([[0, 0, 0], [2, 2, 2]])  
        point = np.array([[1, 1, 1]])  
        line = Surface(line_points)
        point_surface = Surface(point)
        self.assertTrue(line.is_intersecting_3d(point_surface))


    def test_3d_collinear_degenerate_triangle(self):
        # Three collinear points forming a degenerate triangle
        triangle_points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
        # Line segment that intersects the collinear points
        line_points = np.array([[0.5, 0.5, 0.5], [1.5, 1.5, 1.5]])
        triangle = Surface(triangle_points)
        line = Surface(line_points)
        self.assertTrue(triangle.is_intersecting_3d(line))


    def test_3d_collinear_non_intersecting(self):
        # Two collinear but non-intersecting line segments
        points1 = np.array([[0, 0, 0], [1, 1, 1]])
        points2 = np.array([[2, 2, 2], [3, 3, 3]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertFalse(surface1.is_intersecting_3d(surface2))

    def test_3d_collinear_multiple_points(self):
        # Multiple collinear points as vertices
        points1 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
        # Line segment that passes through middle
        points2 = np.array([[1.5, 1.5, 1.5], [2.5, 2.5, 2.5]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting_3d(surface2))

        
    def test_3d_collinear_endpoint_intersection(self):
        # Two line segments that meet exactly at endpoints
        points1 = np.array([[0, 0, 0], [1, 1, 1]])
        points2 = np.array([[1, 1, 1], [2, 2, 2]])
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting_3d(surface2))


    def test_3d_collinear_different_directions(self):
        # Two line segments on same line but pointing different directcions
        points1 = np.array([[0, 0, 0], [2, 2, 2]])
        points2 = np.array([[3, 3, 3], [1, 1, 1]])  # Note: reversed direction
        surface1 = Surface(points1)
        surface2 = Surface(points2)
        self.assertTrue(surface1.is_intersecting_3d(surface2))


if __name__ == '__main__':
    unittest.main()
