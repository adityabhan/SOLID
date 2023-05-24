from abc import ABC, abstractmethod


class Rectangle(ABC):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    @abstractmethod
    def setWidth(self, breadth):
        self.breadth = breadth

    @abstractmethod
    def setHeight(self, length):
        self.length = length

    @abstractmethod
    def get_area(self):
        return self.length * self.breadth


class Square(Rectangle):
    def __init__(self, length) -> None:
        self.length = self.breadth = length

    def setWidth(self, breadth):
        self.length = self.breadth = breadth

    def setHeight(self, length):
        self.length = self.breadth = length

    def get_area(self):
        return self.length * self.breadth


sq = Square(2)
print(sq.get_area())
