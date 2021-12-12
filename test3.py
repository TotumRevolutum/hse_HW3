import unittest
from main import *


class TestCaseType(unittest.TestCase):
    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            open_file('text3.txt')


if __name__ == '__main__':
    unittest.main()
