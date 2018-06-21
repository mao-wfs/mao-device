# coding: utf-8
from .. import device


class Md20M(device.Device):
    """Control 'MD-20-M'

    This class control the modulator driver 'MD-20-M'.
    This class is based on 'device.Device'.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = 'Optilab'
    product_name = 'MD-20-M'
    classification = 'Modulator Driver'

    def __init__(self, com):
        """Initialize 'Md20M'.

        Args:
            com (communicator.Communicator): Communicator to control 'MD-20-M'.
        """
        super().__init__(com)
        self.com.set_terminator('\r\n')

    def set_vadj(self, vadj):
        """Set the voltage which controls the duty cycle.

        Note:
            The setting range is 0.01 - 4.99.

        Args:
            vadj (float): The voltage which controls the duty cycle.

        Return:
            None
        """
        if not 0.01 <= vadj <= 4.49:
            raise ValueError('Set VADJ 0.01 - 4.99.')
        self.com.send(f'SETADJ:{vadj:.3}')
        self.com.recv()
        return

    def set_vbias(self, vbias):
        """Set the voltage of the output DC voltage.

        Note:
            The setting range is 0.01 ~ 9.99.

        Args:
            vbias (float): The voltage of the output DC voltage.

        Return:
            None
        """
        if not 0.01 <= vbias <= 9.99:
            raise ValueError('Set VBIAS 0.01 - 9.99.')
        self.com.send(f'SETBIAS:{vbias:.3}')
        self.com.recv()
        return

    def set_vgain(self, vgain):
        """Set the voltage which controls the RF gain.

        Note:
            The setting range is 1.00 - 8.50.

        Args:
            vgain (float): The voltage which controls the RF gain.

        Return:
            None
        """
        if not 1.00 <= vgain <= 8.50:
            raise ValueError('Set VGAIN 1.00 - 8.50.')
        self.com.send(f'SETGAIN:{vgain:.3}')
        self.com.recv()
        return

    def show_status(self):
        """Show the status of 'MD-20-M'.

        Return:
            ret (str): Status of 'MD-20-M'.
        """
        self.com.send('READ')
        ret = self.readlines()
        return ret
