# Gate 4 — Unit Testing
> Topics: `unittest.TestCase`, `setUp`, `tearDown`, `assertEqual`, `assertNotEqual`,
> `assertTrue`, `assertFalse`, `assertIsNone`, `assertRaises`, `assertIn`,
> testing OOP classes, edge cases, testing exceptions.

***

## Layer A — Skeleton (core rules)

### Predict-output drills (answer before running — write answers on paper)

**1.**
```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**2.**
```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 3)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**3.**
```python
import unittest

class TestChecks(unittest.TestCase):
    def test_true(self):
        self.assertTrue(5 > 3)
    def test_false(self):
        self.assertFalse(2 > 10)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**4.**
```python
import unittest

class TestNone(unittest.TestCase):
    def test_none(self):
        x = None
        self.assertIsNone(x)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**5.**
```python
import unittest

class TestIn(unittest.TestCase):
    def test_in(self):
        self.assertIn(3, [1, 2, 3, 4])

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**6.**
```python
import unittest

class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalc(unittest.TestCase):
    def test_divide_by_zero(self):
        c = Calculator()
        with self.assertRaises(ValueError):
            c.divide(10, 0)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**7.**
```python
import unittest

class TestSetUp(unittest.TestCase):
    def setUp(self):
        self.value = 42

    def test_value(self):
        self.assertEqual(self.value, 42)

    def test_double(self):
        self.assertEqual(self.value * 2, 84)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**8.**
```python
import unittest

class TestNotEqual(unittest.TestCase):
    def test_ne(self):
        self.assertNotEqual(1, 2)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**9.**
```python
import unittest

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0

class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_empty(self):
        self.assertTrue(self.s.is_empty())

    def test_push_pop(self):
        self.s.push(1)
        self.assertEqual(self.s.pop(), 1)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**10.**
```python
import unittest

