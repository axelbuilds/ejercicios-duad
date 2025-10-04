#Ejercicios 4 Pilares de OOP #1

class BankAccount(): #Constructor
    def __init__(self, balance = 0):
        if balance < 0: #Condition for negative balance
            raise ValueError("El balance no puede ser negativo")
        self.balance = balance


    def add_balance(self, amount): #Function to add to balance
        if amount <= 0:
            raise ValueError("El monto debe ser mayor a $0")
        self.balance = self.balance + amount


    def withdraw_balance(self, amount): #Function to substract from balance
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if amount > self.balance: 
            raise ValueError("Fondos insuficientes")
        self.balance = self.balance - amount



class SavingsAccount(BankAccount): #Inhirited class from BankAccount
    def __init__(self, min_balance = 0, balance = 0):
        if balance < min_balance: #Validation of initial balance
            raise ValueError("El balance inicial no puede ser menor al minimo permitido")
        BankAccount.__init__(self, balance) #Calls the constructor
        self.min_balance = min_balance #Saves the minimum balance as attribute


    def withdraw_balance(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor a $0")
        if self.balance - amount < self.min_balance: #Validates the withdrawal is not higher than the balance allowed
            raise Exception("El monto es mayor al minimo permitido")
        BankAccount.withdraw_balance(self, amount)


bank_account = BankAccount()
bank_account.add_balance(1000)
bank_account.withdraw_balance(200)
bank_account.withdraw_balance(1500)
print(f'El balance de la cuenta es {bank_account.balance}')


savings = SavingsAccount(min_balance = 300, balance = 1000)
savings.withdraw_balance(400)
savings.withdraw_balance(300)
print(f'El balance de la ahorros es {savings.balance}')


savings1 = SavingsAccount(min_balance=200, balance=500)
print(f"Cuenta de ahorros con balance {savings1.balance} y minimo {savings1.min_balance}")

bank_account1 = BankAccount()
bank_account1.add_balance(-50)
savings1.withdraw_balance(-50)