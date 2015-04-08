import unittest

import re
from mt940.fields import get_regex_from_spec, get_field_regex


class TestFields(unittest.TestCase):

    def test_2n(self):
        """Match up to 2 digits
        """
        self.assertEqual(
            get_regex_from_spec("2n"),
            r"(\d{0,2})"
        )

    def test_2n_with_slashes(self):
        """Match up to 2 digits
        """
        self.assertEqual(
            get_regex_from_spec("//2n//"),
            r"\/\/(\d{0,2})"
        )

    def test_3n(self):
        self.assertEqual(
            get_regex_from_spec("3n"),
            r"(\d{0,3})"
        )

    def test_3n_mandatory(self):
        self.assertEqual(
            get_regex_from_spec("3!n"),
            r"(\d{3,3})"
        )

    def test_3a_mandatory(self):
        self.assertEqual(
            get_regex_from_spec("3!a"),
            r"([A-Z]{3,3})"
        )

    def test_4c_mandatory(self):
        self.assertEqual(
            get_regex_from_spec("4!c"),
            '([A-Z\\d]{4,4})'
        )

    def test_5d(self):
        self.assertEqual(
            get_regex_from_spec("5d"),
            r"([\d,]{0,5})"
        )

    def test_6x(self):
        self.assertEqual(
            get_regex_from_spec("6x"),
            '([A-Z\\d\\s,]{0,6})'
        )

    def test_multiple_parts(self):
        self.assertEqual(
            get_regex_from_spec("4!c2n"),
            '([A-Z\\d]{4,4})(\\d{0,2})'
        )

    def test_get_field_regex(self):
        with self.assertRaises(KeyError):
            get_field_regex("xxxx")  # Field does not exist

    # def test_field61(self):
    #     data = "0501120112DN2,50NCHGNONREF//BR05012139000003\n824-OPŁ. ZA PRZEL. ELIXIR MT"
    #     regex = get_field_regex("61")
    #     print(regex)
    #     self.assertTrue(
    #         re.match(regex, data)
    #     )
