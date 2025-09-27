#Ejercicio de Pilares OOP #2

from abc import ABC, abstractmethod

class Shape(ABC): #Abstract Class

    @abstractmethod
    def calculate_area(self): #All shapes must include calculate_area()
        pass

    @abstractmethod
    def calculate_perimeter(self): #All shapes must include calculate_perimeter()
        pass


class Circle(Shape): #Circle class inherits from Shape()
    def __init__(self, radius):
        self.radius = radius #Starts the class with radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Square(Shape):
    def __init__(self, side): #Starts the class with side
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, lenght, width): #Starts the class with lenght and width
        self.lenght = lenght
        self.width = width

    def calculate_area(self):
        return self.lenght * self.width

    def calculate_perimeter(self):
        return 2 * (self.lenght + self.width)



#Tests
circle = Circle(3)
print(f'Area del Circulo: {circle.calculate_area()} - Perimetro del Circulo {circle.calculate_perimeter()}')


square = Square(2)
print(f'Area del Cuadrado: {square.calculate_area()} - Perimetro del Cuadrado {square.calculate_perimeter()}')


rectangle = Rectangle(2, 4)
print(f'Area del Rectangulo: {rectangle.calculate_area()} - Perimetro del Rectangulo {rectangle.calculate_perimeter()}')