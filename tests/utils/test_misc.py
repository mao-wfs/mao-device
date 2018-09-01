# -*- coding: utf-8 -*-
import unittest
from maodevice.utils import misc


class TestMisc(unittest.TestCase):
    """Test class of misc.py
    """
    def test_extract_bits(self):
        """Test method of extract_bits
        """
        foo = "foo"
        correct_dict = {
            'S1': 0b00001,
            'S2': 0b00010,
            'S3': 0b00100,
        }
        incorrect_dict = {
            'S1': 0b00001,
            'S2': foo,
            'S3': 0b00100,
        }

        # Test whether the expected value can be obtained
        self.assertEqual(
            ['S2'],
            misc.extract_bits(0b010, correct_dict),
        )
        self.assertEqual(
            ['S1', 'S3'],
            misc.extract_bits(0b101, correct_dict),
        )

        # Test exceptions
        with self.assertRaises(TypeError) as e:
            misc.extract_bits(foo, correct_dict)
        self.assertEqual(
            "unsupported operand type(s) for &: 'str' and 'int'",
            e.exception.args[0],
        )

        with self.assertRaises(AttributeError) as e:
            misc.extract_bits(0b001, foo)
        self.assertEqual(
            "'str' object has no attribute 'values'",
            e.exception.args[0],
        )

        with self.assertRaises(AssertionError) as e:
            misc.extract_bits(0b001, incorrect_dict)
        self.assertEqual(
            "bit_dict: all elements are expected to be 'int'",
            e.exception.args[0],
        )

    def test_or_of_bits(self):
        """Test method of of_of_bits
        """

        # Test whether the expected value can be obtained
        self.assertEqual(21, misc.or_of_bits(1, 4, 16))
        self.assertEqual(0b10010, misc.or_of_bits(0b00010, 0b10000))
        self.assertEqual(0x11, misc.or_of_bits(0x01, 0x10))
        # Test exceptions
        with self.assertRaises(AssertionError) as e:
            misc.or_of_bits(4)
        self.assertEqual(
            "more than one argument required",
            e.exception.args[0],
        )

        with self.assertRaises(AssertionError) as e:
            misc.or_of_bits(1, 4, 'foo', 16)
        self.assertEqual(
            "bits: all elements are expected to be 'int'",
            e.exception.args[0],
        )


if __name__ == "__main__":
    unittest.main()
