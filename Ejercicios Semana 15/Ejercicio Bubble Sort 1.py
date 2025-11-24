#Ejercicio Bubble Sort 1


def bubble_sort(list_to_sort):
    for sort_index in range(0, len(list_to_sort) - 1): #New loop to repeat the number of times equal to the list lenght
        list_changes = False
        #Inner loop to go through the list and Removes the last index number
        for index in range(0, len(list_to_sort) - 1 - sort_index): #Removes the numbers already sorted
            current_num = list_to_sort[index] 
            next_num = list_to_sort[index + 1] #Next number is now the next number in the index
            print(f'Index: {index} - Numero actual: {current_num} - Siguiente numero: {next_num}')

            if current_num > next_num: #Checks if current is greater than next number
                list_to_sort[index] = next_num #If True, changes position to the next number
                list_to_sort[index + 1] = current_num #Current number is now the next in the index
                list_changes = True
                print(f'Se movio: {current_num}')
        #If no changes, number are already sorted
        if not list_changes:
            print(f'Los numeros ya estan ordenados')
            return

#Testing
num_list = [6,4,9,7,2,8,1,3,5] #Input List
bubble_sort(num_list) #Calls function
print(num_list) #Prints the list after sorting