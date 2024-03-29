"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""

import math
import unittest
from circle import Circle


class CircleTest(unittest.TestCase):
    """Tests of the Circle class."""
    def setUp(self):
        self.circle1 = Circle(1)
        self.circle2 = Circle(2)
        self.circle3 = Circle(0)

        self.r1 = self.circle1.get_radius()
        self.r2 = self.circle2.get_radius()
        self.r3 = self.circle3.get_radius()

    def test_add_area(self):
        self.assertEqual(self.circle1.add_area(self.circle2).get_radius(),
                         Circle(math.sqrt(self.r1**2+self.r2**2)).get_radius())
        self.assertEqual(self.circle1.add_area(self.circle2).get_area(),
                         Circle(math.sqrt(self.r1**2+self.r2**2)).get_area())

    def test_edge_case(self):
        self.assertEqual(self.circle1.add_area(self.circle3).get_radius(), Circle(self.r1).get_radius())
        self.assertEqual(self.circle1.add_area(self.circle3).get_area(), Circle(self.r1).get_area())

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-2)

