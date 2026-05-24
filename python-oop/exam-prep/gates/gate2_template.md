# Gate 2 — Inheritance
> Topics: inheritance idea and implementation in Python, parent vs child class,
> `super()`, method overriding, `isinstance()`, `issubclass()`, multi‑level
> inheritance, polymorphism.

---

## Layer A — Skeleton (core rules)

### Predict‑output drills

**1.**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

d = Dog("Rex")
print(d.name)
```

**2.**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

d = Dog("Rex")
print(d.speak())
```

**3.**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    pass

d = Dog("Rex")
print(d.speak())
```

**4.**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

s = Student("Alice", 20, "A")
print(s.name)
print(s.grade)
```

**5.**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

s = Student("Alice", 20, "A")
print(isinstance(s, Student))
print(isinstance(s, Person))
```

**6.**
```python
class A:
    pass

class B(A):
    pass

print(issubclass(B, A))
print(issubclass(A, B))
```

**7.**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f"I am {self.name}"

class Cat(Animal):
    def describe(self):
        return f"I am a cat named {self.name}"

c = Cat("Whiskers")
print(c.describe())
```

**8.**
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"Vehicle: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

c = Car("BMW", "X5")
print(c)
```

**9.**
```python
class A:
    def hello(self):
        return "Hello from A"

class B(A):
    pass

class C(B):
    pass

obj = C()
print(obj.hello())
```

**10.**
```python
class Animal:
    number_of_animals = 0
    def __init__(self, name):
        self.name = name
        Animal.number_of_animals += 1

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog("Rex")
c = Cat("Whiskers")
print(Animal.number_of_animals)
```

**11.**
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def __str__(self):
        return f"{self.name} - {self.grade}"

s = Student("Bob", "B+")
print(s)
```

**12.**
```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for s in shapes:
    print(s.area())
```

**13.**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Labrador")
print(type(d).__name__)
print(isinstance(d, Animal))
```

**14.**
```python
class A:
    x = "A"

class B(A):
    pass

class C(A):
    x = "C"

print(B.x)
print(C.x)
```

**15.**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says ..."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

animals = [Dog("Rex"), Cat("Whiskers"), Animal("Unknown")]
for a in animals:
    print(a.speak())
```

---

### Answers — Layer A

| #  | Answer |
|----|--------|
| 1  | `Rex` |
| 2  | `Woof` |
| 3  | `...` |
| 4  | `Alice` then `A` |
| 5  | `True` then `True` |
| 6  | `True` then `False` |
| 7  | `I am a cat named Whiskers` |
| 8  | `Vehicle: BMW` |
| 9  | `Hello from A` |
| 10 | `2` |
| 11 | `Bob - B+` |
| 12 | `78.5` then `16` |
| 13 | `Dog` then `True` |
| 14 | `A` then `C` |
| 15 | `Rex says Woof` / `Whiskers says Meow` / `Unknown says ...` |

**Pass: 13/15 correct on first attempt, no running code.**

---

### Coding drills — Layer A

1. Recreate the Animal/Bird/Mammal/Fish/Dog/Cat hierarchy from your list 2: one base class `Animal`, intermediate classes `Bird`, `Fish`, `Mammal`, and `Dog`/`Cat` as children of `Mammal`. Use a constructor design so that all share `name` and `colour`, and `number_of_legs` is set appropriately in each subclass.
2. Add per‑class counters `number_of_animals`, `number_of_birds`, `number_of_mammals`, `number_of_dogs`, `number_of_cats`. Show that creating instances increments both the base and the specific subclass counter.
3. Implement an `info()` method (once, in a sensible class) that prints `name`, `colour`, and `number_of_legs` for any of the five subclasses, using inheritance to avoid duplication.
4. Implement a `Person → Student` example where `Student` properly uses `super().__init__` and has an extra `grade` attribute. Add `__str__` and show a list of mixed `Person` and `Student` objects being printed.
5. Implement a `Shape` base class and `Circle`/`Rectangle` with overridden `area()` to demonstrate polymorphism. Create a list of shapes and print `area()` for each.

**Pass: all 5 drills work correctly, first run.**

---

## Layer B — Variants & gotchas

### Predict‑output drills

**1.**
```python
class A:
    def __init__(self):
        self.x = "A"

class B(A):
    def __init__(self):
        self.y = "B"

b = B()
print(b.y)
print(b.x)
```

**2.**
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(B):
    pass

print(C().method())
```

**3.**
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        result = super().method()
        return f"B -> {result}"

print(B().method())
```

**4.**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        parent = super().speak()
        return f"Woof (parent said: {parent})"

