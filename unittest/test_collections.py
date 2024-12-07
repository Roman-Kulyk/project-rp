import unittest


class TestCollections(unittest.TestCase):
    """Comparing Collections"""
    def test_sequence_objects(self):
        a = ("H","e","l","l","o")
        b = "Hello"
        self.assertSequenceEqual(a, b)

    def test_stttring_objects(self):
        a = "Hello"
        b = "Hello"
        self.assertMultiLineEqual(a, b)

    def test_list_objects(self):
        a = [1,2,3,4,5]
        b = [1,2,3,4,5]
        self.assertListEqual(a, b)

    def test_tuple_objects(self):
        a = ("Jane", 25, "NewYork")
        b = ("Jane", 25, "NewYork")
        self.assertTupleEqual(a, b)

    def test_dictionary_objects(self):
        a = {'a': 1, 'b': 2}
        b = {'a': 1, 'b': 2}
        self.assertDictEqual(a, b)

    def test_set_objects(self):
        a = {1,2,4,3,5}
        b = {1,5,3,4,2}
        self.assertSetEqual(a, b)

if __name__=="__main__":  # it makes module executable
    unittest.main(verbosity=2)  # ()main function from unittest allows to load and run 
    # a set of tests