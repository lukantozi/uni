"""
============================================================
Layer A
============================================================
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Current balance: {self.balance}"


class Student:
    student_count = 0
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.student_count += 1

    @classmethod
    def get_count(cls):
        return cls.student_count

    @staticmethod
    def passing_grade():
        return 60

    def passed(self):
        return self.grade >= self.passing_grade()


class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius

    def farenheit(self):
        return self.celcius * 9/5 + 32

    def __str__(self):
        return f"{self.celcius}C -> {self.farenheit()}F"


class Vehicle:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand
    def describe(self):
        return f"{self.brand} has {self.wheels} wheels"


def layer_a():
    # Task 1
    r1 = Rectangle(3, 5)
    r2 = Rectangle(6, 8)
    print(r1)
    print(r2)

    # Task 2
    ba = BankAccount(100)
    ba.deposit(10)
    print(ba)
    ba.withdraw(50)
    print(ba)

    # Task 3
    s1 = Student("John", 80)
    s2 = Student("Mia", 60)
    s3 = Student("Jack", 59)
    print(s3.student_count)
    print(Student.passing_grade())
    print(s2.passed())
    print(s3.passed())

    # Task 4
    t1 = Temperature(0)
    print(t1)
    t2 = Temperature(37)
    print(t2)
    t3 = Temperature(25)
    print(t3)

    # Task 5
    v = Vehicle("Toyota")
    Vehicle.wheels = 6
    print(v.describe()) # -> Toyota has 6 wheels
    print(Vehicle.wheels) # -> 6


"""
============================================================
Layer B
============================================================
"""
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)


class Car:
    total_cars = 0
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    @classmethod
    def reset_count(cls):
        cls.total_cars = 0

    @staticmethod
    def validate_speed(speed):
        return 0 < speed < 300


class Config:
    debug = False
    def __init__(self, debug):
        self.debug = debug


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name} - {self.price}zl"
    
    def __str__(self):
        return f"This {self.name} costs {self.price}"


def layer_b():
    # Task 1
    print("Task 1")
    d1 = Dog("Rex")
    d2 = Dog("Buddy")
    d1.add_trick("sit")
    d2.add_trick("spin")
    print(d1.tricks)
    print(d2.tricks)
    
    # Task 2
    print("Task 2")
    c1 = Car("BMW", "B5")
    c2 = Car("Audi", "A9")
    c3 = Car("Toyota", "R4")
    print(c1.total_cars)
    c2.reset_count()
    print(c2.validate_speed(50))
    print(Car.total_cars)

    # Task 3
    print("Task 3")
    print(Config.debug)
    con1 = Config(True)
    print(Config.debug)
    print(con1.debug)

    # Task 4
    print("Task 4")
    p1 = Product("Cola", 5)
    print(repr(p1))
    print(p1) # if __str__ not defined, it uses __repr__