class TestRaises(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(TypeError):
            x = "a" + 1

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**11.**
```python
import unittest

class TestRaises(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(ValueError):
            x = "a" + 1

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**12.**
```python
import unittest

class TestSetUp(unittest.TestCase):
    def setUp(self):
        self.data = []

    def test_append(self):
        self.data.append(1)
        self.assertIn(1, self.data)

    def test_still_empty(self):
        self.assertEqual(len(self.data), 0)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**13.**
```python
import unittest

class TestAsserts(unittest.TestCase):
    def test_is_none(self):
        self.assertIsNone(None)
    def test_is_not_none(self):
        self.assertIsNotNone(42)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**14.**
```python
import unittest

class MyClass:
    def greet(self):
        return "hello"

class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.obj = MyClass()

    def test_greet(self):
        self.assertEqual(self.obj.greet(), "hello")

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**15.**
```python
import unittest

class TestFail(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 1)
    def test_two(self):
        self.assertEqual(1, 2)
    def test_three(self):
        self.assertTrue(True)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

***

### Answers — Layer A predict-output

| # | Answer |
|---|--------|
| 1 | `True` |
| 2 | `False` — `assertEqual(2, 3)` fails |
| 3 | `2` then `True` — 2 tests run, both pass |
| 4 | `True` |
| 5 | `True` |
| 6 | `True` — `assertRaises` catches the `ValueError`, test passes |
| 7 | `2` then `True` — `setUp` runs fresh before each test |
| 8 | `True` |
| 9 | `2` then `True` |
| 10 | `True` — `"a" + 1` raises `TypeError`, which is what we assert |
| 11 | `False` — `"a" + 1` raises `TypeError`, not `ValueError`, so the test fails |
| 12 | `2` then `True` — `setUp` creates a fresh `[]` for each test, so `test_still_empty` sees an empty list |
| 13 | `2` then `True` |
| 14 | `True` |
| 15 | `3` then `False` — 3 tests run, `test_two` fails |

**Pass: 13/15 correct on first attempt, no running code.**

***

### Coding drills — Layer A

**1.** Create a class `Adder` with a method `add(a, b)` that returns `a + b`. Write a `TestAdder` test case with at least 3 test methods: adding two positives, adding a negative, adding zero. Run and verify all pass.

**2.** Create a class `StringUtils` with a method `reverse(s)` that returns the reversed string. Write a `TestStringUtils` test case. Test normal string, empty string, single character.

**3.** Create a class `Divider` with `divide(a, b)` that raises `ValueError("division by zero")` if `b == 0`. Write a test that uses `assertRaises` to verify the exception is raised. Also test a normal division.

**4.** Create a class `Counter` with `increment()`, `decrement()`, and `reset()` methods and a `value` attribute starting at 0. Write a `TestCounter` test case that uses `setUp` to create a fresh `Counter` instance before each test. Test increment, decrement, and reset independently.

**5.** Write a test class for the following `BankAccount`:
```python
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
```
Cover: deposit works, withdraw works, deposit with zero raises `ValueError`, withdraw more than balance raises `ValueError`.

**Pass: All 5 drills correct on first run. All tests pass (green).**

***

## Layer B — Variants & gotchas

### Predict-output drills (14 questions)

**1.**
```python
import unittest

class TestSetUp(unittest.TestCase):
    def setUp(self):
        self.items = []

    def test_a(self):
        self.items.append("x")
        self.assertEqual(len(self.items), 1)

    def test_b(self):
        self.assertEqual(len(self.items), 0)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**2.**
```python
import unittest

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.log = []

    def tearDown(self):
        self.log.append("tear")

    def test_one(self):
        self.log.append("test")
        self.assertEqual(len(self.log), 1)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**3.**
```python
import unittest

class TestRaisesMsg(unittest.TestCase):
    def test_msg(self):
        with self.assertRaises(ValueError) as ctx:
            raise ValueError("bad input")
        self.assertEqual(str(ctx.exception), "bad input")

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**4.**
```python
import unittest

class TestSkip(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(1, 1)

    @unittest.skip("not implemented yet")
    def test_skipped(self):
        self.assertEqual(1, 2)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**5.**
```python
import unittest

class Validator:
    def validate(self, x):
        if not isinstance(x, int):
            raise TypeError("must be int")
        if x < 0:
            raise ValueError("must be non-negative")
        return True

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.v = Validator()

    def test_valid(self):
        self.assertTrue(self.v.validate(5))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.v.validate("hello")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.v.validate(-1)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**6.**
```python
import unittest

class TestRaisesWrong(unittest.TestCase):
    def test_wrong_exception(self):
        with self.assertRaises(ValueError):
            raise TypeError("wrong type")

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**7.**
```python
import unittest

class TestRaisesNoRaise(unittest.TestCase):
    def test_no_exception(self):
        with self.assertRaises(ValueError):
            x = 1 + 1

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**8.**
```python
import unittest

class MyList:
    def __init__(self):
        self.data = []
    def add(self, item):
        self.data.append(item)
    def get(self, index):
        return self.data[index]

class TestMyList(unittest.TestCase):
    def setUp(self):
        self.lst = MyList()
        self.lst.add(10)
        self.lst.add(20)

    def test_get(self):
        self.assertEqual(self.lst.get(0), 10)

    def test_second(self):
        self.assertEqual(self.lst.get(1), 20)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**9.**
```python
import unittest

class TestEdge(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(len(""), 0)
        self.assertFalse("")

    def test_zero(self):
        self.assertEqual(0, 0)
        self.assertFalse(0)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**10.**
```python
import unittest

class TestMultiAssert(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(1 + 1, 2)
        self.assertEqual(2 + 2, 5)
        self.assertEqual(3 + 3, 6)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**11.**
```python
import unittest

class TestAssertIn(unittest.TestCase):
    def test_in_string(self):
        self.assertIn("ell", "hello")

    def test_in_dict(self):
        self.assertIn("key", {"key": 1})

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())
```

**12.**
```python
import unittest

class Calc:
    def square(self, n):
        return n * n

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.c = Calc()

    def test_positive(self):
        self.assertEqual(self.c.square(3), 9)

    def test_negative(self):
        self.assertEqual(self.c.square(-4), 16)

    def test_zero(self):
        self.assertEqual(self.c.square(0), 0)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

**13.**
```python
import unittest

class TestTearDown(unittest.TestCase):
    results = []

    def tearDown(self):
        self.results.append("done")

    def test_one(self):
        pass

    def test_two(self):
        pass

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(len(TestTearDown.results))
print(result.result.wasSuccessful())
```

**14.**
```python
import unittest

class TestAssertEqual(unittest.TestCase):
    def test_list(self):
        self.assertEqual([1, 2, 3], [1, 2, 3])

    def test_dict(self):
        self.assertEqual({"a": 1}, {"a": 1})

    def test_identity(self):
        a = [1, 2]
        b = [1, 2]
        self.assertEqual(a, b)
        self.assertFalse(a is b)

result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

***

### Answers — Layer B

| # | Answer |
|---|--------|
| 1 | `True` — `setUp` creates a **fresh** `[]` before every test, so `test_b` sees an empty list |
| 2 | `True` — `setUp` runs before test, `tearDown` runs after; `test_one` only sees `["test"]` when asserting |
| 3 | `True` — `ctx.exception` gives the raised exception, `str()` on it gives the message |
| 4 | `1` then `True` — skipped test does NOT count toward `testsRun`, and does not count as failure |
| 5 | `3` then `True` |
| 6 | `False` — asserting `ValueError` but `TypeError` is raised → test fails (wrong exception type propagates) |
| 7 | `False` — no exception was raised inside the `with` block, so `assertRaises` fails |
| 8 | `2` then `True` |
| 9 | `True` |
| 10 | `False` — test stops at the first failing assertion (`2 + 2 == 5`), third assert never runs |
| 11 | `True` — `assertIn` checks substring in string, and key in dict |
| 12 | `3` then `True` |
| 13 | `2` then `True` — `tearDown` runs after each test, 2 tests → 2 entries in `results` |
| 14 | `3` then `True` — `assertEqual` compares by value not identity, `assertFalse(a is b)` passes because they are different objects |

**Pass: 12/14 correct, no notes.**

***

### Coding drills — Layer B

**1.** Write a test class for this `Stack`:
```python
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
```
Use `setUp`. Test: push increases len, pop returns correct item, pop from empty raises `IndexError`, peek doesn't remove item, peek on empty raises `IndexError`.

**2.** Write tests for this `Temperature` class that has a `celsius` property with validation:
```python
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
```
Test: valid creation, fahrenheit conversion (use `assertAlmostEqual`), `TypeError` on string input, `ValueError` below -273.15.

**3.** Write tests that verify `tearDown` runs even when a test fails. Use a class variable list to record when `tearDown` is called. Run 3 tests where one deliberately fails. Verify `tearDown` ran 3 times.

**4.** Write a `TestEmployee` class using `setUp` to create an `Employee("Alice", 50000)`. Test that: `name` is `"Alice"`, `salary` is `50000`, giving a 10% raise changes salary to `55000`, and that creating an `Employee` with a negative salary raises `ValueError`. Use at least 4 test methods.

**Pass: All 4 drills correct. All tests pass (or fail only where deliberately intended).**

***

## Layer C — Speed Run

30 questions. Write all answers on paper first. No running code until you have answered all 30. Target under 20 minutes.

```python
# 1
import unittest
class T(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(2 + 2, 4)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 2
import unittest
class T(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(2 + 2, 5)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 3
import unittest
class T(unittest.TestCase):
    def test_a(self):
        self.assertTrue(True)
    def test_b(self):
        self.assertTrue(False)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())

# 4
import unittest
class T(unittest.TestCase):
    def setUp(self):
        self.x = 10
    def test_one(self):
        self.x = 99
        self.assertEqual(self.x, 99)
    def test_two(self):
        self.assertEqual(self.x, 10)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 5
import unittest
class T(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            x = 1 / 0
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 6
import unittest
class T(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(ValueError):
            x = 1 / 0
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 7
import unittest
class T(unittest.TestCase):
    def test_no_raise(self):
        with self.assertRaises(ValueError):
            x = 1 + 1
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 8
import unittest
class T(unittest.TestCase):
    def test_in(self):
        self.assertIn("a", ["a", "b", "c"])
    def test_not_in(self):
        self.assertNotIn("z", ["a", "b", "c"])
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 9
import unittest
class T(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(None)
    def test_not_none(self):
        self.assertIsNone(0)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 10
import unittest
class T(unittest.TestCase):
    def setUp(self):
        self.data = []
    def test_a(self):
        self.data.append(1)
        self.assertEqual(len(self.data), 1)
    def test_b(self):
        self.assertEqual(len(self.data), 0)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 11
import unittest
class T(unittest.TestCase):
    def test_equal_lists(self):
        self.assertEqual([1, 2, 3], [1, 2, 3])
    def test_equal_dicts(self):
        self.assertEqual({"a": 1}, {"a": 1})
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 12
import unittest
class T(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(1, 1)
        self.assertEqual(2, 3)
        self.assertEqual(4, 4)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 13
import unittest
class T(unittest.TestCase):
    @unittest.skip("skip me")
    def test_skipped(self):
        self.assertEqual(1, 2)
    def test_normal(self):
        self.assertEqual(1, 1)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())

# 14
import unittest
class T(unittest.TestCase):
    def test_raises_msg(self):
        with self.assertRaises(ValueError) as ctx:
            raise ValueError("oops")
        self.assertEqual(str(ctx.exception), "oops")
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 15
import unittest
class T(unittest.TestCase):
    results = []
    def tearDown(self):
        self.results.append(1)
    def test_a(self): pass
    def test_b(self): pass
    def test_c(self): pass
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(len(T.results))

# 16
import unittest
class T(unittest.TestCase):
    def test_almost(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=5)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 17
import unittest
class T(unittest.TestCase):
    def test_almost_fail(self):
        self.assertAlmostEqual(0.1, 0.9, places=5)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 18
import unittest
class T(unittest.TestCase):
    def test_identity(self):
        a = [1, 2]
        b = [1, 2]
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 19
import unittest
class T(unittest.TestCase):
    def test_type(self):
        self.assertIsInstance(42, int)
        self.assertIsInstance("hi", str)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 20
import unittest
class T(unittest.TestCase):
    def test_raises_wrong(self):
        with self.assertRaises(ValueError):
            raise TypeError("wrong")
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 21
import unittest
class T(unittest.TestCase):
    def setUp(self):
        self.val = 0
    def tearDown(self):
        self.val = -1
    def test_one(self):
        self.val += 1
        self.assertEqual(self.val, 1)
    def test_two(self):
        self.assertEqual(self.val, 0)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 22
import unittest
class T(unittest.TestCase):
    def test_not_equal(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual("a", "b")
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 23
import unittest
class T(unittest.TestCase):
    def test_false(self):
        self.assertFalse(0)
        self.assertFalse([])
        self.assertFalse("")
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 24
import unittest
class T(unittest.TestCase):
    def test_true(self):
        self.assertTrue(1)
        self.assertTrue([1])
        self.assertTrue("a")
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 25
import unittest
class T(unittest.TestCase):
    def test_raises_catches_subclass(self):
        with self.assertRaises(Exception):
            raise ValueError("sub")
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 26
import unittest
class T(unittest.TestCase):
    def test_a(self):
        self.fail("forced failure")
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 27
import unittest
class T(unittest.TestCase):
    def setUp(self):
        self.items = [1, 2, 3]
    def test_len(self):
        self.assertEqual(len(self.items), 3)
    def test_contains(self):
        self.assertIn(2, self.items)
    def test_not_contains(self):
        self.assertNotIn(5, self.items)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())

# 28
import unittest
class T(unittest.TestCase):
    def test_is(self):
        a = None
        self.assertIs(a, None)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 29
import unittest
class T(unittest.TestCase):
    def test_raises_no_block(self):
        self.assertRaises(ValueError, int, "abc")
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.wasSuccessful())

# 30
import unittest
class T(unittest.TestCase):
    def test_one(self): self.assertEqual(1, 1)
    def test_two(self): self.assertEqual(2, 2)
    def test_three(self): self.assertEqual(1, 2)
result = unittest.main(argv=[""], exit=False, verbosity=0)
print(result.result.testsRun)
print(result.result.wasSuccessful())
```

### Answers — Layer C

| # | Answer |
|---|--------|
| 1 | `True` |
| 2 | `False` |
| 3 | `2` then `False` |
| 4 | `True` — `setUp` resets `self.x = 10` before each test |
| 5 | `True` |
| 6 | `False` — `ZeroDivisionError` raised, not `ValueError` |
| 7 | `False` — no exception raised, `assertRaises` fails |
| 8 | `True` |
| 9 | `False` — `assertIsNone(0)` fails, `0` is not `None` |
| 10 | `True` — `setUp` creates fresh `[]` each time |
| 11 | `True` |
| 12 | `False` — stops at first failing assert (`assertEqual(2, 3)`) |
| 13 | `1` then `True` — skipped test not counted in `testsRun` |
| 14 | `True` |
| 15 | `3` — `tearDown` runs after each of 3 tests |
| 16 | `True` — `assertAlmostEqual` handles float rounding |
| 17 | `False` — `0.1` and `0.9` are not almost equal to 5 decimal places |
| 18 | `True` — `assertEqual` compares value, `assertIsNot` confirms different objects |
| 19 | `True` |
| 20 | `False` — wrong exception type |
| 21 | `True` — `setUp` resets `val = 0` before each test; `tearDown` runs after but doesn't affect next test's setUp |
| 22 | `True` |
| 23 | `True` |
| 24 | `True` |
| 25 | `True` — `assertRaises(Exception)` catches subclasses like `ValueError` |
| 26 | `False` — `self.fail()` always fails the test |
| 27 | `3` then `True` |
| 28 | `True` |
| 29 | `True` — `assertRaises` can be called as a function: `assertRaises(exc, callable, *args)` |
| 30 | `3` then `False` |

**Pass: 27/30 correct, under 20 minutes, no notes.**
