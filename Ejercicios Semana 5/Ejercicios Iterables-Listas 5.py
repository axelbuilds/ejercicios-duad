#Ejercicios de Iterables y Listas #5

num_list = []
counter = 1

while counter <= 10:
    new_num = int(input("Digite un numero "))
    if counter == 1: #Will be TRUE ONLY the first time
        larger_num = new_num
    else:
        if new_num > larger_num:
            larger_num = new_num
    num_list.append(new_num) #Stores the new numbers in the list
    counter = counter + 1

print(num_list, "El numero mas alto es",larger_num)