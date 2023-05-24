from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, feed):
        self.name = name
        self.feed = feed

    def get_name(self):
        return self.name

    @abstractmethod
    def feed_type(self):
        return f"s{self.name} is {self.feed}"

    @abstractmethod
    def pet(self):
        return f"{self.name} is a pet."


class Dog(Animal):
    def feed_type(self):
        return f"s{self.name} is an {self.feed}"

    def pet(self):
        return f"{self.name} is a pet."


class Tiger(Animal):
    def feed_type(self):
        return f"{self.name} is a {self.feed}"

    def pet(self):
        return f"{self.name} is not a pet."


tiger = Tiger("Richard Parker", "Carnivore")
dog = Dog("Roxy", "Omnivore")

print(dog.pet())
print(tiger.pet())
