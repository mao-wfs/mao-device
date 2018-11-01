# -*- coding: utf-8 -*-
from maodevice.core import BaseValidator


# OCTAD-S (Elecs, Inc.)
class OctadSValidator(BaseValidator):
    """Validate a communication with "OCTAD-S".

    This class is based on "maodevice.core.BaseValidator".

    Note:
        This class is used as a metaclass.
    """
    def _validate(self):
        """Actual validator function of this validator.

        Note:
            This method override the "_validator" in the base class.
        """
        # NOTE: TBD
        pass


# Model 3390 Arbitrary Waveform Generator (Keithley Instruments, Inc.)
class Keithley3390Validator(BaseValidator):
    """Validate a communication with "Model 3390 Arbitrary Waveform Generator".

    This class is based on "maodevice.core.BaseValidator".

    Note:
        This class is used as a metaclass.
    """
    def _validate(self):
        """Actual validator function of this validator.

        Note:
            This method override the "_validator" in the base class.
        """
        ret = self.com.query("SYST:ERR?")
        # NOTE: TBD
        if not ret == b'+0,"No error"\n':
            raise AssertionError(ret.decode())

        return


# RFLL-20-H (Optilab)
class Rfll20HValidator(BaseValidator):
    """Validate a communication with a components of "RFLL-20-H".

    This class is based on "maodevice.core.BaseValidator".

    Note:
        This class is used as a metaclass
    """
    def _validate(self):
        """Actual validator function of this validator.

        Note:
            This method override the "_validator" in the base class.
        """
        # NOTE: TBD
        pass