#Ejercicios de Funciones #4


def string_func(my_string):
    backwards_str = "" #Local variable to store reversed characters
    for index in range(len(my_string)-1,-1,-1): #range() is divided in 3 elements (-1,-1,-1))
        backwards_str = backwards_str + my_string[index] #Adds characters to backwards_str
    return backwards_str


def main():
    my_string = "odnum aloH"
    result = string_func(my_string) #Stores the result and calls function
    print(result)


main()