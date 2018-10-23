# -*- coding: utf-8 -*-
__all__ = [
    "extract_bits",
    "or_of_bits",
]


def extract_bits(bit, bit_dict):
    """Extract bits which is turend on (1).

    Args:
        bit (int): Bit to check.
        bit_dict (dict): Correspondance dict of bit and status.

    Return:
        valid_bit (:obj:`list` of :obj:`str`): List of bit which is
            turned on (1).

    Example:
        >>> sample_dict = {
        ...     "S1": 0b001,
        ...     "S2": 0b010,
        ...     "S3": 0b100,
        ... }
        >>> extract_bits(0b101, sample_dict)
        ["S1", "S3"]
    """
    assert all(isinstance(val, int) for val in bit_dict.values()), \
        "bit_dict: all elements are expected to be 'int'"

    valid_bit = [
        key for key, val in bit_dict.items() if not int(bit) & val == 0
    ]
    return valid_bit


def or_of_bits(*bits):
    """OR the given bits.

    Args:
        *bits (int): Bits for OR. More than one argument required.

    Return:
        or_bit (int): OR of the given bits.

    Example:
        >>> or_of_bits(1, 4, 16)
        21 # 0b10101, 0x15
        >>> or_of_bits(0b00010, 0b10000)
        18 # 0b10010, 0x12
        >>> or_of_bits(0x01, 0x10)
        17 # 0b10001, 0x11
    """
    assert len(bits) > 1, "more than one argument required"
    assert all(isinstance(bit, int) for bit in bits), \
        "bits: all elements are expected to be 'int'"

    or_bit = 0
    for bit in bits:
        or_bit |= bit

    return or_bit
