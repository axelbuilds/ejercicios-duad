#Ejercicios de Unit Testing 1

def bubble_sort(list_to_sort):

    for index_sort in range(0, len(list_to_sort) -1):

        for index in range(0, len(list_to_sort) -1 -index_sort):
            current_num = list_to_sort[index]
            next_num = list_to_sort[index + 1]
            print(f'Indice: {index} - Numero actual {current_num} - Siguiente Numero {next_num}')

            if current_num > next_num:
                list_to_sort[index] = next_num
                list_to_sort[index + 1] = current_num
                print(f'Se cambio {current_num} - por {next_num}')


input_list = [7,5,3,2,8,1,4,9,6]
bubble_sort(input_list)
print(input_list)