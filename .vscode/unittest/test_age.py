import unittest
import sys
from age import categorize_gy_age


class TestCategorizeByAge(unittest.TestCase):
    @unittest.skip("Unconditionally skipped test")
    def test_child(self):
        """Test for 'Child'"""
        self.assertEqual(categorize_gy_age(5), "Child")
    
    @unittest.skipIf(sys.version_info < (3,12), "Requires Python >= 3.12")
    def test_adolescent(self):
        """Test for 'Adolescent'"""
        self.assertEqual(categorize_gy_age(15), "Adolescent")

    @unittest.skipUnless(sys.platform.startswith("win"), "Requires Windows")
    def test_adult(self):
        """Test for 'Adult'"""
        self.assertEqual(categorize_gy_age(30), "Adult")

    def test_golden_age(self):
        """Test for 'Golden age'"""
        self.assertEqual(categorize_gy_age(70), "Golden age")

    def test_negative_age(self):
        """Test for 'negative age'"""
        self.assertEqual(categorize_gy_age(-2), "Invalid age: -2")

    def test_too_old(self):
        """Test for 'too old'"""
        self.assertEqual(categorize_gy_age(151), "Invalid age: 151")
     
    def test_boundary_child_adolescent(self):
        """Test for boundary between 'Child' and 'Adolescent'"""
        self.assertEqual(categorize_gy_age(9), "Child")
        self.assertEqual(categorize_gy_age(18), "Adolescent")

    def test_boundary_adolescent_adult(self):
        """Test for boundary between 'Adolescent' and 'Adult'"""
        self.assertEqual(categorize_gy_age(18),"Adolescent")
        self.assertEqual(categorize_gy_age(19),"Adult")

    def test_boundary_adult_golden_age(self):
        """Test for boundary between 'Adult' and Golden age'"""
        self.assertEqual(categorize_gy_age(65), "Adult")
        self.assertEqual(categorize_gy_age(66), "Golden age")

if __name__=="__main__":  # it makes module executable
    unittest.main(verbosity=2)  # ()main function from unittest allows to load and run 
    # a set of tests