"""
============================================================
Layer A

4. Create a callable Multiplier(n) class using __call__ so m(x) returns n * x.

5. Create a Password class with __password (mangled). Show direct obj.__password fails; obj._Password__password works.

Pass: All 5 drills correct on first run.
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

"""
3. Create a Stack with __len__, __contains__, __getitem__.
"""
class Stack:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, ind):
        if 0 < ind < len(self) - 1:
            return self.items[ind]
        raise ValueError("Wrong index")

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

    task_3()

layer_a()
