#Ejercicios de Iterables y Listas #1

first_list = [
    'Hay',
    'en',
    'que',
    'iteracion',
    'indices',
    'muy'
]

second_list = [
    'casos',
    'los',
    'la',
    'por',
    'es',
    'util'
]

for index in range(len(first_list)): #len() counts the amount of elements on the list (6)
    print(first_list[index],second_list[index]) #prints the value in range of each list once

#len(first_list) counts the amount of elements on the list (6)
#range generates the list of numbers 0,1,2,3,4,5,6
#first_list[0] = 'Hay'
#first_list[1] = 'en'
#first_list[2] = 'que'
#for index in range(6)
#print(first_list[index],second_list[index]) prints the value of each list once
#   0 = 'Hay' - 'casos'