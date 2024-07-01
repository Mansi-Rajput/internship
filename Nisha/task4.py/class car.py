class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


if __name__ == "__main__":
    my_car = Car("mercedes", "benz class", 2024)
    print(my_car)

    
