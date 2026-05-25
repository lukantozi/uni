# Gate 3 — Encapsulation & Dunder Methods
> Topics: private/protected attributes (`_x`, `__x`), name mangling, `@property`, setters/deleters,
> `__eq__`, `__lt__`, `__len__`, `__add__`, `__contains__`, `__getitem__`, `__repr__` vs `__str__`,
> `__call__`, `__bool__`, `__hash__`.

---

## Layer A — Skeleton (core rules)

### Predict-output drills

**1.**
```python
class Person:
    def __init__(self, name):
        self._name = name
p = Person("Alice")
print(p._name)
```

**2.**
```python
class Person:
    def __init__(self, name):
        self.__name = name
p = Person("Alice")
print(p.__name)
```

**3.**
```python
class Person:
    def __init__(self, name):
        self.__name = name
p = Person("Alice")
print(p._Person__name)
```

**4.**
```python
class Circle:
    def __init__(self, r):
        self._r = r
    @property
    def radius(self):
        return self._r
c = Circle(5)
print(c.radius)
```

**5.**
```python
class Circle:
    def __init__(self, r):
        self._r = r
    @property
    def radius(self):
        return self._r
    @radius.setter
    def radius(self, v):
        self._r = v
c = Circle(5)
c.radius = 10
print(c.radius)
```

**6.**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v = Vector(1, 2)
print(v)
print(repr(v))
```

**7.**
```python
class Box:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)
b = Box()
print(len(b))
```

**8.**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)
print(p1 == p3)
```

**9.**
```python
class Bag:
    def __init__(self, items):
        self.items = items
    def __contains__(self, item):
        return item in self.items
b = Bag(["apple", "banana", "cherry"])
print("banana" in b)
print("grape" in b)
```

**10.**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
```

**11.**
```python
class MyList:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]
m = MyList()
print(m)
```

**12.**
```python
class Counter:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count += 1
        return self.count
c = Counter()
print(c())
print(c())
print(c())
```

**13.**
```python
class MyNum:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        return self.val != 0
print(bool(MyNum(5)))
print(bool(MyNum(0)))
```

**14.**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32
t = Temperature(100)
print(t.fahrenheit)
```

**15.**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return self.x < other.x
p1 = Point(1, 5)
p2 = Point(3, 2)
print(p1 < p2)
```

---

### Answers — Layer A

| # | Answer |
|---|--------|
| 1 | `Alice` — `_x` is just convention, still accessible |
| 2 | `AttributeError` — `__name` is name-mangled |
| 3 | `Alice` — correct mangled access `_Person__name` |
| 4 | `5` |
| 5 | `10` |
| 6 | `Vector(1, 2)` then `Vector(1, 2)` — no `__str__`, print falls back to `__repr__` |
| 7 | `3` |
| 8 | `True` then `False` |
| 9 | `True` then `False` |
| 10 | `Vector(4, 6)` |
| 11 | `20` |
| 12 | `1` then `2` then `3` |
| 13 | `True` then `False` |
| 14 | `212.0` |
| 15 | `True` |

**Pass: __ /15 correct on first attempt, no running code.**

---

### Coding drills — Layer A

**1.** Create a `BankAccount` where `_balance` is protected. Add a `@property` getter and a setter that rejects negative values.

**2.** Create a `Vector2D` with `__add__`, `__repr__`, and `__eq__`. Show `Vector2D(1,2) + Vector2D(3,4)` and equality check.

**3.** Create a `Stack` with `__len__`, `__contains__`, `__getitem__`.

**4.** Create a callable `Multiplier(n)` class using `__call__` so `m(x)` returns `n * x`.

**5.** Create a `Password` class with `__password` (mangled). Show direct `obj.__password` fails; `obj._Password__password` works.

**Pass: All 5 drills correct on first run.**

---

## Layer B — Variants & gotchas

### Predict-output drills

**1.**
```python
class A:
    def __init__(self):
        self.__x = 10
a = A()
a.__x = 99
print(a.__x)
print(a._A__x)
```

**2.**
```python
class Celsius:
    def __init__(self, temp):
        self._temp = temp
    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self, value):
        if value < -273.15:
            raise ValueError("Too cold")
        self._temp = value
c = Celsius(25)
c.temp = -300
```

**3.**
```python
class A:
    def __init__(self, x):
        self.__x = x
    def get(self):
        return self.__x
class B(A):
    def get_b(self):
        return self.__x
b = B(5)
print(b.get())
print(b.get_b())
```

**4.**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(p1 is p2)
try:
    s = {p1, p2}
except TypeError:
    print("TypeError")
```

