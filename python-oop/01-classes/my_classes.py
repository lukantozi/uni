class Cars:
    count = 0
    def __init__(self, brand, model, year, max_speed, n_plates):
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.velocity = 0
        self.colour = None
        self.n_plates = n_plates
        Cars.count += 1

    def __str__(self):
        return f"Brand: {self.brand}. Model: {self.model}. Year of production: {self.year}. Colour: {self.colour}"
    
    @classmethod
    def desc(cls):
        print(f"This is car class. Currently there is {cls.count}")

    @property
    def n_plates(self):
        return self.n_plates

    @n_plates.setter
    def n_plates(self, plates):
        if (len(str(plates)) != 6 and plates.isnumeric()):
            raise Exception("Number should be six numbers")
        self._n_plates = str(plates)

    def change_color(self, color):
        self.colour = color

    def run(self):
        self.velocity = 0.75 * self.velocity
        print(f"New speed: {self.velocity}")

    def stop(self):
        self.velocity = 0
        print(f"New speed: {self.velocity}")


class Dealer:
    def __init__(self, name, car_brand):
        self.name = name
        self.car_brand = car_brand
        self.car_list = []

    def __str__(self):
        cars = [f"{car.brand}: {car.model}"for car in self.car_list]
        car_details = [f"{(vars(details))}\n" for details in self.car_list]
        return f"The car dealer {self.name} has following cars: {cars}\nCar details:\n{car_details}"

    def add_car(self, car):
        self.car_list.append(car)


car_1 = Cars("merc", "s500", 2000, 150, 123456)
car_2 = Cars("merc", "e200", 2001, 160, 343235)
car_3 = Cars("merc", "c63", 2011, 220, 300134)

print(list(vars(car_1).values()))
car_2.change_color("red")
car_2.velocity = 200
car_2.run()
print(car_2.colour)
car_2.stop()

print(car_3)
car_3.desc()

car_4 = Cars("bmw", "y500", 2000, 150, 290044)
car_5 = Cars("bmw", "u321", 2010, 160, 405553)
car_6 = Cars("bmw", "i899", 2014, 170, 123123)

car_7 = Cars("honda", "sk100", 2000, 150, 412389)
car_8 = Cars("honda", "sk200", 2004, 160, 481841)
car_9 = Cars("honda", "sk300", 2009, 180, 819126)
car_10 = Cars("honda", "sk400", 2015, 210, 848191)

dealer = Dealer("dealer_name", "honda")
dealer.add_car(car_7)
dealer.add_car(car_8)
print(dealer)
