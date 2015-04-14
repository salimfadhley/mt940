import unittest

from mt940.parser import parse, tokenize


class TestMT940Parser(unittest.TestCase):
    def test_tokenize_simple_message(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}"
        result = tokenize(message)
        types = [t[0] for t in result]
        self.assertEqual(types, ['{', 'NUMERIC', 'COLON', 'ALPHANUMERIC', '}'])


    def test_tokenize_ugly_message(self):
        message = "{1:X}{2:Y}{4\n:A:B\nC\n-}"
        result = tokenize(message)
        types = [t[0] for t in result]
        self.assertEqual(types, [
            '{', 'NUMERIC', 'COLON', 'ALPHANUMERIC', '}',
            '{', 'NUMERIC', 'COLON', 'ALPHANUMERIC', '}',
            '{', 'NUMERIC', 'FIELD_SEPARATOR', 'ALPHANUMERIC', 'COLON', 'ALPHANUMERIC', 'NEWLINE',
            'ALPHANUMERIC', 'TERMINAL_FIELD', '}'
        ])

    def test_header_block_one(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}"
        expected = {"1": 'F01HBOSXXXXAXXX9999999999'}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}"
        expected = {"1": 'F01HBOSXXXXAXXX9999999999', "2": 'I940HBOSXXXXXXXXN'}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two_and_four(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n-}"
        expected = {"1": 'F01HBOSXXXXAXXX9999999999', "2": 'I940HBOSXXXXXXXXN', "4": []}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two_and_four_with_content(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n:61:FOO\n-}"
        expected = {"1": 'F01HBOSXXXXAXXX9999999999', "2": 'I940HBOSXXXXXXXXN', "4": [("61", "FOO")]}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two_and_four_with_multiple_fields(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n:FOO:BLAH\n:FOD:FIB\n-}"
        expected = {"1": 'F01HBOSXXXXAXXX9999999999', "2": 'I940HBOSXXXXXXXXN', "4": [("FOO", "BLAH"), ("FOD", "FIB")]}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two_and_four_newlines_in_data(self):
        message = "{1:X}{2:Y}{4:\n:A:B\nC\n-}"
        expected = {"1": 'X', "2": 'Y', "4": [("A", "B\nC")]}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_colons_in_data(self):
        message = "{1:X}{2:Y}{4:\n:A:B:C\n-}"
        expected = {"1": 'X', "2": 'Y', "4": [("A", "B:C")]}
        self.assertEqual(expected, parse(message))

    def test_header_block_four_with_commas_in_data(self):
        message = "{1:X}{2:Y}{4:\n:A:B, C\n-}"
        expected = {"1": 'X', "2": 'Y', "4": [("A", "B, C")]}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_colons_and_newlines_in_data(self):
        message = "{1:X}{2:Y}{4:\n:A:B:C\nD\n-}"
        expected = {"1": 'X', "2": 'Y', "4": [("A", "B:C\nD")]}
        self.assertEqual(expected, parse(message))

    def test_block_four_with_alphanumeric_field_headers(self):
        message = "{1:X}{2:Y}{4:\n:28A:XXX\n:34D:YYY\n-}"
        expected = {"1": 'X', "2": 'Y', "4": [("28A", "XXX"), ("34D", "YYY")]}
        self.assertEqual(expected, parse(message))

    def test_fields_with_subfields(self):
        message = "{3:{108:X}}"
        expected = {"3": {"108": "X"}}
        self.assertEqual(expected, parse(message))



