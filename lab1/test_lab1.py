import unittest
from lab1 import Add

class Testlab1(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Add(""), 0)

    def test_one_string(self):
        self.assertEqual(Add("1"), 1)

    def test_two_string(self):
        self.assertEqual(Add("1,2"), 3)

    def test_multiple_string(self):
        self.assertEqual(Add("1,2,3,4"), 10)

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            Add("1,a,3")

    def test_newline(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_invalid_newline(self):
        with self.assertRaises(ValueError):
            Add("1,\n2,3")

if __name__ == '__main__':
    unittest.main()