import unittest
import numpy as np
from main import *


class TestCase(unittest.TestCase):
    def test_maxi(self):
        self.assertEqual(maxi(open_file('text.txt')), max(open_file('text.txt')))

    def test_mini(self):
        self.assertEqual(mini(open_file('text.txt')), min(open_file('text.txt')))

    def test_summa(self):
        self.assertEqual(summa(open_file('text.txt')), sum(open_file('text.txt')))

    def test_mult(self):
        self.assertEqual(multi(open_file('text.txt')), np.prod(open_file('text.txt')))


if __name__ == '__main__':
    unittest.main()