**5.**
```python
class MyStr:
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return f"MyStr({self.s!r})"
    def __str__(self):
        return self.s
m = MyStr("hello")
print(m)
print(repr(m))
print([m])
```

**6.**
```python
class Box:
    def __init__(self, val):
        self._val = val
    @property
    def val(self):
        return self._val
b = Box(10)
b.val = 20
```

**7.**
```python
class A:
    def __init__(self, x):
        self.__x = x
class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.__y = y
    def show(self):
        return self._A__x, self.__y
b = B(1, 2)
print(b.show())
```

**8.**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"({self.x},{self.y})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
v3 = Vector(1, 2) + Vector(3, 4)
print(v3)
print(v3 == Vector(4, 6))
```

**9.**
```python
class MyList:
    def __init__(self, data):
        self._data = data
    def __len__(self):
        return len(self._data)
    def __bool__(self):
        return len(self._data) > 0
m1 = MyList([])
m2 = MyList()
print(bool(m1))
print(bool(m2))
print(len(m2))
```

**10.**
```python
class Counter:
    def __init__(self):
        self._n = 0
    def __call__(self, step=1):
        self._n += step
        return self._n
    def __repr__(self):
        return f"Counter({self._n})"
c = Counter()
c(); c(); c(5)
print(c)
```

**11.**
```python
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __contains__(self, item):
        return self.start <= item < self.end
r = Range(1, 10)
print(5 in r)
print(10 in r)
print(0 in r)
```

**12.**
```python
class A:
    def __init__(self, n):
        self._n = n
    @property
    def n(self):
        return self._n
    @n.setter
    def n(self, val):
        self._n = val * 2
a = A(3)
print(a.n)
a.n = 5
print(a.n)
```

**13.**
```python
class A:
    def __init__(self, x):
        self.__x = x
a = A(10)
print(vars(a))
```

**14.**
```python
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __iter__(self):
        return iter([self.a, self.b])
    def __repr__(self):
        return f"Pair({self.a}, {self.b})"
p = Pair(10, 20)
x, y = p
print(x, y)
print(list(p))
```

---

### Answers — Layer B

| # | Answer |
|---|--------|
| 1 | `99` then `10` — `a.__x = 99` creates a new instance attr; `_A__x` is the original mangled one |
| 2 | `ValueError: Too cold` |
| 3 | `5` then `AttributeError` — in `B`, `self.__x` mangles to `_B__x`, not `_A__x` |
| 4 | `True` then `False` then `TypeError` — `__eq__` without `__hash__` makes unhashable |
| 5 | `hello` then `MyStr('hello')` then `[MyStr('hello')]` — list repr uses `__repr__` of elements |
| 6 | `AttributeError: can't set attribute` — property has no setter |
| 7 | `(1, 2)` |
| 8 | `(4,6)` then `True` |
| 9 | `False` then `True` then `2` |
| 10 | `Counter(7)` — `1+1+5 = 7` |
| 11 | `True` then `False` then `False` — end is exclusive |
| 12 | `3` then `10` — setter doubles: `5 * 2` |
| 13 | `{'_A__x': 10}` |
| 14 | `10 20` then `[10, 20]` |

**Pass: __ /14 correct, no notes.**

---

### Coding drills — Layer B

**1.** Show the `__eq__` breaks hashing gotcha: define `__eq__` on a class, put two equal instances in a set — show `TypeError`. Then fix it by implementing `__hash__`.

**2.** Write `PrivateCounter` with `__count` mangled. Try `self.__count` from a subclass, show the error, fix with the mangled name.

**3.** Write a `Temperature` class with a `celsius` property (with setter + `ValueError` guard) and a computed read-only `fahrenheit` property.

**4.** Write `Matrix1D` with `__len__`, `__getitem__`, `__setitem__`, `__contains__`, `__repr__`.

**Pass: All 4 drills correct.**

---

## Layer C — Speed Run

30 questions. Paper first, no code, target under 20 minutes.

