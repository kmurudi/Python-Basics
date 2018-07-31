#!usr/bin/python
# A program to create different animals
class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sound(self):
        print(self.name+" is speaking normal")

# Demonstrating Inheritance from parent class - Animal
class Dog(Animal):
    # See how you can inherit parent class attributes without defining them here in child class
    def describe(self):
        print("Hi I am "+self.name+", a dog! of color- "+self.color)

    # Concept of Overriding methods of parent class
    def sound(self):
        print("Bark Bark.")


class Cat(Animal):
    # See how you can inherit parent class attributes without defining them here in child class
    def describe(self):
        print("Hi I am " + self.name + ", a cat! of color- " + self.color)

    # Concept of Overriding methods of parent class
    def sound(self):
        print("Meow Meow.")

# Creating objects - class instances
dog = Dog("coco","black")
cat = Cat("kitty","white")

# Testing the methods created now
dog.describe()
dog.sound()
cat.describe()
cat.sound()
