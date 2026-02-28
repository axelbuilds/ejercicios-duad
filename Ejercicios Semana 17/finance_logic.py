import json
import os
import csv
from models import AccountActivity

#Manager Class
class FinanceManager:

    DATA_FILE = 'finance_data.json'

    def __init__(self):
        self.categories = []
        self.transactions = []
        self.load_data()

    def load_data(self):
        #Loads data from the JSON file or sets defaults if file does not exist
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                #Loads existing categories or uses default ones
                self.categories = data.get(
                    'categories',
                    ["Comida", "Salario", "Transporte", "Ahorro"]
                )

                raw_tx = data.get('transactions', [])

                #Creates AccountActivity objects from stored JSON data
                self.transactions = [
                    AccountActivity(
                        title=t["titulo"],
                        amount=t["monto"],
                        category=t["categoria"],
                        type=t["tipo"],
                        date=t["fecha"]
                    )
                    for t in raw_tx
                ]

            except Exception as e:
                print(f"Error loading data: {e}")
                self.defaults()
        else:
            self.defaults()

    def defaults(self):
        #Sets default values for a new environment
        self.categories = ["Comida", "Salario", "Transporte", "Ahorro"]
        self.transactions = []

    def save_data(self):
        #Saves current categories and transactions to the JSON file
        data = {
            'categories': self.categories,
            'transactions': [t.to_dictionary() for t in self.transactions]
        }

        with open(self.DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    # ====================================
    # Data Management
    # ====================================

    def clear_history(self):
        #Deletes all recorded transactions
        try:
            self.transactions = []
            self.save_data()
            return True, "El historial ha sido eliminado."
        except Exception as e:
            return False, f"Error al eliminar: {e}"

    def add_category(self, new_category):
        #Validates new category
        if not new_category or not new_category.strip():
            return False, "El nombre no puede estar vacío"

        name = new_category.strip().capitalize()

        if name in self.categories:
            return False, "Esta categoría ya existe"

        self.categories.append(name)
        self.save_data()
        return True, "La categoría se agregó con éxito"

    def add_transaction(self, trans_type, title, amount_str, category):
        #Validates and records a new income or expense

        if not title or not title.strip():
            return False, "El título no puede estar vacío"

        try:
            #Clean strings for possible comma decimals
            clean_amount = amount_str.replace(',', '.')
            amount = float(clean_amount)

            if amount <= 0:
                raise ValueError

        except ValueError:
            return False, "Monto inválido. Ingrese un número positivo"

        new_entry = AccountActivity(
            title.strip(),
            amount,
            category,
            trans_type
        )

        self.transactions.append(new_entry)
        self.save_data()
        return True, "Movimiento guardado"

    def get_balance(self):
        #Calculates and formats the total net balance
        total = sum(
            t.amount if t.type == 'ingreso'
            else -t.amount
            for t in self.transactions
        )
        return f"{total:.2f}"

    def get_formatted_data(self):
        #Returns a list of transactions formatted for the UI Table
        return [
            [f"{t.amount:,.2f}", t.title, t.category, t.date]
            for t in reversed(self.transactions)
        ]

    def get_categories(self):
        #Returns the current list of categories
        return self.categories

    # ====================================
    # CSV Export Logic
    # ====================================

    def export_to_csv(self, filepath):
        #Generates a CSV file with all transactions and summary totals
        try:
            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                #Header row
                writer.writerow(['Fecha', 'Título', 'Monto', 'Categoría', 'Tipo'])

                total_income = 0
                total_expenses = 0

                for t in self.transactions:
                    writer.writerow([t.date, t.title, t.amount, t.category, t.type])

                    if t.type == 'ingreso':
                        total_income += t.amount
                    else:
                        total_expenses += t.amount

                # Summary Section
                writer.writerow([])
                writer.writerow(['TOTALES'])
                writer.writerow(['Ingresos', f"{total_income:.2f}"])
                writer.writerow(['Gastos', f"{total_expenses:.2f}"])
                writer.writerow(['Balance Neto', f"{(total_income - total_expenses):.2f}"])

            return True, f"Archivo guardado en: {filepath}"

        except Exception as e:
            return False, f"Error al exportar: {e}"