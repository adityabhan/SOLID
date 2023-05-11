from math import pi, pow


class Shape:
    def get_area(self, shape):
        if shape.name == "rectangle":
            return shape.length * shape.breadth
        elif shape.name == "circle":
            return pow(shape.radius, 2) * pi


class Rectangle(Shape):
    name = "rectangle"

    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth


class Circle(Shape):
    name = "circle"

    def __init__(self, radius) -> None:
        self.radius = radius


circle = Circle(5)
print(f"area of circle is {circle.get_area(circle)} square units.")

rect = Rectangle(2, 3)
print(f"area of rectangle is {rect.get_area(rect)} square units.")
