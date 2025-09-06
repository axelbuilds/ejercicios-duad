#Ejercicio OOP #1

class Circle():
    def __init__(self,radius): #
        self.radius = radius #Saves radius value


    def get_area(self): #Method to calculate circle area
        area = 3.14 * self.radius**2
        return area


circle_area = Circle(5) #Gives the radius value

print(circle_area.get_area())