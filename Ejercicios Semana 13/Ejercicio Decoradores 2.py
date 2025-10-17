#Ejercicios Decoradores #1

def check_parameters(func):
    def wrapper(*args, **kwargs):
        for value in list(args) + list(kwargs.values()):
            if not isinstance(value, (int, float)):
                raise TypeError(f'El valor {value} no es un numero')
        return func(*args, **kwargs)
    return wrapper

@check_parameters #Calls Decorador
def sum(a, b):
    return a + b

#Testing
print(sum(10, 3))
print(sum(5, "test"))