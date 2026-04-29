import math
import cmath

class Calculator:
    """ A simple calculator App"""

    def add(self, x, y):
        """Add Function"""
        return x + y

    def divide(self, x, y):
        """Divide Function"""
        return x / y

    def average(self, list):
        """ List Function """
        return sum(list) / len(list)

    def calculate_c_in_triangle(self, a, b):
        """ Use Pythagoras theorem """
        return math.sqrt(a**2 + b**2)

    def calculate_zero_of_the_parabolic_function(self, a, b, c):
        """ If you dont remember, google :) """
        if a == 0:
            if b == 0 and c != 0:
                return None
            elif b != 0:
                return -c / b
        else:
            d = b**2 - (4 * a * c)
            if d > 0:
                x1 = (-b - math.sqrt(d)) / (2 * a)
                x2 = (-b + math.sqrt(d)) / (2 * a)
                return x1, x2
            elif d == 0:
                return -b / (2 * a)
            else:
                x1 = (-b - cmath.sqrt(d) / (2 * a))
                x2 = (-b + cmath.sqrt(d) / (2 * a))
                return x1, x2
