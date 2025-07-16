#Ejercicios de Funciones #6


def sort_strings(words):
    my_string = words.split("-") #Divides words whenever a dash "-" is found
    sorted_list = sorted(my_string) #Sorts alphabetically
    joined_strings = "-".join(sorted_list) #Joins the words with a dash "-"
    return joined_strings


def main():
    words = "these-words-are-for-a-function-practice" #Local Variable
    sort_result = sort_strings(words) #Stores the result and calls function sort_strings
    print(sort_result)


main()