#Ejercicios de Funciones #7

def prime_verification(num):
    if num < 2: #Will start on number 2 because 0 and 1 are not a prime numbers
        return False
    
    for index in range(2, num):
        if num % index == 0:
            return False #Will Return false if num == 0
    return True #Will be true if it is not divisible

def prime_numbers(num_list):
    prime_list = []
    for num in num_list:
        if prime_verification(num): #Calls function for each number
            prime_list.append(num) #Appends the numbers to the list
    return prime_list


def main():
    num_list = [1, 4, 6, 7, 13, 9, 67] #Numbers list
    result = prime_numbers(num_list) #Stores the final result and calls function
    print(result)

main()