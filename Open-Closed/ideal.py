from math import pi, pow
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    name = "rectangle"

    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth


class Circle(Shape):
    name = "circle"

    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        return pow(self.radius, 2) * pi


circle = Circle(5)
print(f"area of circle is {circle.get_area()} square units.")

rect = Rectangle(2, 3)
print(f"area of circle is {rect.get_area()} square units.")
