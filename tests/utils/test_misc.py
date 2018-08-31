# -*- coding: utf-8 -*-
import unittest
from maodevice.utils import misc


class TestMisc(unittest.TestCase):
    """Test class of misc.py
    """
    def test_extract_bits(self):
        sample_dicts = {
            'S1': 0b00001,
            'S2': 0b00010,
            'S3': 0b00100,
            'S4': 0b01000,
            'S5': 0b10000,
        }

        values_dict = {
            'value1': 0b01001,
            'value2': 
            'value3': 'Hello world!',
        }
