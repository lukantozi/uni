# Gate 1 — OOP Basics
> Topics: class definition, `__init__`, `self`, `__str__`, naming conventions,
> `type()` / `id()` / `dir()`, instance vs class attributes, regular / class / static methods,
> modifying object properties, creating instances.

---

## Layer A — Skeleton (core rules)

### Predict-output drills (answer before running — write answers on paper)

**1.**
```python
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Rex")
print(d.name)
```

**2.**
```python
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog: {self.name}"

d = Dog("Rex")
print(d)
```

**3.**
```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
print(Counter.count)
```

**4.**
```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
print(a.count)
print(b.count)
```

**5.**
```python
class Dog:
    species = "Canis familiaris"
    def __init__(self, name):
        self.name = name

d = Dog("Rex")
d.species = "Wolf"
print(d.species)
print(Dog.species)
```

**6.**
```python
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
    def accelerate(self, amount):
        self.speed += amount

c = Car("BMW")
c.accelerate(50)
c.accelerate(30)
print(c.speed)
```

**7.**
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(type(p))
```

**8.**
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
p.name = "Bob"
print(p.name)
```

**9.**
```python
class Box:
    @staticmethod
    def info():
        return "I am a box"

print(Box.info())
```

**10.**
```python
class Box:
    label = "generic"

    @classmethod
    def change_label(cls, new_label):
        cls.label = new_label

Box.change_label("special")
print(Box.label)
```

**11.**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"

a = Animal("Cat")
print(a.speak())
```

**12.**
```python
class Student:
    school = "MIT"
    def __init__(self, name):
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")
Student.school = "Harvard"
print(s1.school)
print(s2.school)
```

**13.**
```python
class Foo:
    x = 10
    def __init__(self):
        self.x = 99

f = Foo()
print(f.x)
print(Foo.x)
```

**14.**
```python
class Robot:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

robots = [Robot("R2D2"), Robot("C3PO")]
for r in robots:
    print(r)
```

**15.**
```python
class MyClass:
    pass

obj = MyClass()
obj.color = "red"
print(obj.color)
```

---

### Answers — Layer A predict-output

| # | Answer |
|---|--------|
| 1 | `Rex` |
| 2 | `Dog: Rex` |
| 3 | `2` |
| 4 | `2` then `2` (class attr shared) |
| 5 | `Wolf` then `Canis familiaris` (instance attr shadows class attr) |
| 6 | `80` |
| 7 | `<class '__main__.Person'>` |
| 8 | `Bob` (object properties are mutable) |
| 9 | `I am a box` |
| 10 | `special` |
| 11 | `Cat makes a sound` |
| 12 | `Harvard` then `Harvard` (class attr change affects all instances) |
| 13 | `99` then `10` (instance attr shadows class attr) |
| 14 | `R2D2` then `C3PO` |
| 15 | `red` (can add attrs to instance dynamically) |

**Pass: 13/15 correct on first attempt, no running code.**

---

### Coding drills — Layer A

**1.** Create a class `Rectangle` with attributes `width` and `height` set in `__init__`. Add a method `area()` that returns width × height, and a `__str__` that prints `Rectangle(width x height)`. Create two instances with different sizes and print them.

**2.** Create a class `BankAccount` with attribute `balance` (default 0). Add methods `deposit(amount)` and `withdraw(amount)`. `withdraw` should print `"Insufficient funds"` if balance would go negative. Add `__str__` showing current balance. Demonstrate with a few operations.

**3.** Create a class `Student` with a **class attribute** `student_count = 0` that increments each time a new student is created. Add instance attributes `name` and `grade`. Add a **class method** `get_count()` that returns the current count. Add a **static method** `passing_grade()` that returns `60`. Create 3 students and verify the count.

**4.** Create a class `Temperature` with attribute `celsius`. Add a method `to_fahrenheit()` that returns `celsius * 9/5 + 32`. Add `__str__` showing both values. Demonstrate with at least 3 instances.

**5.** Without running code first — write what the following prints, then verify:
```python
class Vehicle:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand
    def describe(self):
        return f"{self.brand} has {self.wheels} wheels"

v = Vehicle("Toyota")
Vehicle.wheels = 6
print(v.describe())
print(Vehicle.wheels)
```

**Pass: All 5 drills work correctly on first run (no bugs). Drill 5 predicted correctly before running.**

---

## Layer B — Variants & gotchas

### Predict-output drills (14 questions)

**1.**
```python
class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

d1 = Dog("Rex")
d2 = Dog("Buddy")
d1.add_trick("sit")
print(d2.tricks)
```

**2.**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(p)
print(repr(p))
```

**3.**
```python
class Foo:
    def __init__(self):
        self.x = 1
    def get_x(self):
        return self.x

f = Foo()
Foo.y = 100
print(f.y)
```

**4.**
```python
class Counter:
    count = 0
    def __init__(self):
        self.count += 1   # note: self.count, not Counter.count

a = Counter()
b = Counter()
print(Counter.count)
print(a.count)
```

