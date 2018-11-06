# -*- coding: utf-8 -*-
from maodevice.core import BaseValidator
from maodevice.exceptions import (
    OctadSError,
    Model3390AWGError,
    Rfll20HError,
)


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
class Model3390AWGValidator(BaseValidator):
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
        valid_msg = f'+0,"No error"{self.com.terminator}'
        err = self.com.query("SYST:ERR?").decode()
        if err != valid_msg:
            raise Model3390AWGError(err)
        return


# RFLL-20-H (Optilab, LLC.)
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