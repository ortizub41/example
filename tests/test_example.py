#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_example
----------------------------------

Tests for `example` module.
"""

import unittest

import example


class TestExample(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(example.hello_world())
        pass

    def tearDown(self):
        pass
