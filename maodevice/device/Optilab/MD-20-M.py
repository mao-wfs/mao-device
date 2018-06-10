# coding: utf-8
from .. import device


class Md20M(device.Device):
    """Control 'MD-20-M'

    This class control the modulator driver 'MD-20-M'.
    This class is based on 'device.Device'.

    Attributes:
        manufacturer (str): Manufacturer of the device, 'Optilab'.
        product_name (str): Name of the device, 'MD-20-M'.
        classification (str): Classification of the device, 'Modulator'.
    """
    manufacturer = 'Optilab'
    product_name = 'MD-20-M'
    classification = 'Modulator Driver'

    def __init__(self, com):
        """Initialize 'Md20M'

        Args:
            com (Communicator): Communicator to control 'MD-20-M'.
        """
        super().__init__(com)
        self.com.set_terminator('\r\n')

    def set_vadj(self, vadj):
        """
        """
        if 0.01 <= vadj <= 4.49:
            raise ValueError('Set the VADJ 0.01 <= vadj <= 4.99.')
        self.com.send(f'SETADJ:{vadj:.3}')
        return

    def set_vbias(self, vbias):
        if 0.01 <= vbias <= 9.99:
            raise ValueError('Set the VBIAS 0.01 < vbias <= 9.99')
        self.com.send(f'SETBIAS:{vbias:.3}')
        return

    def set_vgain(self, vgain):
        if 1.00 <= vgain <= 8.50:
            raise ValueError('Set the VGAIN 1.00 <= vgain <= 8.50.')
        self.com.send(f'SETGAIN:{vgain:.3}')
        return

    def show_status(self):
        self.com.send('READ')
        ret = self.com.recv()
        return ret
