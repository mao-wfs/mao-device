# coding: utf-8
from .. import device


class Pd30M(device.Device):
    """Control 'PD-30-M'.

    This class control the O/E converter 'PD-30-M'.
    This class is based on 'device.Device'.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = 'Optilab'
    product_name = 'PD-30-M'
    classification = 'O/E Converter'

    def __init__(self, com):
        """Initialize 'Pd30M'.

        Args:
            com (communicator.Communicator): Communicator to control 'PD-30-M'.
        """
        super().__init__(com)
        self.com.set_terminator('\r\n')

    def show_status(self):
        """Show status of 'PD-30-M'.

        Return:
            ret (str): Status of 'PD-30-M'.
        """
        self.com.send('READP')
        ret = self.readlines()
        return ret
