# -*- coding: utf-8 -*-
from maodevice.core import BaseDeviceHandler
from maodevice.utils.decorators import decoder, limitter


class Md20M(BaseDeviceHandler):
    """Control 'MD-20-M'.

    The Optilab MD-20-M Modulator Driver (MD) is a 20 GHz bandwidth
    RF amplifier in a compact and user-friendly module that provides
    a high-quality, single-ended voltage to drive an optical modulator.

    Note:
        This class is based on 'maodevice.core.BaseDeviceHandler'

    Args:
        com (maodevice.communicator):
            Communicator instance to control the device.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = "Optilab"
    product_name = "MD-20-M"
    classification = "Modulator Driver"

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator("\r\n")

    @limitter("vadj", 0.01, 4.99, 0.01)
    def set_vadj(self, vadj):
        """Set the voltage which controls the duty cycle.

        Note:
            The setting range is 0.01 - 4.99.

        Args:
            vadj (float): The voltage which controls the duty cycle.

        Return:
            None
        """
        self.send(f"SETADJ:{vadj}")
        return

    @limitter("vbias", 0.01, 9.99, 0.01)
    def set_vbias(self, vbias):
        """Set the voltage of the output DC voltage.

        Note:
            The setting range is 0.01 - 9.99.

        Args:
            vbias (float): The voltage of the output DC voltage.

        Return:
            None
        """
        self.send(f"SETBIAS:{vbias}")
        return

    @limitter("vgain", 1.00, 8.50, 0.01)
    def set_vgain(self, vgain):
        """Set the voltage which controls the RF gain.

        Note:
            The setting range is 1.00 - 8.50.

        Args:
            vgain (float): The voltage which controls the RF gain.

        Return:
            None
        """
        self.send(f"SETGAIN:{vgain}")
        return

    @decoder
    def show_status(self):
        """Show the status fo 'MD-20-M'.

        Return:
            ret (bytes): Status of 'MD-20-M'
        """
        ret = self.query(msg="READ", byte=1024)
        return ret
