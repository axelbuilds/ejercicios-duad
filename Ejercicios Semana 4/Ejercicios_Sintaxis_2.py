#Ejercicio de Sintaxis #2

name = (input("Escriba su nombre "))
last_name = (input("Escriba su apellido "))
age = int(input("Escriba su edad "))

if age <= 2:
    print("Usted es un bebe")
elif age <= 10:
    print("Usted es niño")
elif age <= 12:
    print("Usted es preadolescente")
elif age <= 17:
    print("Usted es adolescente")
elif age <= 29:
    print("Usted es adulto joven")
elif age <= 59:
    print("Usted es adulto")
else:
    print("Usted es adulto mayor")