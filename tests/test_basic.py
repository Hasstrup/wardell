import unittest
from basic.basic import Basic

print(__name__)


class TestBasic(unittest.TestCase):
    def test_even_placed_chars(self):
        test_string = 'pynative'
        expected = ['p', 'n', 't', 'v']
        result = Basic().even_placed_chars(test_string)
        self.assertEqual(expected, result, f"should be {expected}, got: {result}")


if __name__ == '__main__':
    unittest.main()
