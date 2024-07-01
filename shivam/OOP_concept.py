#Task 1 of topic 4

#create a class name car 
class Car:
    #define an instance object with method display_info
     def __init__(self,make,model,year):
         self.make=make
         self.model=model
         self.year=year
     def display_info(self):
        print("Make :",self.make)
        print("Model:",self.model)
        print("Year:",self.year)

         
class ElectricCar(Car):
     def __init__(self,make,model,year,battery_size):
#Super function is used to call the __init__ and display_info
      super().__init__(make,model,year)
      self.battery_size = battery_size
    
     def display_info(self):         
        super().display_info()
        print("Battery size: ",self.battery_size)

my_car = ElectricCar("Nexon","Model S", 2023,75)
my_car.display_info()


#Polymerphism
class Bike:
    def start_engine(self):
        print("Bike engine started")
class Car1:
    def start_engine(self):
        print("Car engine started")
        
def start_vehicle(vehicle):
    vehicle.start_engine()
bike = Bike()
car = Car1()
start_vehicle(bike) 
start_vehicle(car)


#Encapsulation
#Getters: These are the methods used in Object-Oriented Programming(OOPS) which helps to access the private attributes from class.
#Setters: These are the methods used in OOPS feature which helps to set the value to private attributes in a class
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # Getter methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Setter methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_make())  
print(my_car.get_model()
print(my_car.get_year())  

my_car.set_make("Honda")
my_car.set_model("Civic")
my_car.set_year(2022)
print(my_car.get_make())  
print(my_car.get_model()
print(my_car.get_year())  
