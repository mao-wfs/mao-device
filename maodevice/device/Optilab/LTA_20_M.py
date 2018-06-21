# coding: utf-8
from .. import device


class Lta20M(device.Device):
    """Control 'LTA-20-M'.

    This class control the E/O converter 'LTA-20-M'.
    This class is based on 'device.Device'.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = 'Optilab'
    product_name = 'LTA-20-M'
    classification = 'E/O Converter'

    def __init__(self, com):
        """Initialize 'Lta20M'.

        Args:
            com (communicator.Communicator): Communicator to control 'LTA-20-M'.
        """
        super().__init__(com)
        self.com.set_terminator('\r\n')

    def show_status(self):
        """Show status of 'LTA-20-M'.

        Return:
            ret (str): Status of 'LTA-20-M'.
        """
        self.com.send('READ')
        ret = self.readlines()
        return ret
