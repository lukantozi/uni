import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.add = self.calculator.add
        self.divide = self.calculator.divide
        self.average = self.calculator.average
        self.triangle_c = self.calculator.calculate_c_in_triangle
        self.parabola_x = self.calculator.calculate_zero_of_the_parabolic_function

    def test_calculator_add(self):
        self.assertEqual(2, self.add(1, 1))
        self.assertNotEqual(0, self.add(-1, -1))

    def test_calculator_divide(self):
        self.assertEqual(5, self.divide(25, 5))
        self.assertNotEqual(2, self.divide(10, 3))
        self.assertAlmostEqual(3.3333, self.divide(10, 3), places=4)
        with self.assertRaises(ZeroDivisionError):
            self.divide(4, 0)

    def test_calculator_average(self):
        self.assertEqual(2, self.average([1, 2, 3]))
        self.assertNotEqual(1, self.average([1, 2, 3]))
        self.assertEqual(5, self.average([5]))
        with self.assertRaises(ZeroDivisionError):
            self.average([])

    def test_triangle_c(self):
        self.assertEqual(5, self.triangle_c(3, 4))
        self.assertNotEqual(3, self.triangle_c(4, 5))

    def test_parabola_x(self):
        self.assertEqual((1.0, 3.0), self.parabola_x(1, -4, 3))
        self.assertEqual(-1.0, self.parabola_x(1, 2, 1))
        self.assertEqual(-0.5, self.parabola_x(0, 4, 2))
        self.assertEqual(((-2 - 2j), (-2 + 2j)), self.parabola_x(1, 2, 5))
        self.assertEqual(None, self.parabola_x(0, 0, 1))


if __name__ == "__main__":
    unittest.main()
