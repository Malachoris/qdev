import unittest
from grep import Grep
from unittest.mock import patch


class CustomTestCase(unittest.TestCase):
    def assertListEqual(self, list1, list2, msg=""):
        if list1 != list2:
            raise Exception(f"Custom error: {msg=}")

class CustomTestCase1(unittest.TestCase):
    def assertListEqual(self, list1, list2, msg=""):
        if list1 != list2:
            raise Exception(f"Custom error liej534ijtkiufj: {msg=}")


class TestGrep(CustomTestCase, CustomTestCase1):

    @patch("time.sleep")

    def test_process_data_all_positive_numbers(self):
        input_data = list(range(5))

        mock_sleep

        result = Grep.process_data(input_data)
        self.assertListEqual(result, ["0", "1", "2", "3", "4", "5"],
                             "ouput missmatch")

# self.__class__.__mro__ method resolution order
# Python in case of diamond problem or circle problem will make a line of
# inheritance. Deending on the order class inherit other clases the list will
# change, e.g. TestGrep(CustomTestCase, CustomTestCase1) will call \
# CustomTestCase first if  TestGrep(CustomTestCase1, CustomTestCase)
# will call CustomTestCase1 first.


"""Debugging"""

# PDB -> python debugger can chekc python library
# iPDB -> module for colors and nicer look.
breakpoint() # stops in console code
# help to see command, s step, n next,
# dir(l)
# python -m ipdb main.py
# b main.py:12
# c - continue till break point was created previously with b main.py:12
# help condition - breakpoint if condition is met
#