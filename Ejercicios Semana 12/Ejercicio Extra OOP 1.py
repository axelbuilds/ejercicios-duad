#Ejercicio Extra OOP 1

#Reminder
# name = Public
# _name = Protected
# __name = Private

class Employee():
    def __init__(self, _name, _salary):
        self._name = _name #Private attribute
        self._salary = _salary #Private attribute

    @property #Turns the method into a getter, allowing it to be accessed like an attribute
    def name(self):
        return self._name

    @name.setter #When a value is assigned to the property the method with @<attribute_name>.setter is executed
    def name(self, value):
        self._name = value

    @property
    def salary(self, salary):
        return self.salary

    @salary.setter
    def salary(self, value):
        if value < 0: #Validates the salary is not negative
            raise ValueError("El salario no puede ser negativo")
        self._salary = value

    def promote(self, percentage): #Method for salary calculation
        self.salary = self._salary * (1 + percentage)


employee = Employee("Axel", 1000) #Object - Parameters to constructor
employee.promote(0.1) #Adds to percentage parameter
print(employee._salary)