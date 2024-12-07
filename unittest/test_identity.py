import unittest


class TestListIdentity(unittest.TestCase):
    """Comparing Objects by Their Identity"""
    def test_list_aliases(self):
        a = ["Python", "unittest"]
        b = a
        self.assertIs(a,b)

    def test_list_objects(self):
        a = ["Python", "unittest"]
        b = ["Python", "unittest"]
        self.assertIsNot(a, b)

if __name__=="__main__":  # it makes module executable
    unittest.main(verbosity=2)  # ()main function from unittest allows to load and run 
    # a set of tests