# coding: utf-8
from ..device import Device
from ... import utils


class Md20M(Device):
    """Control 'MD-20-M'

    This class is based on 'Device'.

    Args:
        com: Communicator instance to control the device

    Attributes:
        manufacturer (str): Manufacturer of the device
        product_name (str): Name of the device
        classification (str): Classification of the device
    """
    manufacturer = 'Optilab'
    product_name = 'MD-20-M'
    classification = 'Modulator Driver'

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator('\r\n')

    @utils.filter('vgain', 1.00, 8.50)
    def set_vgain(self, vgain):
        """Set the voltage which controls the RF gain

        Note:
            The setting range is 1.00 - 8.50.

        Args:
            vgain (float): The voltage which controls the RF gain

        Return:
            None
        """
        self.com.send(f'SETGAIN:{vgain:.3}')
        # self.com.recv()
        return

    @utils.filter('vadj', 0.01, 4.99)
    def set_vadj(self, vadj):
        """Set the voltage which controls the duty cycle

        Note:
            The setting range is 0.01 - 4.99.

        Args:
            vadj (float): The voltage which controls the duty cycle

        Return:
            None
        """
        self.com.send(f'SETADJ:{vadj:.3}')
        # self.com.recv()
        return

    @utils.filter('vbias', 0.01, 9.99)
    def set_vbias(self, vbias):
        """Set the voltage of the output DC voltage

        Note:
            The setting range is 0.01 - 9.99.

        Args:
            vbias (float): The voltage of the output DC voltage

        Return:
            None
        """
        self.com.send(f'SETBIAS:{vbias:.3}')
        # self.com.recv()
        return

    @utils.decoder
    def show_status(self):
        """Show the status of 'MD-20-M'

        Return:
            ret (bytes): Status of 'MD-20-M'
        """
        ret = self.com.query('READ')
        return ret
