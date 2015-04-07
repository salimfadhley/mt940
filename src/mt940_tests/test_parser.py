import unittest

from mt940.parser import parse, tokenize


class TestMT940Parser(unittest.TestCase):

    def test_basic(self):
        message = "{}"
        expected = {}
        self.assertEqual(expected, parse(message))

    def test_tokenize_28c(self):
        message = "{:28C:00065/001}"
        tokenize(message)

    def test_tokenize_61(self):
        message = "{:61:0501120112DN449,77\nNTRF\nREFKLI1234567890//BR05012139000001944-PRZEL.KRAJ.WYCH.MT.ELX}"
        tokenize(message)

    def test_single_key(self):
        message = "{:28C:00065/001}"
        expected = {'Statement Number/Sequence Number':(65,1)}
        self.assertEqual(expected, parse(message))

    def test_reference_number(self):
        message = "{:20:2267602902375194}"
        expected = {"Reference Number":2267602902375194}
        self.assertEqual(expected, parse(message))

    def test_multiple_keys(self):
        message = "{:20:2267602902375194\n:28C:00065/001}"
        expected = {"Reference Number":2267602902375194, 'Statement Number/Sequence Number':(65,1)}
        self.assertEqual(expected, parse(message))

