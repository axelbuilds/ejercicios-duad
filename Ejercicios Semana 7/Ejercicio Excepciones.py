#Ejercicio de Excepciones


def sum_function(current_num):
    print("Digite los numeros que desea sumar o escriba 'Menu' para regresar al Menu Principal.")
    while True:
        num = input("+ ")
        if num.lower() == "menu": # .lower() Allows lower and upper case to match the value
            return current_num #Returns the new value of current_num
        try:
            num = int(num)
            current_num = current_num + num #Sum operation
            print(f'Resultado: {current_num}')
        except ValueError:
            print("Por favor, digite un numero valido o 'Menu' para regresar al Menu Principal.")


def deduct_function(current_num):
    print("Digite los numeros que desea restar o escriba 'Menu' para regresar al Menu Principal.")
    if current_num == 0: #Condition to determine if the current num will be the initial value
        initial_num = True
    else:
        initial_num = False
    while True:
        num = input("- ")
        if num.lower() == "menu": # .lower() Allows lower and upper case to match the value
            return current_num #Returns the new value of current_num
        try:
            num = int(num)
            if initial_num:
                current_num = num
                initial_num = False
            else:
                current_num = current_num - num #Deducts from the current number
            print(f'Resultado: {current_num}')
        except ValueError:
            print("Por favor, digite un numero valido o 'Menu' para regresar al Menu Principal.")


def multiply_function(current_num):
    print("Digite los numeros que desea multiplicar o escriba 'Menu' para regresar al Menu Principal.")
    if current_num == 0: #Condition to determine if the current num will be the initial value
        initial_num = True
    else:
        initial_num = False
    while True:
        num = input("x ")
        if num.lower() == "menu": # .lower() Allows lower and upper case to match the value
            return current_num #Returns the new value of current_num
        try:
            num = int(num)
            if initial_num:
                current_num = num
                initial_num = False
            else:
                current_num = current_num * num #Multiplication operation
            print(f'Resultado: {current_num}')
        except ValueError:
            print("Por favor, digite un numero valido o 'Menu' para regresar al Menu Principal.")


def division_function(current_num):
    print("Digite los numeros que desea dividir o escriba 'Menu' para regresar al Menu Principal.")
    if current_num == 0: #Condition to determine if the current num will be the initial value
        initial_num = True
    else:    
        initial_num = False
    while True:
        num = input("/ ")
        if num.lower() == "menu": # .lower() Allows lower and upper case to match the value
            return current_num #Returns the new value of current_num
        try:
            num = int(num)
            if initial_num:
                current_num = num
                initial_num = False
            else:
                current_num = current_num / num #Division operation
            print(f'Resultado: {current_num}')
        except ValueError:
            print("Por favor, digite un numero valido o 'Menu' para regresar al Menu Principal.")


def main():
    current_num = 0
    while True:
        print('''
            Bienvenido al Menu Principal
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Borrar Resultado
            ''')
        try:
            menu_selection = int(input("Digite un numero segun la operacion que desea realizar: "))
            print(current_num)
            if menu_selection == 1:
                current_num = sum_function(current_num) #Calls Sum Function
            elif menu_selection == 2:
                current_num = deduct_function(current_num) #Calls Deduct Function
            elif menu_selection == 3:
                current_num = multiply_function(current_num) #Calls Multiplication Function
            elif menu_selection == 4:
                current_num = division_function(current_num) #Calls Division Function
            elif menu_selection == 5:
                current_num = 0  #Assigns value 0 to the global variable
                print('''
                    - Se borro el resultado -
                    ''')
            else: #Calls main function of value is different from the options available
                print('''
                    - Digite un numero del 1 al 5 para seleccionar las operaciones disponibles -
                    ''')

        except ValueError: #Catches any string and calls back main function
            print('''
                Entrada Invalida. Por favor digite un número del 1 al 5.
                ''')


main()