#Ejercicios de Sintaxis #4

print("Digite 3 numeros para mostrar cual es el mayor")

current_num = 0
larger_num = 0
counter = 1

while counter <= 3:
    current_num = int(input("Digite un numero "))
    if counter == 1: #Will be TRUE ONLY the first time
        larger_num = current_num
    else:
        if current_num > larger_num:
            larger_num = current_num
    counter = counter + 1 #Increments counter
print("El numero mayor es",larger_num)