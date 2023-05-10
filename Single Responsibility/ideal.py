class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def get_age(self):
        return f"{self.name} is {self.age} years old."

    def get_name(self):
        return self.name

class AnimalSound:
    def get_sound(self,animal: Animal) -> str:
        return f"{animal.name} says {animal.sound}."
    
# object creation
cat = Animal("Tom", 2, "Meow")
animal_sound = AnimalSound()
print(animal_sound.get_sound(cat))

dog = Animal("Buddy", 4, "Bark")
animal_sound = AnimalSound()
print(animal_sound.get_sound(dog))