```python
# 1
class A:
    def __init__(self):
        self._x = 1
a = A()
print(a._x)

# 2
class A:
    def __init__(self):
        self.__x = 1
a = A()
print(a.__x)

# 3
class A:
    def __init__(self):
        self.__x = 1
a = A()
print(a._A__x)

# 4
class A:
    def __init__(self):
        self.__x = 10
a = A()
a.__x = 99
print(a.__x)
print(a._A__x)

# 5
class C:
    def __init__(self, v):
        self._v = v
    @property
    def v(self):
        return self._v
c = C(42)
print(c.v)

# 6
class C:
    def __init__(self, v):
        self._v = v
    @property
    def v(self):
        return self._v
c = C(42)
c.v = 99

# 7
class C:
    def __init__(self, v):
        self._v = v
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, val):
        self._v = val
c = C(1)
c.v = 5
print(c.v)

# 8
class A:
    def __repr__(self): return "repr"
    def __str__(self): return "str"
a = A()
print(a)
print(repr(a))

# 9
class A:
    def __repr__(self): return "repr"
a = A()
print(a)
print(str(a))

# 10
class A:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)
a = A()
print(len(a))

# 11
class A:
    def __init__(self, items):
        self.items = items
    def __contains__(self, x):
        return x in self.items
a = A()
print(2 in a)
print(5 in a)

# 12
class A:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
a1 = A(5)
a2 = A(5)
print(a1 == a2)
print(a1 is a2)

# 13
class V:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return V(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"V({self.x},{self.y})"
print(V(1, 2) + V(3, 4))

# 14
class A:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, i):
        return self.data[i]
a = A()
print(a)

# 15
class A:
    def __call__(self, x):
        return x * 2
a = A()
print(a(5))

# 16
class A:
    def __init__(self, n):
        self.n = n
    def __bool__(self):
        return self.n > 0
print(bool(A(3)))
print(bool(A(-1)))
print(bool(A(0)))

# 17
class A:
    def __init__(self, x):
        self.x = x
    def __lt__(self, other):
        return self.x < other.x
items = [A(3), A(1), A(2)]
print(sorted(items, key=lambda a: a.x).x)

# 18
class A:
    def __init__(self, x):
        self.__x = x
print(vars(A(5)))

# 19
class A:
    def __init__(self, x):
        self._x = x
class B(A):
    def get(self):
        return self._x
print(B(99).get())

# 20
class A:
    def __init__(self, x):
        self.__x = x
class B(A):
    def get(self):
        return self.__x
print(B(5).get())

# 21
class A:
    def __init__(self, items):
        self._items = items
    def __iter__(self):
        return iter(self._items)
a = A()
print(list(a))

# 22
class A:
    def __init__(self, n):
        self._n = n
    @property
    def n(self):
        return self._n
    @n.setter
    def n(self, v):
        self._n = v * 2
a = A(3)
a.n = 4
print(a.n)

# 23
class A:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
a = A(1)
b = A(1)
try:
    s = {a, b}
    print(len(s))
except TypeError:
    print("TypeError")

# 24
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __iter__(self):
        return iter([self.x, self.y])
x, y = A(3, 7)
print(x, y)

# 25
class A:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return f"A({self.n})"
items = [A(1), A(2), A(3)]
print(items)

# 26
class A:
    def __init__(self):
        self.__x = 10
a = A()
a.__x = 99
print(vars(a))

# 27
class C:
    def __init__(self):
        self._count = 0
    def __call__(self):
        self._count += 1
    def __repr__(self):
        return f"C({self._count})"
c = C()
c(); c(); c()
print(c)

# 28
class A:
    def __init__(self, x):
        self._x = x
    @property
    def x(self):
        return self._x
    @x.deleter
    def x(self):
        del self._x
a = A(5)
del a.x
print(hasattr(a, '_x'))

# 29
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    def __hash__(self):
        return hash((self.a, self.b))
s = {A(1, 2), A(1, 2), A(3, 4)}
print(len(s))

# 30
class A:
    def __init__(self, x):
        self.__x = x
    def __repr__(self):
        return f"A({self.__x})"
a = A(42)
print(a)
print(a._A__x)
```

### Answers — Layer C

| # | Answer |
|---|--------|
| 1 | `1` |
| 2 | `AttributeError` |
| 3 | `1` |
| 4 | `99` then `10` |
| 5 | `42` |
| 6 | `AttributeError: can't set attribute` |
| 7 | `5` |
| 8 | `str` then `repr` |
| 9 | `repr` then `repr` |
| 10 | `4` |
| 11 | `True` then `False` |
| 12 | `True` then `False` |
| 13 | `V(4,6)` |
| 14 | `30` |
| 15 | `10` |
| 16 | `True` then `False` then `False` |
| 17 | `1` |
| 18 | `{'_A__x': 5}` |
| 19 | `99` |
| 20 | `AttributeError` |
| 21 | `[1, 2, 3]` |
| 22 | `8` |
| 23 | `TypeError` |
| 24 | `3 7` |
| 25 | `[A(1), A(2), A(3)]` |
| 26 | `{'_A__x': 10, '__x': 99}` |
| 27 | `C(3)` |
| 28 | `False` |
| 29 | `2` |
| 30 | `A(42)` then `42` |

**Pass: 27/30 correct, under 20 minutes.**
