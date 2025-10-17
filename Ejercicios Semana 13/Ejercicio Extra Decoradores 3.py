#Ejercicio Extra Decoradores 3

from datetime import datetime

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for value in list(args) + list(kwargs.values()): #Combines values into a single list
            if not isinstance(value, (int, float)): #If value is not a number raises Exception
                raise TypeError(f'El valor {value} no es un numero')
        return func(*args, **kwargs)
    return wrapper


def log_call(func):
    def wrapper(*args, **kwargs):
        current_time = datetime.now() #Gets the current date and time
        print(f'Funcion: {func.__name__} - args: {args}, {kwargs}, Fecha: [{current_time}]')
        result = func(*args, **kwargs) #Execute original function
        print(f'Resultado: {result}') #Prints the return value
        return result #Return the function result
    return wrapper

#Calls decoradors
@log_call 
@validate_numbers
def multiply(a, b):
    return a * b


#Testing
print(multiply(2, 6))
print(multiply("abc", 4))