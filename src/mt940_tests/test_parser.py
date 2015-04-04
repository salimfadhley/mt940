from mt940.parser import parse, tokenize
import unittest


class TestMT940Parser(unittest.TestCase):

    def test_basic(self):
        message = "{}"
        expected = {}
        self.assertEqual(expected, parse(message))

    def test_tokenize_28c(self):
        message = "{:28C:00065/001}"
        result = tokenize(message)
        print(result)

    # def test_single_key(self):
    #     message = ":28C:00065/001"
    #     expected = ('Statement Number/Sequence Number',(65,1))
    #     self.assertEqual(expected, parse(message))
    #
