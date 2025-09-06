#Ejercicio Extra OOP 1

class Rectangle: #Constructor
    def __init__(self, width, height):
        if width < 0 or height < 0: #Validates values are higher than 0
            raise ValueError("Hay un valor negativo. Los valores solo pueden ser positivos")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height) * 2


#Input requests with a loop until valid values are entered
while True: 
    try:
        width = int(input("Ingrese el ancho del rectangulo: "))
        height = int(input("Ingrese la altura del rectangulo: "))

        rectangle = Rectangle(width, height) #Creates Rectangle Instance

        print(f'Area: {rectangle.get_area()}')
        print(f'Perimetro: {rectangle.get_perimeter()}')
        break #Exits the loop if no there are no catches
    except ValueError as e:
        print("Debe ingresar valores numericos")