#Ejercicio Extra 1 - Bubble Sort

class Node:
    def __init__(self, data):
        self.data = data #Saves node's value
        self.next = None #Pointer to next node in the list


class LinkedList:
    def __init__(self):
        self.head = None #First node in the list

    def append(self, data):
        new_node = Node(data) #Creates a new node with given data

        if self.head is None: #Checks if list is empty
            self.head = new_node #New node becomes the head
            return
        
        #Runs through the list until reaches the last node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node #Adds new node at the end of the list

    def length(self):
        count = 0 #Counter to count nodes
        current = self.head  #Start from the head
        while current: #Goes through the list
            count = count + 1 #Adds to the counter
            current = current.next  #Moves to next node
        return count #Returns total nodes

    def bubble_sort(self):
        if self.head is None: #Checks if list is empty
            return
        
        list_lenght = self.length() #Gets list length to control how many times to loop

        #New loop to repeat the number of times equal to the list length - 1
        for sort_index in range(0, list_lenght - 1):
            list_changes = False #Tracks if any swap was made

            current = self.head #Starts from the first node in each iteration
            index = 0 #Manual index counter to imitate list indexing

            #Inner loop to go through the list and remove the last index numbers already sorted
            while current and current.next and index < list_lenght - 1 - sort_index:
                current_num = current.data #Stores the value of the current node
                next_num = current.next.data #Stores the value of the next node

                #Prints current comparison
                print(f"Index: {index} - Numero actual: {current_num} - Siguiente numero: {next_num}")

                #Checks if current is greater than next number
                if current_num > next_num:
                    #If True, swaps the values
                    current.data, current.next.data = next_num, current_num
                    list_changes = True #Marks that a swap was made

                    print(f"Se movio: {current_num}")

                #Moves to the next node (equivalent to increasing index)
                current = current.next
                index += 1 #Increases index to imitate list index movement

            #If no changes, numbers are already sorted
            if not list_changes:
                print("Los numeros ya estan ordenados")
                return

    def print_list(self):
        current = self.head #Starts printing from the head
        while current:
            print(f"{current.data}", end = " - ")  #Prints each node's value
            current = current.next #Moves to next node
        print("None") #End of list


#Testing
linked_list = LinkedList()

for num in [6,4,9,7,2,8,1,3,5]:#Adds the numbers to the linked list
    linked_list.append(num)

linked_list.bubble_sort() #Calls bubble sort

print(f'Lista ordenada:')
linked_list.print_list() #Prints list after sorting