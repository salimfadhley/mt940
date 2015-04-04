from mt940.parser import parse
import unittest


class TestMT940Parser(unittest.TestCase):

    def test_basic(self):
        message = "{}"
        expected = {}
        self.assertEqual(expected, parse(message))

    def test_single_key(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}"
        expected = {1:"F01HBOSXXXXAXXX9999999999"}
        self.assertEqual(expected, parse(message))

