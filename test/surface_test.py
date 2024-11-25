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

if __name__ == '__main__':
    unittest.main()
