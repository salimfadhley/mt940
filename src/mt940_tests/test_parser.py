from mt940.parser import parse
import unittest


class TestMT940Parser(unittest.TestCase):

    def test_basic(self):
        message = "{}"
        expected = {}
        self.assertEqual(expected, parse(message))

