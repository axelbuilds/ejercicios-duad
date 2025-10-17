#Ejercicios Decoradores #3

from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth #Stores user DOB

    @property #Converts age like an attribute instead of method
    def age(self):
        today = date.today() #Gets current date
        #Calculates age by current date and date of birth
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )


def age_check(func): #Decorador to check is the user is an adult
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("El usuario debe ser mayor de edad.")
        return func(user, *args, **kwargs) #If condition is not met runs original function
    return wrapper


@age_check #Calls decorador
def regular_user(user):
    #Runs only if user is older than 18
    return f"Tiene acceso. La edad del usuario es {user.age}."


#Testing
user1 = User(date(1995, 2, 10))
user2 = User(date(2010, 3, 21))

print(regular_user(user1))
print(regular_user(user2))