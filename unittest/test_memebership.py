import unittest


class TestMembership(unittest.TestCase):
    """Running Membership Tests"""
    def test_value_in_collection(self):
        a = 1
        b = [1,2,3,4,5]
        self.assertIn(a, b)

    def test_value_not_in_collection(self):
        a = 10
        b = [1,2,3,4,5]
        self.assertNotIn(a, b)

if __name__=="__main__":  # it makes module executable
    unittest.main(verbosity=2)  # ()main function from unittest allows to load and run 
    # a set of tests