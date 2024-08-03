class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says Bark!"

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


my_dog = Dog("Chance", 5, "Golden Retreiver")

print(my_dog.bark())
print(my_dog.get_age())
my_dog.set_age(8)
print(my_dog.get_age())
