# This is kinda ugly boilerplate for every test... :(
try:
    # PyCharm (et al) set up testing better and probably don't need to back-ref dirs
    import Looper 
except:
    # Anything else (Pythonista :( ) may just simply use this script at the top-level, so add '..'
    import sys
    sys.path.append('..')
    
    import Looper

import unittest
from collections import Counter
from helpers import list_01_by_3

class Test_Looper(unittest.TestCase):
    #
    def test_list(self):
        items = Looper.list(0, 2, 3)
        boring = list_01_by_3()

        print("Test: items == boring")
        self.assertEqual(Counter(map(str,items)), Counter(map(str,boring)))

if __name__ == '__main__':
    unittest.main(verbosity=2)
