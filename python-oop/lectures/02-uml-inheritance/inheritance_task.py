class Animal:
    number_of_animals = 0
    def __init__(self, name, color, legs):
        self.name = name
        self.color = color
        self.legs = legs
        Animal.number_of_animals += 1
    
    @classmethod
    def how_many(cls):
        #print(f"There have been {cls.number_of_animals} animals created")
        return cls.number_of_animals

    def description(self):
        print(f"Name: {self.name}\nColor: {self.color}\nLegs: {self.legs}")


class Bird(Animal):
    number_of_birds = 0
    def __init__(self, name, color):
        super().__init__(name, color, 2)
        Bird.number_of_birds += 1


class Mammal(Animal):
    number_of_mammals = 0
    def __init__(self, name, color, legs=-1):
        super().__init__(name, color, legs)
        Mammal.number_of_mammals += 1


class Fish(Animal):
    number_of_fish = 0
    def __init__(self, name, color):
        super().__init__(name, color, 0)
        Fish.number_of_animals += 1


class Dog(Mammal):
    number_of_dogs = 0
    def __init__(self, name, color):
        super().__init__(name, color, 4)
        Dog.number_of_dogs += 1

    @classmethod
    def info(cls):
        print(f"There have been {cls.number_of_dogs} dogs created")
        print(f"There have been {cls.how_many()} animals created")


class Cat(Mammal):
    number_of_cats = 0
    def __init__(self, name, color):
        super().__init__(name, color, 4)
        Cat.number_of_animals += 1


cat = Cat("malwinka", "orange")
print(cat.name)
fish = Fish("jub", "yellow")
print(fish.color)
dog = Dog("jack", "white")
dog.info()
print(Dog.__mro__)
dog.description()
animal = Animal("name", "color", 2)
animal.how_many()
