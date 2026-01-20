#Ejercicios Unit Testing 2

import unittest
from ejercicios_semana_6 import sum_list, string_func, uppercase_count, lowercase_count

class UnitTesting(unittest.TestCase):

    # Unit Test for sum_list
    def test_sum_list_standard(self):
        #Sum for positive numbers
        self.assertEqual(sum_list([3, 5, 7, 10]), 25)

    def test_sum_list_negatives(self):
        #Sum for positive and negative numbers
        self.assertEqual(sum_list([-10, 5, -5, 20]), 10)

    def test_sum_list_empty(self):
        #Empty values to return 0
        self.assertEqual(sum_list([]), 0)


    # Unit Test for string_func (Reverse
    def test_string_func_basic(self):
        #Reverse simple string
        self.assertEqual(string_func("Hola"), "aloH")

    def test_string_func_sentence(self):
        #Reverse phrase with spaces
        self.assertEqual(string_func("Hola Mundo"), "odnuM aloH")

    def test_string_func_palindrome(self):
        #Reads the same word backwards
        self.assertEqual(string_func("ana"), "ana")


    # Unit Test uppercase_count and lowercase_count
    def test_counts_mixed_case(self):
        #Mixes upper and lower case
        text = "I Love Programming"
        self.assertEqual(uppercase_count(text), 3)
        self.assertEqual(lowercase_count(text), 13)

    def test_counts_only_numbers_symbols(self):
        #Symbols and numbers must be 0
        text = "12345!@#$ "
        self.assertEqual(uppercase_count(text), 0)
        self.assertEqual(lowercase_count(text), 0)

    def test_counts_all_upper(self):
        #Only upper case
        text = "HELLO"
        self.assertEqual(uppercase_count(text), 5)
        self.assertEqual(lowercase_count(text), 0)

if __name__ == '__main__':
    unittest.main()