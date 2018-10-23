# -*- coding: utf-8 -*-
from maodevice.core import BaseDeviceHandler
from maodevice.utils.decorators import decoder


class Pd30M(BaseDeviceHandler):
    """Control "PD-30-M".

    The PD-30-M is a 30 GHz bandwidth PIN receiver photodiode module
    designed for RF over fiber, antenna remoting, and broadband RF
    transmission applications using single mode optical.

    Note:
        This class is based on "maodevice.core.BaseDeviceHandler".

    Args:
        com: (maodevice.communicator)
            Communicator instance to control the device.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = "Optilab"
    product_name = "PD-30-M"
    classification = "O/E converter"

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator("\r\n")

    @decoder
    def show_status(self):
        """Show status of "PD-30-M".

        Return:
            ret (bytes): Status of "PD-30-M"
        """
        ret = self.com.query("READP")
        return ret
