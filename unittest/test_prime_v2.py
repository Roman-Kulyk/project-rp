import unittest
from prime_v1 import is_prime

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        """Test for 'prime numbers'"""
        for number in [2, 3, 5, 7, 11, 13, 17, 19]:
            with self.subTest(number=number):
                self.assertTrue(is_prime(number))

    def test_non_prime_number(self):
        """Test for 'non_prime numbers'"""
        for number in [4, 6, 8, 9, 12, 14, 15, 16, 18]:
            with self.subTest(number=number):
                self.assertFalse(is_prime(number))
            
if __name__=="__main__":  # it makes module executable
    unittest.main(verbosity=2)  # ()main function from unittest allows to load and run 
    # a set of tests