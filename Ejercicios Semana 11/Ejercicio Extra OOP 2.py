#Ejercicio Extra OOP 2

class Animal: #Constructor
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un sonido"


class Dog(Animal): #Inherits from Animal
    def speak(self):
        return "Guau"


class Cat(Animal): #Inherits from Animal
    def speak(self):
        return "Miau"

#Creates Objects
dog = Dog("Firulais")
cat = Cat("Misingo")

#Calls speack function and prints value
print(dog.speak())
print(cat.speak())