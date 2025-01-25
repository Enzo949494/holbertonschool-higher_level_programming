#!/usr/bin/python3
"""Unittest module for max_integer function.

This module contains comprehensive unit tests for the max_integer function,
covering various input scenarios and edge cases.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer function."""

    def test_positive_numbers(self):
        """Test max_integer with a list of positive numbers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        """Test max_integer with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-10, 5, 0, -5]), 5)

    def test_single_element(self):
        """Test max_integer with a single element list."""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-42]), -42)

    def test_empty_list(self):
        """Test max_integer with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_repeated_max(self):
        """Test max_integer with repeated maximum values."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-1, -1, -1]), -1)

    def test_float_numbers(self):
        """Test max_integer with floating point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -0.5]), -0.5)

    def test_large_numbers(self):
        """Test max_integer with large numbers."""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([-1000000, -999999, -1000001]), -999999)

    def test_zero_handling(self):
        """Test max_integer with zero values."""
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, 0, 1]), 1)

if __name__ == '__main__':
    unittest.main()
