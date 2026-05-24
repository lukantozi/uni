"""
============================================================
Layer A
============================================================
"""

# Task 1-2-3 (original version from homework)
class Animal:
    animal_count = 0
    def __init__(self, name, color, legs):
        self.name = name
        self.color = color
        self.legs = legs
        Animal.animal_count += 1

    @classmethod
    def how_many_animals(cls):
        print(f"{cls.animal_count} animal(s) created")

    def description(self):
        print(f"Name: {self.name}\nColor: {self.color}\nLegs: {self.legs}")


class Mammal(Animal):
    mammal_count = 0
    def __init__(self, name, color, legs=-1):
        super().__init__(name, color, legs)
        Mammal.mammal_count += 1


class Bird(Animal):
    bird_count = 0
    def __init__(self, name, color):
        super().__init__(name, color, legs=2)
        Bird.bird_count += 1


class Fish(Animal):
    fish_count = 0
    def __init__(self, name, color):
        super().__init__(name, color, legs=0)
        Fish.fish_count += 1


class Cat(Mammal):
    cat_count = 0
    def __init__(self, name, color):
        super().__init__(name, color, legs=4)
        Cat.cat_count += 1



class Dog(Mammal):
    dog_count = 0
    def __init__(self, name, color):
        super().__init__(name, color, legs=4)
        Dog.dog_count += 1

    @classmethod
    def info(cls):
        print(f"{cls.dog_count} dog(s) created")
        Animal.how_many_animals()


# Task 4
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person named {self.name}"


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def __str__(self):
        return f"Student {self.name} received {self.grade}"


# Task 5
class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


# Test layer a implementations
def layer_a():
    def task_123():
        d1 = Dog("Jack", "grey")
        d1.info()
        d1.description()
        print(Cat("H", "s").cat_count)
        print(Animal.animal_count)
        b1 = Bird("p", "r")
        b1.description()

    def task_4():
        people = [Student("Josh", "B"), Person("Rick"), Person("Ross"), Student("Joey", "A")]
        for p in people:
            print(p)

    def task_5():
        figs = [Circle(5), Square(4), Shape()]
        for f in figs:
            print(f.area())
