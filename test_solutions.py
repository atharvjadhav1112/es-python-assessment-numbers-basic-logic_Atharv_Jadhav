"""
Simple unit tests for solutions.py using Python's built-in unittest module.
Run with: python -m unittest test_solutions.py
"""

import unittest
from solutions import even_or_odd, add_all


class TestEvenOrOdd(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(even_or_odd(4), "Even")

    def test_odd_number(self):
        self.assertEqual(even_or_odd(7), "Odd")

    def test_zero(self):
        self.assertEqual(even_or_odd(0), "Even")

    def test_negative_even(self):
        self.assertEqual(even_or_odd(-4), "Even")

    def test_negative_odd(self):
        self.assertEqual(even_or_odd(-7), "Odd")

    def test_whole_number_float(self):
        self.assertEqual(even_or_odd(2.0), "Even")

    def test_invalid_string_input(self):
        with self.assertRaises(TypeError):
            even_or_odd("five")

    def test_invalid_none_input(self):
        with self.assertRaises(TypeError):
            even_or_odd(None)

    def test_invalid_non_integer_float(self):
        with self.assertRaises(ValueError):
            even_or_odd(3.5)


class TestAddAll(unittest.TestCase):

    def test_sample_list(self):
        self.assertEqual(add_all([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(add_all([]), 0)

    def test_mixed_int_float(self):
        self.assertEqual(add_all([10, -5, 2.5]), 7.5)

    def test_single_element(self):
        self.assertEqual(add_all([100]), 100)

    def test_invalid_non_list_input(self):
        with self.assertRaises(TypeError):
            add_all("not a list")

    def test_invalid_element_in_list(self):
        with self.assertRaises(TypeError):
            add_all([1, 2, "three", 4])


if __name__ == "__main__":
    unittest.main()
