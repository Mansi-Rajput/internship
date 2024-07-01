class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage 

    def drive(self, miles):
        self.mileage += miles

    def display_info(self):
        print(f"Car details:")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage} miles")

        

class ElectricCar(Car):
    def __init__(self, color, mileage, battery_size):
        super().__init__(color, mileage)
        self.battery_size = battery_size

    def charge(self, hours):
        self.battery_size += hours

    def display_info(self):
        super().display_info()
        print(f"Battery size: {self.battery_size} kWh")

my_car = ElectricCar('blue', 30000, 75)
my_car.drive(100)
my_car.charge(5)
my_car.display_info()
      
