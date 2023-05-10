class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def get_age(self):
        return f"{self.name} is {self.age} years old."

    def get_name(self):
        return self.name

    def get_sound(self) -> str:
        return f"{self.name} says {self.sound}."

# object creation
cat = Animal("Tom", 2, "Meow")
print(cat.get_name())
print(cat.get_age())
print(cat.get_sound())