#### Task 1 ####
# Define a class Car with attributes make, model, and year.
# Create an instance of the Car class.
# Add a method display_info that prints out the details of the car.

class Car:
    def __init__(self, make, model, year):
        """Initializes instance attributes"""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """This is an instance method which is used to display info"""
        print(f"The Car's details are:\n Make: {self.make}\n Model: {self.model}\n Year: {self.year}")

#object creation
car_obj = Car("Toyota", "Corolla", 2020)
#calling method using object reference
car_obj.display_info()

#### Task 2 ####
# Define a class ElectricCar that inherits from the Car class.
# Add an attribute battery_size to the ElectricCar class.
# Override the display_info method to include battery size.

class Car:
    def __init__(self, make, model, year):
        """Initializes instance attributes"""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """This is an instance method which is used to display info"""
        print(f"The Car's details are:\n Make: {self.make}\n Model: {self.model}\n Year: {self.year}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        """Initializes instance attributes"""
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        """Overridden Method to display onfo"""
        super().display_info()
        print(f" Battery size: {self.battery_size} kWh")

#object creation
ecarobj = ElectricCar("Tesla", "Model S", 2022, 100)
#calling method using object reference
ecarobj.display_info()

#### Task 3 ####
# Define a class Bike with a method start_engine that prints "Bike engine started".
# Add a method start_engine to the Car class that prints "Car engine started".
# Write a function start_vehicle that takes a vehicle object and calls its start_engine method.

class Bike:
    def start_engine(self):
        print("Bike engine started.")
        
class Car(Bike):
    def start_engine(self):
        print("Car engine started.")

def start_vehicle(vehicle):
    """function used to call a method using 
    object reference given as an argument"""
    vehicle.start_engine()

my_bike = Bike()
my_car = Car()

start_vehicle(my_bike)
start_vehicle(my_car)

#### Task 4 ####
# Modify the Car class to make the make, model, and year attributes private.
# Add getter and setter methods to access and modify these private attributes.

class Car:
    def __init__(self, make, model, year):
        """Initialization"""
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        """ getter method """
        return self.__make
    
    def set_make(self, make):
        """ setter method """
        self.__make = make

    def get_model(self):
        """ getter method """
        return self.__model
    
    def set_model(self, model):
        """ setter method """
        self.__model = model

    def get_year(self):
        """ getter method """
        return self.__year
    
    def set_year(self, year):
        """ setter method """
        self.__year = year

#object creation
car_obj = Car("Toyota", "Corolla", 2020)

print(f"Make: {car_obj.get_make()}")
car_obj.set_make("Honda")
print(f"Updated Make: {car_obj.get_make()}")

print(f"Model: {car_obj.get_model()}")
car_obj.set_model("Civic")
print(f"Updated Model: {car_obj.get_model()}")

print(f"Year: {car_obj.get_year()}")
car_obj.set_year(2018)  
print(f"Updated Year: {car_obj.get_year()}")