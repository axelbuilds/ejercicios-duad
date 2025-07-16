#Ejercicios de Iterables y Listas #2

my_string = "Pizza con piña"

for index in range(len(my_string)-1,-1,-1): #range() is divided in 3 elements (-1,-1,-1))
    print(my_string[index])

# First element of range() indicates where the loop begins. -1 The last string will be the start.
# Second element of range() indicates where the loop will stop before reaching this index. 
    # If used range(len(my_string)-1,9,-1) it will only print 'piña'
# Third element of range() indicates how many steps to move on the index.