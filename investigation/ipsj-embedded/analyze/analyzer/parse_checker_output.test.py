
import unittest

from .parse_checker_output import parse_checker_output


class MyTestCase(unittest.TestCase):
    def test_parse_output(self):
        checker_output = """

[category1] path/to/file1

[category2] path/to/file2



[category3] path/to/file3:1:3


        """
        print(checker_output)
        expected = [
            {'category': 'category1', 'path': 'path/to/file1'},
            {'category': 'category2', 'path': 'path/to/file2'},
            {'category': 'category3', 'path': 'path/to/file3:1:3'},
        ]
        actual = parse_checker_output(checker_output)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
