#Ejercicio Extra 2 - Bubble Sort

def bubble_sort_steps(list_to_sort):
    iterations = 0
    swaps = 0

    for sort_index in range(0,(len(list_to_sort) - 1)): #Loop to count how many time it runs
        iterations = iterations + 1 #Adds to iteration
        list_changes = False

        for index in range(0, len(list_to_sort) - 1 - sort_index): #Inner Loop to compare numbers
            current_num = list_to_sort[index] #Current number is equal to the position in the index
            next_num = list_to_sort[index + 1] #Next number is the next number in the index to the right

            if current_num > next_num: #Checks if current is greater than next number
                list_to_sort[index] = next_num #If True, changes position to the next number
                list_to_sort[index + 1] = current_num #Current number is now the next in the index
                swaps = swaps + 1 #Adds to swap
                list_changes = True
        if not list_changes:
            break

    print(f'Lista ordenada: {list_to_sort}')
    print(f'Iteraciones: {iterations}')
    print(f'Swaps: {swaps}')

#Testing
num_list = [5,4,3,6,1,7,2]
bubble_sort_steps(num_list)