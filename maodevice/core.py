# -*- coding: utf-8 -*-
class BaseCommunicator(object):
    """Communicate with a device.

    This is the base class of device communicators.

    Note:
        This class itself is not used, but it is inherited b
        child classes and used.

    Args:
        *args: Variable length argument list.

    Attributes:
        method (str): Communication method.
        connection (bool): Connection indicator.
            If it is true, the connection has been established.
        terminator (str): Termination character.
    """
    method = ""
    connection = False
    terminator = "\n"

    def __init__(self, *args):
        if len(args) != 0:
            self.open()

    def set_terminator(self, term_char):
        """Set the termination character.

        Args:
            term_char (str): Termination character.

        Return:
            None
        """
        self.terminator = term_char
        return

    def open(self):
        """Open the connection to the device.

        Note:
            This method is overridden in the child class.
        """
        pass

    def close(self):
        """Close the connection to the device.

        Note:
            This method is overridden in the child class.
        """
        pass

    def send(self, msg):
        """Send a message to the device.

        Note:
            This method is overridden in the child class.

        Args:
            msg (str): A message to send the device.
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

    def recv(self, byte):
        """Receive the response of the device.

        Note:
            This method is overridden in the child class.

        Args:
            byte (int): Bytes to read.
        """
        pass

    def readlines(self):
        """Receive the multiple rows response of the device.

        Note:
            This method is overridden in the child class.
        """
        pass


class BaseDeviceHandler(object):
    """Control a device.

    This is the base class of device handler.

    Note:
        This class itself is not used, but it is inherited by
        child classes and used.

    Args:
        com (maodevice.communicator):
            Communicator instance to control the device.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = ""
    product_name = ""
    classification = ""

    def __init__(self, com):
        self.com = com
        self.open()

    def open(self):
        """Open the connection to the device.

        Note:
            This method uses the one of "com".

        Return:
            None
        """
        self.com.open()
        return

    def close(self):
        """Close the connection to the device.

        Note:
            This method uses the one of "com".

        Return:
            None
        """
        self.com.close()
        return
