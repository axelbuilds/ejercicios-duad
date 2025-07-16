#Ejercicio de Diccionarios #2

dictionary = {}

keys_list = [
    "first_name",
    "last_name",
    "role"
]
values_list = [
    "Axel",
    "Martinez",
    "Student"
]

for index in range(len(keys_list)):
    dictionary[keys_list[index]] = values_list[index] #Assigns the values to keys while storing in dictionary

print(dictionary)