# -*- coding: utf-8 -*-
from maodevice.core import BaseDeviceHandler
from maodevice.utils import decoder


class Lta20Q(BaseDeviceHandler):
    """Control 'LTA-20-Q'.

    The LTA-20-Q modular transmitters are a wideband RF-over-fiber
    transmitter modules designed for antenna remoting and broadband
    RF transmission applications using single mode optical fiber.

    Note:
        This class is based on 'maodevice.core.BaseDeviceHandler'.

    Args:
        com (maodevice.communicator)
            Communicator instance to control the device.

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

    @decoder
    def show_status(self):
        """Show status of 'LTA-20-M'.

        Return:
            ret (bytes): Status of 'LTA-20-Q'.
        """
        ret = self.com.query("READ", byte=1024)
        return ret
