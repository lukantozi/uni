class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades


class Professor(Person):
    pass


student1 = Student("Luka", 24, [1, 1])
