# coding: utf-8
from .. import device


class Lta20M(device.Device):
    """Control 'LTA-20-M'.

    This class control the E/O converter 'LTA-20-M'.
    This class is based on 'device.Device'.

    Attributes:
        manufacturer (str): Manufacturer of the device, 'Optilab'.
        product_name (str): Name of the device, 'LTA-20-M'.
        classification (str): Classification of the device, 'E/O converter'.
    """
    manufacturer = 'Optilab'
    product = 'LTA-20-M'
    classification = 'E/O Converter'

    def __init__(self, com):
        """Initialize 'Lta20M'.

        Args:
            com (Communicator): Communicator to control 'LTA-20-M'.
        """
        super().__init__(com)
        self.com.set_terminator('\r\n')

    def show_status(self):
        """Show status of 'LTA-20-M'.

        Return:
            ret (str): Status of 'LTA-20-M'.
        """
        self.com.send('READ')
        ret = self.com.recv()
        return ret
