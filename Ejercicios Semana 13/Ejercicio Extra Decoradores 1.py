#Ejercicio Extra Decoradores 1

def repeat_twice(func): #Decorador calls function twice
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@repeat_twice #Calls decorador
def greeting(name):
    print(f'Hola {name}')


#Testing
greeting("Axel")