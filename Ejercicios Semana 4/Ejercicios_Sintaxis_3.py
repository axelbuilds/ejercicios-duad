#Ejercicio de Sintaxis #3
#Uso de Modulo random para generar numeros aleatorios

import random #Calls module

secret_num = random.randint(1,10) #Generates a random number
num_guess = int(input("Adivine el numero secreto del 1 al 10 "))

while num_guess != secret_num:
    secret_num = random.randint(1,10)
    num_guess = int(input("Numero incorrecto. Intentelo de nuevo "))
print("Felicidades, adivino el numero secreto")