from abc import ABC
from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Crust(Enum):
    PLAIN = 100
    CHEESE = 200
    VEGAN = 300

class Pizza(ABC):
    def __init__(self):
        self.cost

class PeperroniPizza(Pizza):
    def __init__(self, size: Size, crust: Crust):
        self.cost = 100
        self.size = size
        self.crust = crust
        self.toppings = []

    def get_price(self):
        
        toppings = 0
        for topping in self.toppings:
            toppings += topping.get_price

        return toppings + (self.cost * self.size) + self.crust
