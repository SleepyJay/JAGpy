#!/usr/bin/python

import unittest
from collections import namedtuple
from JAGpy.Structs import lookup, has_item, list_to_set_without

LookupTest = namedtuple('lookup_test', 'name, collection, good_key, expected_good, bad_key')


class Test_Structs(unittest.TestCase):

    def test_lookup(self):
        tests = [
            LookupTest('set', {1, 2, 3}, 1, 1, 4),
            LookupTest('list', [4, 5, 6], 1, 5, 4),
            LookupTest('dict', dict(a=7, b=8, c=9), 'a', 7, 'd'),
            LookupTest('tuple', (4, 5, 6), 1, 5, 4),
        ]

        # You probably wouldn't use `lookup` with namedtuple, but...
        tests.append(LookupTest('namedtuple', tests[0], 0, 'set', 12))

        if_none = 'blah'
        for test in tests:
            self.assertEqual(lookup(test.collection, test.good_key), test.expected_good,
                             f"Lookup ({test.good_key}) for '{test.name}': ok")
            self.assertEqual(lookup(test.collection, test.bad_key), None,
                             "Lookup() is None for '{test.name}': ok")
            self.assertEqual(lookup(test.collection, test.bad_key, if_none), if_none,
                             "Lookup() for missing with if_none for set ok")

    def test_has_item(self):
        tests = [
            LookupTest('set', {1, 2, 3}, 1, True, 4),
            LookupTest('list', [4, 5, 6], 4, True, 7),
            LookupTest('dict', dict(a=7, b=8, c=9), 'a', True, 'd'),
            LookupTest('tuple', (4, 5, 6), 4, True, 7),
        ]

        if_none = 'blah'
        for test in tests:
            self.assertEqual(has_item(test.collection, test.good_key), test.expected_good,
                             f"Lookup ({test.good_key}) for '{test.name}': ok")
            self.assertEqual(has_item(test.collection, test.bad_key), None,
                             "Lookup() is None for '{test.name}': ok")
            self.assertEqual(has_item(test.collection, test.bad_key, if_none), if_none,
                             "Lookup() for missing with if_none for set ok")

    def test_list_to_set_without(self):
        my_list = [4, 5, 6, 4, 7]
        my_without = [5]
        my_expected = {4, 6, 7}

        my_actual = list_to_set_without(my_list, my_without)

        self.assertEqual(my_actual, my_expected, f"Lookup list to set without: ok")