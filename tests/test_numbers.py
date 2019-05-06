#!/usr/bin/python

import unittest
from collections import namedtuple
from JAGpy.Numbers import intify

TestCase = namedtuple('test_case', 'name value expected')


class Test_Numbers(unittest.TestCase):

    def test_intify(self):
        tests = [
            TestCase('string_int', '4', 4),
            TestCase('int', 5, 5),
            TestCase('float', '6.3', '6.3'),
            TestCase('blah', 'blah', 'blah'),
        ]

        for test in tests:
            print(f"Testing: intify('{test.value}') => {test.expected}")
            self.assertEqual(intify(test.value), test.expected,
                             f"Intify '{test.value}' => {test.expected}: ok")

