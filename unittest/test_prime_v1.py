import unittest
from  prime_v1 import is_prime


class TestIsPrime(unittest.TestCase):
    """Comparing Values"""
    def test_prime_number(self):
        """Test for 'prime number'"""
        self.assertTrue(is_prime(17))

    def test_non_prime_number(self):
        """Test for 'not prime number'"""
        self.assertFalse(is_prime(10))

if __name__=="__main__":  # it makes module executable
    unittest.main(verbosity=2)  # ()main function from unittest allows to load and run 
    # a set of tests
