class Car:
    runs = True
    no_of_wheels = 4

    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    @classmethod
    def get_no_of_wheels(cls):
        print(f"Car has {cls.no_of_wheels} wheels")

    # self is implicitly passed when the method is invoked by the instance
    def start(self):
        if self.runs:
            print(f"{self.make} {self.model} is started. Vroom vroom!")
        else:
            print(f"{self.make} {self.model} is broken :(")


my_car = Car("Honda", "City")
# print(dir(my_car))

print(f"My car runs: {my_car.runs}")
my_car.start()
my_car.get_no_of_wheels()

Car.get_no_of_wheels()
Car.no_of_wheels = 6
my_car.get_no_of_wheels()

my_car.no_of_wheels = 10
my_car.get_no_of_wheels()
Car.get_no_of_wheels()
