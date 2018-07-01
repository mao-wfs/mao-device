# -*- coding: utf-8 -*-
from ..device import Device
from ... import utils


class Pd30M(Device):
    """Control 'PD-30-M'.

    This is a child class of the base class 'Device'.

    Args:
        com: Communicator instance to control the device.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = 'Optilab'
    product_name = 'PD-30-M'
    classification = 'O/E Converter'

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator('\r\n')

    @utils.decoder
    def show_status(self):
        """Show status of 'PD-30-M'.

        Return:
            ret (bytes): Status of 'PD-30-M'.
        """
        ret = self.com.query('READP')
        return ret
