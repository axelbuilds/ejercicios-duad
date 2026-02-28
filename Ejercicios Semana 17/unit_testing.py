import unittest
from finance_logic import FinanceManager

class TestFinance(unittest.TestCase):
    def setUp(self):
        #Clean instance for each test
        self.manager = FinanceManager()
        self.manager.transactions = []
        self.manager.categories = ["Test"]

    def test_add_income_success(self):
        #Add a normal income
        res, _ = self.manager.add_transaction("ingreso", "Salario", "500", "Test")
        self.assertTrue(res)

    def test_balance_is_correct(self):
        #Balance calculation
        self.manager.add_transaction("ingreso", "A", "100", "Test")
        self.manager.add_transaction("gasto", "B", "40", "Test")
        self.assertEqual(self.manager.get_balance(), "60.00")

    def test_empty_title(self):
        #Title validation
        res, _ = self.manager.add_transaction("ingreso", "", "100", "Test")
        self.assertFalse(res)

    def test_invalid_monto(self):
        #Text in amount field
        res, _ = self.manager.add_transaction("ingreso", "A", "abc", "Test")
        self.assertFalse(res)

    def test_zero_amount(self):
        #Zero amount validation
        res, _ = self.manager.add_transaction("gasto", "A", "0", "Test")
        self.assertFalse(res)

    def test_duplicate_cat(self):
        #Duplicate category validation
        self.manager.add_category("Ahorro")
        res, _ = self.manager.add_category("Ahorro")
        self.assertFalse(res)

    def test_transaction_list_size(self):
        #Verify list growth
        self.manager.add_transaction("ingreso", "X", "10", "Test")
        self.assertEqual(len(self.manager.transactions), 1)

    def test_formatted_data_type(self):
        #Ensure GUI receives a list of lists
        self.manager.add_transaction("ingreso", "X", "10", "Test")
        data = self.manager.get_formatted_data()
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], list)

if __name__ == "__main__":
    unittest.main()