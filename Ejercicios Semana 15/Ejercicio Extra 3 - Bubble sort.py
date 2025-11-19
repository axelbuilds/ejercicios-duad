#Ejercicio Extra 3 - Bubble Sort

def bubble_sort(list_to_sort):
    num = len(list_to_sort) #Stores the amount of numbers saved in the list
    for x in range(num - 1): #Outer loop to run through the list
        for i in range(num - 1 - x): #Inner loop to compare numbers
            if list_to_sort[i] > list_to_sort[i + 1]: #Compares current number with the next one
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i] #Swaps the numbers
    return list_to_sort #Returns sorted list


def get_list():
    list_input = (input(("Escriba los numeros que desea ordenar separados por coma: ")))
    if not list_input.strip(): #Validates if list is empty
        print("La lista no puede estar vacia")
        return
    values = list_input.split(',') #Separates values into a list
    numbers = []
    try:
        for x in values:
            numbers.append(int(x.strip())) #Checks if values are numbers, if not raise error
    except:
        ValueError(print("Error. La lista contiene elementos no numericos"))
        return
    sorted_list = bubble_sort(numbers)
    print(f'Lista ordenada: {sorted_list}')

get_list()