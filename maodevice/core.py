# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class BaseCommunicator(metaclass=ABCMeta):
    """Communicate with a device.

    This is the base class of device communicators.

    Note:
        This class itself is not used, but it is inherited b
        child classes and used.

    Args:
        *args: Variable length argument list.

    Attributes:
        METHOD (str): Communication method.
        connection (bool): Connection indicator.
            If it is true, the connection has been established.
        terminator (str): Termination character.
    """
    METHOD = ""

    connection = False
    terminator = "\n"

    def __init__(self, *args):
        if not len(args) != 0:
            self.open()

    @abstractmethod
    def open(self):
        """Open the connection to the device.

        Note:
            This method must be overridden in the child class.
        """
        pass

    @abstractmethod
    def close(self):
        """Close the connection to the device.

        Note:
            This method must be overridden in the child class.
        """
        pass

    @abstractmethod
    def send(self, msg):
        """Send a message to the device.

        Note:
            This method must be overridden in the child class.

        Args:
            msg (str): A message to send the device.
        """
        pass

    @abstractmethod
    def recv(self, byte):
        """Receive the response of the device.

        Note:
            This method must be overridden in the child class.

        Args:
            byte (int): Bytes to read.
        """
        pass

    def query(self, msg, byte=4096):
        """Query a message to the device.

        Args:
            msg (str): A message to query the device.

        Return:
            ret (bytes): The response of the device.
        """
        self.send(msg)
        ret = self.recv(byte)
        return ret

    @classmethod
    def set_terminator(cls, term_char):
        """Set the termination character.

        Args:
            term_char (str): Termination character.

        Return:
            None
        """
        cls.terminator = term_char
        return


class BaseDeviceHandler(metaclass=ABCMeta):
    """Control a device.

    This is the base class of device handler.

    Note:
        This class itself is not used, but it is inherited by
        child classes and used.

    Args:
        com (maodevice.communicator):
            Communicator instance to control the device.

    Attributes:
        MANUFACTURER (str): Manufacturer of the device.
        PRODUCT_NAME (str): Name of the device.
        CLASSIFICATION (str): Classification of the device.
    """
    MANUFACTURER = ""
    PRODUCT_NAME = ""
    CLASSIFICATION = ""

    def __init__(self, com):
        self.com = com
        com.open()

    @abstractmethod
    def validate(self):
        """Validate a communication to the device.

        Note:
            This method must be overridden in the child class.
        """
        pass