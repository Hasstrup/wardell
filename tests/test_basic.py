import unittest
from basic.basic import Basic


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.target = Basic()

    def test_even_placed_chars(self):
        test_string = 'pynative'
        expected = ['p', 'n', 't', 'v']
        result = self.target.even_placed_chars(test_string)
        self.assertEqual(expected, result, f"should be {expected}, got: {result}")

    def test_slice_string_with_diff(self):
        test_string = 'pynative'
        expected = 'tive'
        result = self.target.slice_string_with_diff(test_string, 4)
        self.assertEqual(expected, result, f"should be {expected}, got: {result}")

    def test_bool_on_start_end_equality(self):
        list = [1, 2, 3, 4, 5, 6, 7]
        self.assertFalse(self.target.bool_on_start_end_equality(
            list), "Expected false, got true")
        list = [1, 4, 5, 6, 1]
        self.assertTrue(self.target.bool_on_start_end_equality(
            list), "Expected true got false")

    def test_is_divisible_by_five(self):
        target = [3, 4, 20, 15, 25]
        expected = [20, 15, 25]
        result = self.target.is_divisible_by_five(target)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_count_substring(self):
        str = "Emma is good developer. Emma is a writer"
        result = self.target.count_substring(str, "Emma")
        self.assertEqual(result, 2)

    def test_number_palindrome(self):
        self.assertTrue(self.target.number_palindrome(121))
        self.assertTrue(self.target.number_palindrome(232))
        self.assertFalse(self.target.number_palindrome(124))


if __name__ == '__main__':
    unittest.main()