d = Dog("Rex")
print(d.speak())
```

**5.**
```python
class A:
    def __init__(self):
        self.x = 1
        self.setup()
    def setup(self):
        pass

class B(A):
    def setup(self):
        self.y = 2

b = B()
print(b.x)
print(b.y)
```

**6.**
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

class GradStudent(Student):
    def __init__(self, name, grade, thesis):
        super().__init__(name, grade)
        self.thesis = thesis

g = GradStudent("Alice", "A", "OOP in Python")
print(g.name)
print(g.grade)
print(g.thesis)
print(isinstance(g, Person))
```

**7.**
```python
class A:
    class_var = "A"

class B(A):
    pass

b = B()
b.class_var = "B-instance"
print(B.class_var)
print(b.class_var)
```

**8.**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Animal: {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Labrador")
print(d)
```

**9.**
```python
class A:
    def greet(self):
        return f"Hello from {type(self).__name__}"

class B(A):
    pass

print(B().greet())
```

**10.**
```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

class SpecialCounter(Counter):
    pass

Counter()
SpecialCounter()
SpecialCounter()
print(Counter.count)
print(SpecialCounter.count)
```

**11.**
```python
class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    def total(self):
        return self.x + self.y

b = B(3, 4)
print(b.total())
print(issubclass(type(b), A))
```

**12.**
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def describe(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def describe(self):
        return f"{super().describe()}, Model: {self.model}"

c = Car("Toyota", "Corolla")
print(c.describe())
```

**13.**
```python
class A:
    def __init__(self):
        self.value = self.default()
    def default(self):
        return 0

class B(A):
    def default(self):
        return 42

b = B()
print(b.value)
```

**14.**
```python
class Animal:
    legs = 4
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    legs = 2

class Dog(Animal):
    pass

print(Dog.legs)
print(Bird.legs)
b = Bird("Tweety")
print(b.legs)
print(isinstance(b, Animal))
```

---

### Answers — Layer B

| #  | Answer |
|----|--------|
| 1  | `B` then `AttributeError` — `B.__init__` never calls `super()`, so `x` is not set |
| 2  | `B` |
| 3  | `B -> A` |
| 4  | `Woof (parent said: …)` |
| 5  | `1` then `2` — `B.setup()` called polymorphically from `A.__init__` |
| 6  | `Alice` / `A` / `OOP in Python` / `True` |
| 7  | `A` then `B-instance` — class attr unchanged, instance attr shadows it |
| 8  | `Animal: Rex` |
| 9  | `Hello from B` |
| 10 | `3` then `3` — same shared class attr `count` |
| 11 | `7` then `True` |
| 12 | `Brand: Toyota, Model: Corolla` |
| 13 | `42` |
| 14 | `4` / `2` / `2` / `True` |

**Pass: 12/14 correct, no notes.**

---

### Coding drills — Layer B

1. Rewrite drill B‑1 properly: fix `B.__init__` to call `super().__init__()`, prove that `b.x` now exists, and explain in a short comment why missing `super()` is dangerous in inheritance chains.
2. Build a `Vehicle → Car → ElectricCar` chain where each `describe()` uses `super().describe()` and adds one more detail (brand → brand+model → brand+model+range). Show the final `describe()` output.
3. Implement the Animal counters with `Animal.number_of_animals`, `Dog.number_of_dogs`, etc., and print all counters after creating multiple animals, verifying that subclass and base counters behave as expected.
4. Implement the `default()` overriding example (`A` with `default() = 0`, `B` overriding `default() = 42`) and add a second subclass `C` that returns `-1`. Show the values of `B().value` and `C().value` and explain how runtime method resolution works.

---

## Layer C — Speed run

Exactly 30 questions, matching the JSON I gave you, for timed practice. Answer everything on paper first, no running code, target under 20 minutes.

```python
# 1
class A:
    def hello(self): return "A"
class B(A): pass
print(B().hello())

# 2
class A:
    def hello(self): return "A"
class B(A):
    def hello(self): return "B"
print(B().hello())

# 3
class A:
    x = 10
class B(A): pass
print(B.x)

# 4
class A:
    def __init__(self): self.x = 1
class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2
b = B()
print(b.x, b.y)

# 5
class A:
    def __init__(self): self.x = 1
class B(A):
    def __init__(self): self.y = 2
b = B()
print(b.y)
print(b.x)

# 6
class A: pass
class B(A): pass
class C(B): pass
print(issubclass(C, A))

# 7
class A: pass
class B(A): pass
obj = B()
print(isinstance(obj, A))
print(isinstance(obj, B))

# 8
class A:
    def method(self): return "A"
class B(A):
    def method(self): return super().method() + "B"
print(B().method())

# 9
class Animal:
    def __init__(self, name): self.name = name
    def __str__(self): return f"Animal({self.name})"
class Dog(Animal): pass
print(Dog("Rex"))

# 10
class A:
    count = 0
    def __init__(self): A.count += 1
class B(A): pass
A(); B(); B()
print(A.count)

# 11
class A:
    def greet(self): return f"I am {type(self).__name__}"
class B(A): pass
print(B().greet())

# 12
class Shape:
    def area(self): return 0
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2
print(Circle(1).area())

# 13
class A:
    x = "class_A"
class B(A):
    x = "class_B"
class C(B): pass
print(C.x)

# 14
class A:
    def __init__(self, n): self.n = n
class B(A):
    def __init__(self, n, m):
        super().__init__(n)
        self.m = m
b = B(1, 2)
print(b.n, b.m)

# 15
class A: pass
class B(A): pass
print(issubclass(A, B))
print(issubclass(B, A))

# 16
class Animal:
    def speak(self): return "..."
class Dog(Animal):
    def speak(self): return "Woof"
class Cat(Animal):
    def speak(self): return "Meow"
for a in [Dog(), Cat(), Animal()]:
    print(a.speak())

# 17
class A:
    def __init__(self): self.val = self.get_val()
    def get_val(self): return 0
class B(A):
    def get_val(self): return 99
print(B().val)

# 18
class A:
    def method(self): return "A"
class B(A):
    def method(self): return "B"
class C(A):
    def method(self): return "C"
class D(B, C): pass
print(D().method())

# 19
class Vehicle:
    def __init__(self, brand): self.brand = brand
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
c = Car("BMW", "X5")
print(isinstance(c, Vehicle))
print(type(c).__name__)

# 20
class A:
    label = "A"
class B(A): pass
b = B()
B.label = "B"
print(b.label)
print(A.label)

# 21
class A:
    def __str__(self): return "A"
class B(A):
    pass
print(B())

# 22
class A:
    def __init__(self, x): self.x = x
class B(A):
    def double(self): return self.x * 2
b = B(5)
print(b.double())

# 23
class A: pass
class B(A): pass
class C(B): pass
obj = C()
print(isinstance(obj, A))
print(issubclass(C, A))

# 24
class A:
    def method(self): return "A"
class B(A):
    def method(self):
        return super().method() + "+B"
class C(B):
    def method(self):
        return super().method() + "+C"
print(C().method())

# 25
class Animal:
    number = 0
    def __init__(self): Animal.number += 1
class Dog(Animal):
    number = 0
    def __init__(self):
        super().__init__()
        Dog.number += 1
Dog(); Dog()
print(Animal.number)
print(Dog.number)

# 26
class A:
    def __init__(self, x): self.x = x
    def __str__(self): return f"A({self.x})"
class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    def __str__(self): return f"B({self.x},{self.y})"
print(B(1, 2))

# 27
class A:
    val = []
class B(A): pass
B.val.append(1)
print(A.val)

# 28
class Person:
    def __init__(self, name): self.name = name
class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa
s = Student("Alice", 4.0)
print(s.name, s.gpa)

# 29
class A:
    def method(self): return "A"
class B(A): pass
class C(B):
    def method(self): return "C"
print(C().method())
print(B().method())

# 30
class Base:
    def info(self): return "Base"
class Mid(Base):
    def info(self): return f"Mid->{super().info()}"
class Top(Mid):
    def info(self): return f"Top->{super().info()}"
print(Top().info())
```

### Answers — Layer C

| #  | Answer                    |
|----|---------------------------|
| 1  | A                         |
| 2  | B                         |
| 3  | 10                        |
| 4  | 1 2                       |
| 5  | 2 then AttributeError     |
| 6  | True                      |
| 7  | True then True            |
| 8  | AB                        |
| 9  | Animal(Rex)               |
| 10 | 3                         |
| 11 | I am B                    |
| 12 | 3.14                      |
| 13 | class_B                   |
| 14 | 1 2                       |
| 15 | False then True           |
| 16 | Woof / Meow / ...         |
| 17 | 99                        |
| 18 | B                         |
| 19 | True then Car             |
| 20 | B then A                  |
| 21 | A                         |
| 22 | 10                        |
| 23 | True then True            |
| 24 | A+B+C                     |
| 25 | 2 then 2                  |
| 26 | B(1,2)                    |
| 27 | [1]                       |
| 28 | Alice 4.0                 |
| 29 | C then A                  |
| 30 | Top->Mid->Base            |

**Pass: 27/30 correct, under 20 minutes, no notes.**

---
