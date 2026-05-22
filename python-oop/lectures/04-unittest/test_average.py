import unittest
from average import average

class TestAverage(unittest.TestCase):
    def test_average_singleton_list(self):
        self.assertEqual(5, average([5]))

    def test_list_with_many_values(self):
        self.assertEqual(3, average([1, 2, 3, 4, 5]))

    def test_average_of_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            average([])
