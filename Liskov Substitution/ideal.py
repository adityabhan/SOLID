from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    def setWidth(self, breadth):
        self.breadth = breadth

    def setHeight(self, length):
        self.length = length

    def get_area(self):
        return self.length * self.breadth


class Square(Shape):
    def __init__(self, length) -> None:
        self.side = length

    def get_area(self):
        return self.side**2


sq = Square(2)
print(sq.get_area())