**5.**
```python
class MyClass:
    def method(self):
        return "instance method"
    @classmethod
    def cls_method(cls):
        return "class method"
    @staticmethod
    def static_method():
        return "static method"

obj = MyClass()
print(obj.method())
print(obj.cls_method())
print(obj.static_method())
```

**6.**
```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = p1
p2.name = "Bob"
print(p1.name)
```

**7.**
```python
class Box:
    items = []
    def __init__(self, label):
        self.label = label
        self.items = []   # overrides class attr with instance attr

b1 = Box("A")
b2 = Box("B")
b1.items.append("pen")
print(b2.items)
```

**8.**
```python
class MyClass:
    x = 5
    def __init__(self):
        pass
    def double(self):
        return self.x * 2

obj = MyClass()
print(obj.double())
MyClass.x = 10
print(obj.double())
```

**9.**
```python
class Validator:
    @staticmethod
    def is_positive(n):
        return n > 0
    @classmethod
    def describe(cls):
        return f"I am {cls.__name__}"

print(Validator.is_positive(-1))
print(Validator.describe())
```

**10.**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Animal: {self.name}"

a = Animal("Lion")
print(str(a))
print(a)
```

**11.**
```python
class Foo:
    pass

f = Foo()
print(type(f) == Foo)
print(type(f) == type(Foo))
```

**12.**
```python
class Config:
    debug = False

c = Config()
c.debug = True
print(Config.debug)
print(c.debug)
```

**13.**
```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def reset(cls):
        cls.count = 0

Counter()
Counter()
Counter()
print(Counter.count)
Counter.reset()
print(Counter.count)
```

**14.**
```python
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog({self.name})"

dogs = [Dog("Rex"), Dog("Buddy"), Dog("Max")]
print([str(d) for d in dogs])
```

---

### Answers — Layer B

| # | Answer |
|---|--------|
| 1 | `['sit']` — mutable class attribute (list) shared by ALL instances (classic gotcha!) |
| 2 | `Alice, 30` then `Person('Alice', 30)` — `print()` uses `__str__`, `repr()` uses `__repr__` |
| 3 | `100` — attributes added to the class after creation are accessible on existing instances |
| 4 | `Counter.count` stays `0`; `a.count` is `1` — `self.count += 1` creates an instance attr, doesn't modify class attr |
| 5 | `instance method` / `class method` / `static method` — all three work on instances |
| 6 | `Bob` — both `p1` and `p2` point to the same object |
| 7 | `[]` — `self.items = []` in `__init__` creates a fresh instance attr, class attr not touched |
| 8 | `10` then `20` — `self.x` falls through to class attr; changing `MyClass.x` affects all lookups |
| 9 | `False` then `I am Validator` |
| 10 | `Animal: Lion` then `Animal: Lion` — `str(a)` and `print(a)` both call `__str__` |
| 11 | `True` then `False` — `type(f) == Foo` is True; `type(f) == type(Foo)` compares `Foo` to `type` (metaclass) |
| 12 | `False` then `True` — instance attr `c.debug` shadows class attr but doesn't change it |
| 13 | `3` then `0` |
| 14 | `['Dog(Rex)', 'Dog(Buddy)', 'Dog(Max)']` |

**Pass: 12/14 correct, no notes.**

---

### Coding drills — Layer B

**1.** The classic mutable default gotcha: rewrite the `Dog` class from B-drill-1 above so each dog gets its **own** independent tricks list. Verify `d1.add_trick("sit")` does NOT affect `d2.tricks`.

**2.** Create a class `Car` where:
- `make` and `model` are instance attrs
- `total_cars` is a class attr that tracks how many Cars were created
- `reset_count()` is a class method that resets the counter to 0
- `validate_speed(speed)` is a static method that returns `True` if speed is between 0 and 300
Show that `total_cars` updates correctly after creating 3 cars and resetting.

**3.** Create a class `Config` where setting `Config.debug = True` on the class does NOT affect instances that already have their own `debug` attribute set. Demonstrate the shadowing clearly with `print` statements.

**4.** Write a `__repr__` method for a `Product` class with `name` and `price` attrs. Show the difference in output between `print(p)` (uses `__str__`) and `repr(p)` (uses `__repr__`). If only `__repr__` is defined and not `__str__`, what does `print(p)` show?

**Pass: All 4 drills work correctly. You can explain the mutable default and shadowing gotchas from memory.**

---

## Layer C — Speed Run

30 questions. Write all answers on paper first (or in a text file). No running code until you've answered all 30. Time yourself — target under 20 minutes.

```python
# 1
class A:
    x = 1
a = A()
print(a.x)

# 2
class A:
    x = 1
a = A()
a.x = 99
print(A.x)

# 3
class A:
    count = 0
    def __init__(self): A.count += 1
A(); A(); A()
print(A.count)

# 4
class A:
    def greet(self): return "hi"
print(A().greet())

# 5
class A:
    def __str__(self): return "I am A"
print(A())

# 6
class A:
    val = []
a1 = A(); a2 = A()
a1.val.append(1)
print(a2.val)

