#Ejercicios de Funciones #3

def sum_list(num_list):
    total_sum = 0 #Local variable to store the value in the list
    for index in num_list: #Goes through the list and sums the numbers
        total_sum = total_sum + index
    return total_sum


def main():
    num_list = [3, 5, 7, 10] #List of numbers
    result = sum_list(num_list) #Stores the total sum and calls sum_list function
    print(result)


main()