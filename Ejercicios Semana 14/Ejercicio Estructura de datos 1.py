#Ejercicio Estructura de Datos #1

class Node:
    def __init__(self, data):
        self.data = data #Saves node's value
        self.next = None #Next node in the stack


class Stack:
    def __init__(self):
        self.top = None #Last node added to the stack

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top #New node is the previous at the top
        self.top = new_node #New node is the top

    def pop(self):
        if self.top is None:
            print("El stack esta vacio")
            return None
        value = self.top.data
        self.top = self.top.next #Top now points to the next node
        return value

    def print_stack(self):
        current = self.top
        if current is None:
            print("El stack esta vacio")
            return
        print("Stack:")
        while current: #Prints data from the top until there are no nodes left
            print(f'{current.data}')
            current = current.next


#Test
stack = Stack()

stack.push(1) #Data to stack LIFO
stack.push(2)
stack.push(3)
stack.print_stack()

print(f'Dato eliminado: {stack.pop()}')
stack.print_stack()