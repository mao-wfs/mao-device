# coding: utf-8
from ..device import Device
from ... import utils


class Lta20Q(Device):
    """Control 'LTA-20-Q'.

    This is a child class of the base class 'Device'.

    Args:
        com: Communicator instance to control the device.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = 'Optilab'
    product_name = 'LTA-20-Q'
    classification = 'E/O Converter'

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator('\r\n')

    @utils.decoder
    def show_status(self):
        """Show status of 'LTA-20-M'.

        Return:
            ret (str): Status of 'LTA-20-Q'.
        """
        ret = self.com.query('READ')
        return ret
