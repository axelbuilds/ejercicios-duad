#Ejercicio Extra Decoradores 2

class User:
    def __init__(self, name, logged_in):
        self.name = name #Store user's name
        self.logged_in = logged_in #Checks whether logged_in is True or False


def requires_login(func): #Decorador to check if the user is logged in
    def wrapper(user, *args, **kwargs):
        if not user.logged_in: #If user is not logged in raises exception
            raise Exception("Usuario no autenticado")
        return func(user, *args, **kwargs)
    return wrapper


@requires_login #Calls decorador
def access(user):
    return f'Acceso permitido al perfil de {user.name}'


#Testing
user1 = User("Axel", logged_in = True)
user2 = User("Test", logged_in = False)

print(access(user1))
print(access(user2))
