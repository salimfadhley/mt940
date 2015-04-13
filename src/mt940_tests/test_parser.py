import unittest

from mt940.parser import parse, tokenize


class TestMT940Parser(unittest.TestCase):
    def test_tokenize_simple_message(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}"
        result = tokenize(message)
        types = [t[0] for t in result]
        self.assertEqual(types, ['{', 'NUMERIC', 'COLON', 'ALPHANUMERIC', '}'])


    def test_header_block_one(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}"
        expected = {1:'F01HBOSXXXXAXXX9999999999'}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}"
        expected = {1:'F01HBOSXXXXAXXX9999999999', 2:'I940HBOSXXXXXXXXN'}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two_and_four(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n-}"
        expected = {1: 'F01HBOSXXXXAXXX9999999999', 2: 'I940HBOSXXXXXXXXN', 4: {}}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two_and_four_with_content(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n:61:FOO\n-}"
        expected = {1:'F01HBOSXXXXAXXX9999999999', 2:'I940HBOSXXXXXXXXN', 4:{"61":"FOO"}}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two_and_four_with_multiple_fields(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n:FOO:BLAH\n:FOD:FIB\n-}"
        expected = {1: 'F01HBOSXXXXAXXX9999999999', 2: 'I940HBOSXXXXXXXXN', 4: {"FOO": "BLAH", "FOD": "FIB"}}
        self.assertEqual(expected, parse(message))

        # def test_header_block_one_and_two_and_four_with_ugly_data(self):
        #     message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n:FOO:BLAH\n:FOD:JHKDKD DKLHDLH\nKJDHKDH\nIIIEEE\n-}"
        #     expected = {1:'F01HBOSXXXXAXXX9999999999', 2:'I940HBOSXXXXXXXXN', 4:{"FOO":"BLAH", "FOD":"FIB"}}
    #     self.assertEqual(expected, parse(message))



