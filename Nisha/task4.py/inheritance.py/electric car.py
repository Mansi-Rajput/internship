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
        self.battery_size = battery_size  # added attribute

    def charge(self, hours):
        self.battery_size += hours

    def display_info(self):
        super().display_info()
        print(f"Battery size: {self.battery_size} kWh")

my_car = ElectricCar('red', 30000, 75)
my_car.drive(100)
my_car.charge(5)
my_car.display_info()

class Device:
    def __init__(self, name, battery_size):
        self.name = name
        self.battery_size = battery_size

    def display_info(self):
        print(f"Device: {self.name}")
        print(f"Battery Size: {self.battery_size} mAh")

class Smartphone(Device):
    def __init__(self, name, battery_size, screen_size):
        super().__init__(name, battery_size)
        self.screen_size = screen_size

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size} inches")

# Create a Smartphone object
my_phone = Smartphone("iPhone 13", 4500, 6.1)

# Call the display_info method
my_phone.display_info()