import unittest
from even import is_even


class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        """Test for 'even number'"""
        self.assertEqual(is_even(2), True)

    def test_odd_number(self):
        """Test for 'odd number'"""
        self.assertEqual(is_even(3), False)

    def test_negative_even_number(self):
        """Test for 'negative even number'"""
        self.assertEqual(is_even(-2), True)

    def test_negative_odd_number(self):
        """Test for 'negative odd number'"""
        self.assertEqual(is_even(-3), False)

    def test_zero(self):
        """Test for 'zero'"""
        self.assertEqual(is_even(0), True)

if __name__=="__main__":
    unittest.main(verbosity=2)
                         
                         
                         
                