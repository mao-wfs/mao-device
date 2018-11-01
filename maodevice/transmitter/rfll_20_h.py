# -*- coding: utf-8 -*-
__all__ = [
    "Md20M",
    "Lta20Q",
    "Pd30M",
]


from maodevice.core import BaseDeviceHandler
from maodevice.validators import Rfll20HValidator


class Md20M(BaseDeviceHandler, metaclass=Rfll20HValidator):
    """Control "MD-20-M".

    The Optilab MD-20-M Modulator Driver (MD) is a 20 GHz bandwidth
    RF amplifier in a compact and user-friendly module that provides
    a high-quality, single-ended voltage to drive an optical modulator.

    Note:
        This class is based on "maodevice.core.BaseDeviceHandler"

    Args:
        com (maodevice.communicator):
            Communicator instance to control the device.

    Attributes:
        MANUFACTURER (str): Manufacturer of the device.
        PRODUCT_NAME (str): Name of the device.
        CLASSIFICATION (str): Classification of the device.
    """
    MANUFACTURER = "Optilab"
    PRODUCT_NAME = "MD-20-M"
    CLASSIFICATION = "Modulator Driver"

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator("\r\n")

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

    def show_status(self):
        """Show the status fo "MD-20-M".

        Return:
            ret (bytes): Status of "MD-20-M"
        """
        ret = self.query(msg="READ", byte=1024)
        return ret


class Lta20Q(BaseDeviceHandler, metaclass=Rfll20HValidator):
    """Control "LTA-20-Q".

    The LTA-20-Q modular transmitters are a wideband RF-over-fiber
    transmitter modules designed for antenna remoting and broadband
    RF transmission applications using single mode optical fiber.

    Note:
        This class is based on "maodevice.core.BaseDeviceHandler".

    Args:
        com (maodevice.communicator)
            Communicator instance to control the device.

    Attributes:
        MANUFACTURER (str): Manufacturer of the device.
        PRODUCT_NAME (str): Name of the device.
        CLASSIFICATION (str): Classification of the device.
    """
    MANUFACTURER = "Optilab"
    PRODUCT_NAME = "LTA-20-Q"
    CLASSIFICATION = "E/O Converter"

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator("\r\n")

    def show_status(self):
        """Show status of "LTA-20-M".

        Return:
            ret (bytes): Status of "LTA-20-Q".
        """
        ret = self.com.query("READ", byte=1024)
        return ret


class Pd30M(BaseDeviceHandler, metaclass=Rfll20HValidator):
    """Control "PD-30-M".

    The PD-30-M is a 30 GHz bandwidth PIN receiver photodiode module
    designed for RF over fiber, antenna remoting, and broadband RF
    transmission applications using single mode optical.

    Note:
        This class is based on "maodevice.core.BaseDeviceHandler".

    Args:
        com: (maodevice.communicator)
            Communicator instance to control the device.

    Attributes:
        MANUFACTURER (str): Manufacturer of the device.
        PRODUCT_NAME (str): Name of the device.
        CLASSIFICATION (str): Classification of the device.
    """
    MANUFACTURER = "Optilab"
    PRODUCT_NAME = "PD-30-M"
    CLASSIFICATION = "O/E converter"

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator("\r\n")

    def show_status(self):
        """Show status of "PD-30-M".

        Return:
            ret (bytes): Status of "PD-30-M"
        """
        ret = self.com.query("READP")
        return ret
