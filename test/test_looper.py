import unittest
#import Looper
from collections import Counter
from helpers import list_01_by_3

import importlib
importlib.import_module('Looper')

class Test_Looper(unittest.TestCase):
    #
    def test_list(self):
        items = Looper.list(0, 2, 3)
        boring = list_01_by_3()

        print("Test: items == boring")
        self.assertEqual(Counter(map(str,items)), Counter(map(str,boring)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
