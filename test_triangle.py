import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_incorrect_type_area(self):
        with self.assertRaises(TypeError):
            triangle.area("5", 6)
    def test_incorrect_value_area(self):
        with self.assertRaises(ValueError):
            triangle.area(-5, 6)
    def test_area(self):
        self.assertEqual(triangle.area(5, 6), 15)

    def test_incorrect_type_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("5", 6, [8])
    def test_incorrect_value_perimeter(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, 6, 0)
    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 6, 4), 15)

    def test_incorrect_type_triangle(self):
        with self.assertRaises(TypeError):
            triangle.is_correct_triangle("5", 6, [8])
    def test_incorrect_value_triangle(self):
        with self.assertRaises(ValueError):
            triangle.is_correct_triangle(-5, 6, 0)
    def test_correct_triangle(self):
        self.assertEqual(triangle.is_correct_triangle(5, 6, 4), 1)
    def test_incorrect_triangle(self):
        self.assertEqual(triangle.is_correct_triangle(5, 6, 14), 0)