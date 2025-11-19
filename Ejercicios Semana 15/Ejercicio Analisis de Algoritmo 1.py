#Ejercicio Bubble Sort 1


def bubble_sort(list_to_sort):

    for sort_index in range(0, len(list_to_sort) - 1): #O(n)
        
        list_changes = False #O(1)
        
        for index in range(0, len(list_to_sort) - 1 - sort_index): #O(n)
            current_num = list_to_sort[index] #O(1)
            next_num = list_to_sort[index + 1] #O(1)
            print(f'Index: {index} - Numero actual: {current_num} - Siguiente numero: {next_num}') #O(1)
            
            if current_num > next_num: #O(1)
                list_to_sort[index] = next_num #O(1)
                list_to_sort[index + 1] = current_num #O(1)
                list_changes = True #O(1)
                print(f'Se movio: {current_num}') #O(1)
        
        if not list_changes: #O(1)
            print(f'Los numeros ya estan ordenados') #O(1)
            return # O(1)

#Testing
num_list = [6,4,9,7,2,8,1,3,5] #O(1)
bubble_sort(num_list) #O(1)
print(num_list) #O(1)