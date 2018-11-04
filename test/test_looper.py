import unittest
import Looper
from collections import Counter
from test.helpers import list_01_by_3


class Test_Looper(unittest.TestCase):
    #
    def test_list(self):
        items = Looper.list(0, 2, 3)
        boring = list_01_by_3()

        print("Test: items == boring")
        self.assertEqual(Counter(map(str,items)), Counter(map(str,boring)))



