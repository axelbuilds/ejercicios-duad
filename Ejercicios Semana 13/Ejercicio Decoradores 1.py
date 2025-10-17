#Ejercicios Decoradores #1

def decorador_example(func): #Decorador
    def wrapper(*args, **kwargs):
        print(f'Funcion {func.__name__} con *args = {args}, **kwargs = {kwargs}')
        result = func(*args, ** kwargs)

        print(f'Funcion {func.__name__} devolvio {result}')
        return result
    return wrapper

@decorador_example #Calls Decorador
def sum(a, b):
    return a + b

@decorador_example #Calls Decorador
def greeting(name, age=None):
    return f'Hola {name}, age={age}'


#Testing
sum(3, 4)
greeting("Axel", age=30)