"""
============================================================
Layer A
============================================================
"""
# Task 1
class BankAccount:
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, b):
        if (not (isinstance(b, (int, float)))) or b < 0:
            raise ValueError("Only non-negative values allowed")
        self._balance = b


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return self.__class__(newx, newy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


class Stack:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, ind):
        if 0 <= ind < len(self):
            return self.items[ind]
        raise ValueError("Wrong index")


class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, m):
        return self.n * m


class Password:
    def __init__(self, password):
        self.__password = password


"""
============================================================
Layer B
============================================================
Coding drills — Layer B


Pass: All 4 drills correct.
"""
class Equal:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return id(self)


class PrivateCounter:
    def __init__(self):
        self.__count = 0

    def __call__(self, size=1):
        self.__count += size


class SubCounterShow(PrivateCounter):
    def show_broken(self):
        return self.__count

    def show(self):
        return self._PrivateCounter__count


class Temperature:
    def __init__(self, c):
        self.celsius = c

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, c):
        if not isinstance(c, (int, float)):
            raise ValueError("Please enter a number")
        self._celsius = c

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class Matrix1D:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, ind):
        if not (0 <= ind < len(self.items)):
            raise ValueError("Index out of range")
        return self.items[ind]

    def __setitem__(self, ind, item):
        if not (0 <= ind < len(self.items)):
            raise ValueError("Index out of range")
        self.items[ind] = item

    def __contains__(self, item):
        return item in self.items
    
    def __repr__(self):
        return f"Matrix1D({self.items})"


"""
============================================================
Test implementations
============================================================
"""
def layer_a():
    def task_1():
        ba = BankAccount("user", 1.0)
        bb = BankAccount("user", 100)
        print(ba.balance)
        print(bb.balance)

    def task_2():
        v1 = Vector2D(3, 4)
        v2 = Vector2D(4, 2)
        v3 = Vector2D(4, 2)
        print(v1 + v2)
        print(v1 == v2)
        print(v2 == v3)

    def task_3():
        s = Stack([2, 4, 6, 9])
        print(len(s))
        print(6 in s)

    def task_4():
        m = Multiplier(5)
        print(m(3))

    def task_5():
        p = Password(12345)
        try:
            print(p.__password)
        except AttributeError:
            print("Can't access directly")
        print(p._Password__password)


def layer_b():
    def task_1():
        e = Equal(5)
        e1 = Equal(5)
        print(e == e1)
        s = {e, e1}
        print(s)

    def task_2():
        c = SubCounterShow()
        c(); c(); c()
        print(c.show())
        print(c.show_broken())

    def task_3():
        t = Temperature("s")
        t.celsius = 123
        print(t.celsius)
        print(t.fahrenheit)

    def task_4():
        m = Matrix1D([3, 4, 5])
        print(len(m))
        print(m[2])
        m[6] = 4
        print(m)
        print(4 in m)
        print(8 in m)
