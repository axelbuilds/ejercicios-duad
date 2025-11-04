#Ejercicio Estructura de datos 3

class Node:
    def __init__(self, data):
        self.data = data #Stores node's value
        self.left = None #Points to left child node
        self.right = None #Points to right child node


class BinaryTree:
    def __init__(self):
        self.root = None #Root node of the tree

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node #If root is empty set as root
            return value
        
        current = self.root
        while True:
            if value < current.data: 
                if current.left is None: #Go left
                    current.left = new_node
                    return value
                current = current.left
            
            else:
                if current.right is None: #Go right
                    current.right = new_node
                    return value
                current = current.right

    def print_tree(self):
        if self.root is None:
            print("El árbol está vacío")
        else:
            self.print_inorder(self.root) #Calls recursive method to print left to right

    def print_inorder(self, node):
        if node is not None: #Checks if the node exists
            self.print_inorder(node.left) #Checks for left child node first
            print(node.data)
            self.print_inorder(node.right) #Checks for right child node last


#Test
tree = BinaryTree()
tree.insert(5)
tree.insert(7)
tree.insert(2)
tree.insert(8)
tree.insert(1)
tree.insert(3)
tree.insert(6)

tree.print_tree()