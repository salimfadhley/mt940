import pprint
import unittest

import pkg_resources
from mt940.parser import parse


class TestActualData(unittest.TestCase):
    def test_complex_message(self):
        message = pkg_resources.resource_string("mt940_tests", "sample_file.txt").decode("utf-8")

        pprint.pprint(message)
        result = parse(message)
        pprint.pprint(result)


if __name__ == '__main__':
    unittest.main()