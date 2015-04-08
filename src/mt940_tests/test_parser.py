import unittest

from mt940.parser import parse, tokenize
import pkg_resources


class TestMT940Parser(unittest.TestCase):

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
        expected = {1:'F01HBOSXXXXAXXX9999999999', 2:'I940HBOSXXXXXXXXN', 4:{}}
        self.assertEqual(expected, parse(message))

    def test_header_block_one_and_two_and_four_with_content(self):
        message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n:61:FOO\n-}"
        expected = {1:'F01HBOSXXXXAXXX9999999999', 2:'I940HBOSXXXXXXXXN', 4:{"61":"FOO"}}
        self.assertEqual(expected, parse(message))

    # def test_header_block_one_and_two_and_four_with_tricky_content(self):
    #     message = "{1:F01HBOSXXXXAXXX9999999999}{2:I940HBOSXXXXXXXXN}{4:\n:FOO:BLAH\n:FOD:AB CD\n-}"
    #     expected = {1:'F01HBOSXXXXAXXX9999999999', 2:'I940HBOSXXXXXXXXN', 4:{"FOO":"BLAH", "FOD":"12 34"}}
    #     self.assertEqual(expected, parse(message))

    # def test_sample_data(self):
    #     message = pkg_resources.resource_string('mt940_tests', 'sample_file.txt')
    #     parsed = parse(message)
    #     print(parsed)


