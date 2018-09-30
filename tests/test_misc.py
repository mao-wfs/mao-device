# -*- coding: utf-8 -*-
import pytest
from maodevice.utils.misc import *


class TestExtractBits(object):
    """Test class of 'maodevice.utils.misc.extract_bits'
    """
    correct_dict = {"S1": 0b001, "S2": 0b010, "S3": 0b100}
    incorrect_dict = {"S1": 0b001, "S2": "foo", "S3": 0b100}

    @pytest.mark.parametrize(
        "bit, bit_dict, expected",
        [
            (0b010, correct_dict, ["S2"]),
            (0b101, correct_dict, ["S1", "S3"]),
        ])
    def test_success(self, bit, bit_dict, expected):
        """Test method for success
        """
        result = extract_bits(bit, bit_dict)
        assert result == expected

    @pytest.mark.parametrize(
        "bit, bit_dict, expected",
        [
            ("foo", correct_dict, pytest.raises(TypeError)),
            (0b001, "foo", pytest.raises(AttributeError)),
            (0b001, incorrect_dict, pytest.raises(AssertionError)),
        ]
    )
    def test_exception(self, bit, bit_dict, expected):
        """Test method for exceptions
        """
        with expected:
            extract_bits(bit, bit_dict)


class TestOrOfBits(object):
    """Test class of 'maodevice.utils.misc.or_of_bits'
    """
    @pytest.mark.parametrize(
        "bits, expected",
        [
            ((1, 4, 16), 21),
            ((0b00010, 0b10000), 0b10010),
            ((0x01, 0x10), 0x11),
        ])
    def test_success(self, bits, expected):
        """Test method for success
        """
        result = or_of_bits(*bits)
        assert result == expected

    @pytest.mark.parametrize(
        "bits, expected",
        [
            ((4,), pytest.raises(AssertionError)),
            ((1, 4, "foo", 16), pytest.raises(AssertionError)),
        ]
    )
    def test_exception(self, bits, expected):
        """Test method for exceptions
        """
        with expected:
            or_of_bits(*bits)


if __name__ == "__main__":
    pytest.main()
