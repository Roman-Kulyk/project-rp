import unittest
from even import is_even

class TestIsEven(unittest.TestCase):
    """Creating SubTests"""
    def test_even_numbers(self):
        """Test for 'even numbers'"""
        for number in [2, 4, 6, -8, -10, -12]:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), True)

    def test_odd_numbers(self):
        """Test for 'odd numbers'"""
        for number in [1, 3, 5, -7, -9, -11]:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), False)

if __name__=="__main__":  # it makes module executable
    unittest.main(verbosity=2)  # ()main function from unittest allows to load and run 
    # a set of tests