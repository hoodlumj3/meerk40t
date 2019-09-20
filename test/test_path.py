from __future__ import print_function

import unittest

import svg_parser
from path import *


class TestPath(unittest.TestCase):

    def test_subpaths(self):
        path = Path()
        svg_parser.parse_svg_path(path, "M0,0 50,50 100,100z M0,100 50,50, 100,0")
        for i, p in enumerate(path.as_subpaths()):
            if i == 0:
                self.assertEqual(p.d(), "M 0,0 L 50,50 L 100,100 Z")
            elif i == 1:
                self.assertEqual(p.d(), "M 0,100 L 50,50 L 100,0")
            self.assertLessEqual(i, 1)

    def test_move_quad_smooth(self):
        path = Path()
        path.move((4, 4), (20, 20), (25, 25), 6 + 3j)
        path.quad((20, 33), (100, 100))
        path.smooth_quad((13, 45), (16, 16), (34, 56), "z")
        self.assertEqual(path.d(), "M 4,4 L 20,20 L 25,25 L 6,3 Q 20,33 100,100 T 13,45 T 16,16 T 34,56 T 4,4 Z")

    def test_move_cubic_smooth(self):
        path = Path()
        path.move((4, 4), (20, 20), (25, 25), 6 + 3j)
        path.cubic((20, 33), (25, 25), (100, 100))
        path.smooth_cubic((13, 45), (16, 16), (34, 56), "z")
        self.assertEqual(path.d(), "M 4,4 L 20,20 L 25,25 L 6,3 C 20,33 25,25 100,100 S 13,45 16,16 S 34,56 4,4 Z")

    def test_transform_scale(self):
        matrix = Matrix()
        path = Path()
        path.move((0, 0), (0, 100), (100, 100), 100 + 0j, "z")
        svg_parser.parse_svg_transform("scale(2)", matrix)
        path *= matrix
        self.assertEqual(path.d(), "M 0,0 L 0,200 L 200,200 L 200,0 L 0,0 Z")

    def test_transform_skewx(self):
        matrix = Matrix()
        path = Path()
        path.move((0, 0), (0, 100), (100, 100), 100 + 0j, "z")
        svg_parser.parse_svg_transform("skewX(10,50,50)", matrix)
        path *= matrix
        self.assertEqual(path.d(), "M -8.81635,0 L 8.81635,100 L 108.816,100 L 91.1837,0 L -8.81635,0 Z")

    def test_transform_skewy(self):
        matrix = Matrix()
        path = Path()
        path.move((0, 0), (0, 100), (100, 100), 100 + 0j, "z")
        svg_parser.parse_svg_transform("skewY(10, 50,50)", matrix)
        path *= matrix
        print(path.d())
        self.assertEqual(path.d(), "M 0,-8.81635 L 0,91.1837 L 100,108.816 L 100,8.81635 L 0,-8.81635 Z")