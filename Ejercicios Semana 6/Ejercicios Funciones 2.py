#Ejercicios de Funciones #2

num3 = 2 #Global variable


def get_num(num2):
    num1 = int(input("Digite un numero "))
    if num1 >= 5: 
        global num3 #Changes Global variable num3 value if condition is met
        num3 = 1
    result = (num1 + num2) * num3
    print(result)


def main():
    num2 = 3 #Local variable
    get_num(num2) #Calls function


main()