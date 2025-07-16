#Ejercicios de Funciones #1


def get_larger_num():
    counter = 1
    while counter <= 2:
        current_num = int(input("Digite un numero "))
        if counter == 1:
            larger_num = current_num
        else:
            if current_num > larger_num:
                larger_num = current_num
        counter = counter + 1 #Sum the counter
    print("El numero mayor es",larger_num)


def get_user():
    name = (input("Escriba su nombre "))
    print("Hola",name)
    get_larger_num() #Calls get_larger_num function


get_user()