#Ejercicio Estructura de datos 2

class Node:
    def __init__(self, data):
        self.data = data #Stores de Node's value
        self.next = None #Points to the next node
        self.previous = None #Points to the previous node


class Deque:
    def __init__(self):
        self.left = None #First Node (left to right)
        self.right = None #Last node (left to right)

    def push_left(self, data):
        new_node = Node(data)
        if self.left is None:
            self.left = self.right = new_node # If queue is empty both ends are the same
        else:
            new_node.next = self.left #Link the new node to the current left node
            self.left.previous = new_node
            self.left = new_node #Update left to the new node and it becomes the new front

    def push_right(self, data):
        new_node = Node(data)
        if self.right is None:
            self.left = self.right = new_node #If queue is empty both ends are the same
        else:
            new_node.previous = self.right #Link the new node to the current right node
            self.right.next = new_node
            self.right = new_node #Update right to the new node and it becomes the new rear

    def pop_left(self):
        if self.left is None:
            print("El deque esta vacio")
            return None
        value = self.left.data #Store the value of the current left node before removing it
        self.left = self.left.next #Move the left pointer to the next node
        if self.left is not None:
            self.left.previous = None #If there is still a node, remove the previous link
        else:
            self.right = None #If the deque is empty, reset the right pointer too
        return value

    def pop_right(self):
        if self.right is None:
            print("El deque esta vacio")
            return None
        value = self.right.data #Store the value of the current right node before removing it
        self.right = self.right.previous #Move the right pointer to the previous node
        if self.right is not None:
            self.right.next = None #If there is still a node, remove the next link
        else:
            self.left = None #If the deque is now empty, reset the left pointer too
        return value

    def print_deque(self):
        if self.left is None:
            print("El deque esta vacio")
            return
        current = self.left
        print("Deque (Izquierda a Derecha):")
        while current: #Prints the deque from left to right with each node's data
            print(f" - {current.data}")
            current = current.next
            print(f" - {current.data}")
            current = current.next


#Test
dq = Deque()

dq.push_left(1) #Data combination of FIFO and LIFO
dq.push_left(2)
dq.push_right(3)
dq.push_right(4)
dq.print_deque()

print(f'Eliminado de la izquierda {dq.pop_left()}')
print(f'Eliminado de la derecha {dq.pop_right()}')

dq.print_deque()