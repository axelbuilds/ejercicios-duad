#Ejercicios de Iterables y Listas #4

my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
]
even_num_list = []
odd_list = []

for index in range(len(my_list)):
    if my_list[index] % 2 == 0: #Identifies which numbers of the list can be divided by 2
        even_num_list.append(my_list[index])
    else:
        odd_list.append(my_list[index])

print(even_num_list)
print(odd_list)