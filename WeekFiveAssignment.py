# Assignment 1
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price > 0:
            self.price = price
        else:
            print("Price must be positive!")

    def display_details(self):
        print(f"Brand: {self.brand},Model: {self.model}, Price: {self.price}")

    def price_comparison(self, phone2):
        if isinstance(phone2,Phone):
            if self.price > phone2.price:
                print(f"{self.brand} {self.model} is more expensive than {phone2.brand} {phone2.model}")

class Smartphone(Phone):
    def __init__(self, brand, model, price, os, ram):
        super().__init__(brand, model, price)  # Call parent constructor
        self.os = os
        self.ram = ram

    def display_details(self):
        super().display_details()  # Call parent method
        print(f"Operating System: {self.os}, RAM: {self.ram}GB")


phone1 = Smartphone("Apple", "iPhone 16", 1500, "iOS", 8)
phone2 = Smartphone("Samsung", "S22", 1200, "Android", 12)

phone1.display_details()
phone2.display_details()
phone1.price_comparison(phone2)


# Activity 2: Polymorphism Challenge!
class Vehicles:
    def move(self):
        pass

class Sedan(Vehicles):
    def move(self):
        print("Driving")

class Jet(Vehicles):
    def move(self):
        print("Flying")

class Yacht(Vehicles):
    def move(self):
        print("Sailing")

def movement(Vehicles):
    for vehicle in Vehicles:
        vehicle.move()

Bmw =  Sedan()
Boeing = Jet()
Marina = Yacht()

# Bmw.move()
# Boeing.move()
# Marina.move()
Vehicles = [Bmw, Boeing, Marina]
movement(Vehicles)