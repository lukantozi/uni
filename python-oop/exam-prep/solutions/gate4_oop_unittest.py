import unittest


"""
============================================================
Layer A
============================================================
"""
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


"""
============================================================
Layer B
============================================================
"""
# Task 1
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def __len__(self):
        return len(self._items)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_len_after_push(self):
        prev_len = len(self.s)
        self.s.push(2)
        self.assertGreater(len(self.s), prev_len)

    def test_pop(self):
        self.s.push(3)
        self.assertEqual(self.s.peek(), self.s.pop())

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.s.pop()

    def test_peek_not_remove(self):
        self.s.push(5)
        self.s.peek()
        self.assertEqual(len(self.s), 1)

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.s.peek()


# Task 2
class Temperature:
    def __init__(self, c):
        self.celsius = c

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, c):
        if not isinstance(c, (int, float)):
            raise TypeError("celsius must be a number")
        if c < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = c

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


class TestTemperature(unittest.TestCase):
    def setUp(self):
        self.t = Temperature(31)

    def test_temp_creation(self):
        self.assertTrue(self.t)

    def test_temp_conversion_f(self):
        self.assertAlmostEqual(self.t.fahrenheit, 87.8)

    def test_temp_string(self):
        with self.assertRaises(TypeError):
            self.t.celsius = "30"

    def test_temp_below_k0(self):
        with self.assertRaises(ValueError):
            self.t.celsius = -290


# Task 3
class TestTear(unittest.TestCase):
    tears = []

    def tearDown(self):
        self.tears.append("torn")

    def test_example_1(self):
        self.assertEqual(1, 1)

    def test_example_2(self):
        pass
        #self.assertEqual(1, 2)

    def test_example_3(self):
        self.assertEqual(2, 2)


# Task 4
class Employee:
    raise_amt = 1.10

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, s):
        if not isinstance(s, (int, float)):
            raise TypeError("must be an integer")
        if s < 0:
            raise ValueError("must be non-negative")
        self._pay = s


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.e = Employee("Alice", 50000)

    def test_employee_name(self):
        self.assertEqual(self.e.name, "Alice")

    def test_employee_pay(self):
        self.assertEqual(self.e.pay, 50000)

    def test_employee_raise(self):
        self.e.apply_raise()
        self.assertAlmostEqual(self.e.pay, 55000.0000, places=4)

    def test_employee_neg(self):
        with self.assertRaises(ValueError):
            Employee("Alice", -4)


"""
============================================================
Test implementations
============================================================
"""
result = unittest.main(argv=[""], exit=False, verbosity=2)
print(result.result.wasSuccessful())
print(TestTear.tears)
