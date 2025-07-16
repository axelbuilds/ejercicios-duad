#Ejercicios de Funciones #5


def uppercase_count(my_string):
    upper_count = 0
    for index in my_string:
        if index.isupper(): #Search for uppercase in my_string
            upper_count = upper_count + 1
    return upper_count


def lowercase_count(my_string):
    lower_count = 0
    for index in my_string:
        if index.islower(): #Search for lowercase in my_string
            lower_count = lower_count + 1
    return lower_count


def main():
    my_string = "I Love Programming, it is FUN" #Local Variable
    upper_total = uppercase_count(my_string)
    lower_total = lowercase_count(my_string)
    print(f'There are {upper_total} uppercase, and {lower_total} lowercase')


main()


###Se puede hacer mas corto usando una sola funcion para sacar upper y lower
###Preguntar si es mejor separarlas en 2 funciones
#def char_count(my_string):
#    upper_count = 0  # Se define como variable local
#    lower_count = 0
#
#    for char in my_string:  # Más limpio que usar range + índices
#        if char.isupper():
#            upper_count += 1
#        elif char.islower():
#            lower_count += 1
#
#    return upper_count, lower_count  # Devuelve ambos valores
#
#
#def main():
#    my_string = "I love Programming it is FUN"
#    upper_total, lower_total = char_count(my_string)  # Recibe los 2 valores
#    print(f'There are {upper_total} uppercase letters and {lower_total} lowercase letters.')
#
#
#main()
