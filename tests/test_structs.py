#!/usr/bin/python

import unittest
from JAGpy.Structs import lookup


class Test_Structs(unittest.TestCase):
    def test_lookup(self):

        my_set = {1, 2, 3}
        self.assertEqual(lookup(my_set, 1), True, 'Lookup (1) for set ok')
        self.assertEqual(lookup(my_set, 4), None, 'Lookup() for None for set ok')
        self.assertEqual(lookup(my_set, 4, 'blah'), 'blah', 'Lookup() for missing with if none for set ok')

        my_list = [4, 5, 6]
        self.assertEqual(lookup(my_list, 4), 4, 'Lookup (1) for list ok')
        self.assertEqual(lookup(my_list, 4), None, 'Lookup() for None for list ok')
        self.assertEqual(lookup(my_list, 4, 'blah'), 'blah', 'Lookup() for missing with if none for list ok')

        my_dict = dict(a=7, b=8, c=9)
        self.assertEqual(lookup(my_dict, 'a'), 7, 'Lookup (1) for dict ok')
        self.assertEqual(lookup(my_dict, 'd'), None, 'Lookup() for None for dict ok')
        self.assertEqual(lookup(my_dict, 'd', 'blah'), 'blah', 'Lookup() for missing with if none for dict ok')

