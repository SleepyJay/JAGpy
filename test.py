#!/usr/bin/python

import sys, os

relative_to_me = '../JAGpy'

base_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(base_dir, relative_to_me)))

from JAGpy import Pyrove

Pyrove.run_tests()
