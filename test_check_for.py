import unittest
import check_for

class TriangleTestCase(unittest.TestCase):
    def test_is_not_number(self):
        self.assertEqual(check_for.check_for_number("5"), 0)
    def test_is_number(self):
        self.assertEqual(check_for.check_for_number(5), 1)

    def test_is_negative(self):
        self.assertEqual(check_for.check_for_not_negative(-5), 0)
    def test_is_not_negative(self):
        self.assertEqual(check_for.check_for_not_negative(5), 1)