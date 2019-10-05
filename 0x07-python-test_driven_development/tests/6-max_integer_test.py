#!/usr/bin/python3
"""Unittext for max_integer([..]) """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """ Test case normal """

        self.assertAlmostEqual(max_integer([50, 40, 60, 30]), 60)

    def test_multiple_max(self):
        """ Test case with multiple Max """

        self.assertAlmostEqual(max_integer([100, 100, 60, 40]), 100)

    def test_raise_errors(self):
        """ Raising Errors """

        self.assertRaises(TypeError, max_integer, None)

    def test_negative(self):
        """ gives the bigger negative """

        self.assertAlmostEqual(max_integer([-100, -200, -4, -300]), -4)

    def test_only_number(self):
        """ Test only number """

        self.assertAlmostEqual(max_integer([100]), 100)

    def test_tupla(self):
        """ test a tupla """

        self.assertAlmostEqual(max_integer((1, 3, 4, 6, 10)), 10)

    def test_type_err(self):
        """ test error with string """

        self.assertRaises(TypeError, max_integer, [1, 3, "alo", 4])

    def test_floats(self):
        """ test which float is bigger """

        self.assertEqual(max_integer([2.3, 2.5, 8.99]), 8.99)

    def test_strings(self):
        """ test strings tuplas """
        self.assertAlmostEqual(max_integer("hOLA"), "h")

    def test_character(self):
        """ test character by character """
        self.assertAlmostEqual(max_integer('h'), 'h')

    def test_tuplastrings(self):
        """ test error tupla strings """
        self.assertAlmostEqual(max_integer([("hol"), ("ad")]), "hol")

    def test_emptylist(self):
        """ test error for empty matrix """
        self.assertAlmostEqual(max_integer(), None)

    def test_emptylistMatrix(self):
        """ test error empty list in matrix """
        self.assertAlmostEqual(max_integer([]), None)
