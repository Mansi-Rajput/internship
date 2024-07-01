class Bike:
    def start_engine(self):
        print("Bike engine started")

# Create a Bike object
my_bike = Bike()

# Call the start_engine method
my_bike.start_engine()


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def start_engine(self):
        print("Car engine started")

    def display_info(self):
        print(f"Car: {self.model}, Color: {self.color}")

# Create a Car object
my_car = Car("blue", "Toyota")

# Call the start_engine method
my_car.start_engine()

# Call the display_info method
my_car.display_info()

def start_vehicle(vehicle):
    vehicle.start_engine()

# Define a Bike class
class Bike:
    def start_engine(self):
        print("Bike engine started")

# Define a Car class
class Car:
    def start_engine(self):
        print("Car engine started")

# Create a Bike object
my_bike = Bike()

# Create a Car object
my_car = Car()

# Call the start_vehicle function with a Bike object
start_vehicle(my_bike)

# Call the start_vehicle function with a Car object
start_vehicle(my_car)