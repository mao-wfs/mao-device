# -*- coding: utf-8 -*-
from maodevice.core import BaseValidator


# Keithley3390
class Keithley3390Validator(BaseValidator):
    """Validate a communication with "Model 3390 Arbitrary Waveform Generator"

    This class is based on "maodevice.core.BaseValidator".

    Note:
        This class is used as a metaclass.
    """
    def _validate(self):
        """Validate 

        Note:
            This method override the "close" in the base class.
        """
        if not hasattr(self, "com"):
            raise AttributeError("this class has no attribute 'com'")

        ret = self.com.query("SYST:ERR?")
        # NOTE: TBD
        if not ret == b'+0,"No error"\n':
            raise AssertionError(ret.decode())

        return