# 7
class A:
    @staticmethod
    def add(x, y): return x + y
print(A.add(3, 4))

# 8
class A:
    name = "generic"
    @classmethod
    def set_name(cls, n): cls.name = n
A.set_name("special")
print(A.name)

# 9
class A:
    def __init__(self, x): self.x = x
a = A(5)
a.x = 10
print(a.x)

# 10
class A:
    pass
a = A()
print(type(a).__name__)

# 11
class A:
    def __init__(self): self.items = []
a1 = A(); a2 = A()
a1.items.append(99)
print(a2.items)

# 12
class A:
    x = 10
    def __init__(self): self.x = 20
a = A()
print(a.x)
print(A.x)

# 13
class A:
    @staticmethod
    def hello(): return "hello"
a = A()
print(a.hello())

# 14
class A:
    def __init__(self, n): self.n = n
    def __str__(self): return str(self.n)
items = [A(1), A(2), A(3)]
print([str(i) for i in items])

# 15
class A:
    count = 0
    def __init__(self): self.count += 1
a = A()
print(A.count)
print(a.count)

# 16
class A:
    def method(self): return "method"
    @classmethod
    def cls(cls): return "cls"
    @staticmethod
    def stat(): return "stat"
a = A()
print(a.method(), a.cls(), a.stat())

# 17
class A:
    data = {}
a1 = A(); a2 = A()
a1.data["key"] = "val"
print(a2.data)

# 18
class A:
    def __init__(self, x): self.x = x
a = A(10)
b = a
b.x = 99
print(a.x)

# 19
class A:
    label = "A"
a = A()
A.label = "B"
print(a.label)

# 20
class A:
    def __repr__(self): return "A-repr"
    def __str__(self): return "A-str"
a = A()
print(a)
print(repr(a))

# 21
class A:
    x = 5
    def double(self): return self.x * 2
A.x = 3
a = A()
print(a.double())

# 22
class A:
    def __init__(self, name): self.name = name
    def __str__(self): return f"A({self.name})"
print(str(A("test")))

# 23
class A:
    total = 0
    def __init__(self):
        A.total += 1
    @classmethod
    def get_total(cls): return cls.total
A(); A()
print(A.get_total())

# 24
class A:
    pass
a = A()
a.new_attr = "dynamic"
print(hasattr(a, "new_attr"))
print(hasattr(A, "new_attr"))

# 25
class A:
    val = 0
a = A()
a.val = 10
del a.val
print(a.val)

# 26
class A:
    def __init__(self, x): self.x = x
a1 = A(1); a2 = A(1)
print(a1 == a2)

# 27
class A:
    @classmethod
    def who(cls): return cls.__name__
print(A.who())

# 28
class A:
    x = []
    def __init__(self): self.x = []
a1 = A(); a2 = A()
a1.x.append(1)
print(A.x)

# 29
class A:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return f"n={self.n}"
a = A(42)
a.n = 0
print(a)

# 30
class A:
    val = "class"
a = A()
print(a.val)
a.val = "instance"
print(a.val)
print(A.val)
```

### Answers — Layer C

| # | Answer |
|---|--------|
| 1 | `1` |
| 2 | `1` — instance attr shadows class attr, class attr unchanged |
| 3 | `3` |
| 4 | `hi` |
| 5 | `I am A` |
| 6 | `[1]` — mutable class attr shared |
| 7 | `7` |
| 8 | `special` |
| 9 | `10` |
| 10 | `A` |
| 11 | `[]` — instance attr (created in `__init__`) not shared |
| 12 | `20` then `10` |
| 13 | `hello` — static methods callable on instances too |
| 14 | `['1', '2', '3']` |
| 15 | `A.count = 0`; `a.count = 1` — `self.count += 1` makes an instance attr |
| 16 | `method cls stat` |
| 17 | `{'key': 'val'}` — mutable class attr dict is shared |
| 18 | `99` — same object, both names point to it |
| 19 | `B` — no instance attr, falls through to class attr |
| 20 | `A-str` then `A-repr` |
| 21 | `6` |
| 22 | `A(test)` |
| 23 | `2` |
| 24 | `True` then `False` — dynamic attr added to instance only |
| 25 | `0` — deleting instance attr reveals class attr underneath |
| 26 | `False` — no `__eq__` defined, compares by identity |
| 27 | `A` |
| 28 | `[]` — `self.x = []` in `__init__` creates instance attrs, `A.x` (class) untouched |
| 29 | `n=0` |
| 30 | `class` → `instance` → `class` |

**Pass: 27/30 correct, under 20 minutes, no notes.**

---

## Gate 1 — W3Schools Exercises

Complete these directly on W3Schools (open-book, but try from memory first):
- https://www.w3schools.com/python/exercise.asp?filename=exercise_classes1
- https://www.w3schools.com/python/exercise.asp?filename=exercise_inheritance1

Work through **all** exercises under: **Classes**, **Class Methods**, **Static Methods**.

---

## Gate 1 Complete ✓

When all three layers pass, put a `[x]` next to Gate 1 in `README.md` and move to Gate 2.
