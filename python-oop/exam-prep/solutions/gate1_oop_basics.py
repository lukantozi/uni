class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

r1 = Rectangle(3, 5)
r2 = Rectangle(6, 8)
print(r1)
print(r2)

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

ba = BankAccount(100)
ba.deposit(10)
print(ba)
ba.withdraw(50)
print(ba)

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

s1 = Student("John", 80)
s2 = Student("Mia", 60)
s3 = Student("Jack", 59)
print(s3.student_count)
print(Student.passing_grade())
print(s2.passed())
print(s3.passed())

class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius

    def farenheit(self):
        return self.celcius * 9/5 + 32

    def __str__(self):
        return f"{self.celcius}C -> {self.farenheit()}F"

t1 = Temperature(0)
print(t1)
t2 = Temperature(37)
print(t2)
t3 = Temperature(25)
print(t3)

class Vehicle:
    wheels = 4
    def __init__(self, brand):
        self.brand = brand
    def describe(self):
        return f"{self.brand} has {self.wheels} wheels"

v = Vehicle("Toyota")
Vehicle.wheels = 6
print(v.describe()) # -> Toyota has 6 wheels
print(Vehicle.wheels) # -> 6
