#Ejercicio Extra OOP 3

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = [] #List to store product objects

    def add_product(self, product):
        self.products.append(product) #Appends a product to the list

    def show_products(self):
        for product in self.products: #Runs through the list to show products
            print(f'Producto: {product.name}, Precio: {product.price}, Cantidad: {product.quantity}')

    def calculate_total_inventory_value(self):
        total = 0
        for product in self.products:
            total = total + product.price * product.quantity #Calculates the sum of the products and saves the value
        return total


#Creates Objects
product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)
product3 = Product("Headset", 10000, 4)
inventory = Inventory()

inventory.add_product(product1) #Add products
inventory.add_product(product2) #Add products
inventory.add_product(product3) #Add products

inventory.show_products() #Show products

print(f'El valor del inventario es de: {inventory.calculate_total_inventory_value()}')