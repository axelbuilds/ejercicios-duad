#Ejercicios Unit Testing 2

#Ejercicio Funciones 3 - Semana 6
def sum_list(num_list):
    total_sum = 0
    for index in num_list:
        total_sum = total_sum + index
    return total_sum


#Ejercicio Funciones 4 - Semana 6
def string_func(my_string):
    backwards_str = ""
    for index in range(len(my_string)-1,-1,-1):
        backwards_str = backwards_str + my_string[index]
    return backwards_str


#Ejercicio Funciones 5 - Semana 6
def uppercase_count(my_string):
    upper_count = 0
    for index in my_string:
        if index.isupper():
            upper_count = upper_count + 1
    return upper_count

def lowercase_count(my_string):
    lower_count = 0
    for index in my_string:
        if index.islower():
            lower_count = lower_count + 1
    return lower_count