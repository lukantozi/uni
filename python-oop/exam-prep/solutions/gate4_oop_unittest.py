"""
============================================================
Layer A
============================================================
"""
import unittest

# Task 1
class Adder:
    def add(self, a, b):
        return a + b


class TestAdder(unittest.TestCase):
    def setUp(self):
        self.adder = Adder()

    def test_positive(self):
        self.assertEqual(self.adder.add(2, 4), 6)

    def test_negative(self):
        self.assertEqual(self.adder.add(2, -1), 1)

    def test_zero(self):
        self.assertEqual(self.adder.add(2, 0), 2)


# Task 2
class StringUtils:
    def reverse(self, s):
        return s[::-1]


class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.su = StringUtils()

    def test_reverse_normal(self):
        self.assertEqual(self.su.reverse("hello"), "olleh")

    def test_reverse_empty(self):
        self.assertEqual(self.su.reverse(""), "")

    def test_reverse_singleton(self):
        self.assertEqual(self.su.reverse("s"), "s")


# Task 3
class Divider:
    def divide(self, a, b):
        if b == 0:
            raise ValueError("division by zero")
        return a / b


class TestDivider(unittest.TestCase):
    def setUp(self):
        self.d = Divider()
    
    def test_divider_normal(self):
        self.assertEqual(self.d.divide(4, 2), 2)

    def test_divider_raise(self):
        with self.assertRaises(ValueError):
            self.d.divide(5, 0)


# Task 4
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, step=1):
        self.value += step

    def decrement(self, step=1):
        self.value -= step

    def reset(self):
        self.value = 0


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.c = Counter()

    def test_increment(self):
        self.assertEqual(self.c.value, 0)
        self.c.increment()
        self.assertEqual(self.c.value, 1)

    def test_decrement(self):
        self.assertEqual(self.c.value, 0)
        self.c.decrement()
        self.assertEqual(self.c.value, -1)

    def test_reset(self):
        self.c.increment()
        self.assertEqual(self.c.value, 1)
        self.c.reset()
        self.assertEqual(self.c.value, 0)


# Task 5
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.ba = BankAccount()

    def test_deposit(self):
        self.ba.deposit(20)
        self.assertEqual(self.ba.balance, 20)

    def test_withdraw(self):
        self.ba.deposit(100)
        self.ba.withdraw(50)
        self.assertEqual(self.ba.balance, 50)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.ba.deposit(0)

    def test_withdraw_too_much(self):
        with self.assertRaises(ValueError):
            self.ba.withdraw(10)


result = unittest.main(argv=[""], exit=False, verbosity=2)
print(result.result.wasSuccessful())
