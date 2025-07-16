#Ejercicio de Diccionarios #3

list_of_keys = [
    "access_level",
    "age"
]
employee = {
    "name": "Axel",
    "email": "axel@ecorp.com",
    "access_level": 5,
    "age": 28
    }

for key in list_of_keys: #Goes through the list and .pop will delete any key that matches
    employee.pop(key)
print(employee)