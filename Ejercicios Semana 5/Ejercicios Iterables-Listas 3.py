#Ejercicios de Iterables y Listas #3

my_list = [
    4,
    3,
    6,
    1,
    7
]

first_element = my_list[0] #Finds the first element of the list
last_element = my_list[-1] #Finds the last element of the list

my_list.pop(0) #Removes the First and Last elements of the original list
my_list.pop(-1)

my_list.insert(0,last_element) #Inserts the last number to position 0 of the list
my_list.append(first_element) #Appends the first number to the last position

print(my_list)