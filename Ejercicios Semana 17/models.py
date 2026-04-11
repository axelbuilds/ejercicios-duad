from datetime import datetime

class AccountActivity:
    #Class for financial transaction Income or Expense
    def __init__(self, title, amount, category, type, date=None):
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.type = type
        #If no date is provided, uses today date
        self.date = date if date else datetime.now().strftime('%d/%m/%Y') # DD/MM/YY date format

    def to_dictionary(self):
        #Converts the object instance to a dictionary for JSON format
        return {
            "titulo": self.title,
            "monto": self.amount,
            "categoria": self.category,
            "tipo": self.type,
            "fecha": self.date
        }

    @staticmethod
    def from_dictionary(data):
        #Creates an AccountActivity object from a dictionary
        return AccountActivity(**data)