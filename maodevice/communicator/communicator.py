# coding: utf-8
class Communicator(object):
    """Communicate with a device

    This is the base class of device communicators.

    Note:
        This class itself is not used, but it is inherited by
        child classes and used.

    Args:
        *args: Variable length argument list

    Attributes:
        method (str): Communication method
        connection (bool): Connection indicator
            If it is true, the connection has been established.
        terminator (str): Termination character
    """
    method = 'communicator_base_class'
    connection = False
    terminator = '\n'

    def __init__(self, *args):
        if len(args) is not 0:
            self.open(*args)
            
    def set_terminator(self, term_char):
        """Set the termination character
        
        Args:
            term_char (str): Termination character

        Return:
            None
        """
        self.terminator = term_char
        return

    def open(self):
        """Open the connection to the device

        Note:
            This method is overridden in the child class.
        """
        pass

    def close(self):
        """Close the connection to the device

        Note:
            This method is overridden in the child class.
        """
        pass

    def send(self, msg):
        """Send a message to the device
        
        Note:
            This method is overridden in the child class.

        Args:
            msg (str): A Message to send the device
        """
        pass

    def query(self, msg):
        """Query a message to the device

        Args:
            msg (str): A message to query the device

        Return:
            ret (:obj:`list` of :obj:`bytes`): The response of the device
        """
        self.send(msg)
        ret = self.readlines()
        return ret

    def recv(self, byte):
        """Receive the response of the device

        Note:
            This method is overridden in the child class.

        Args:
            byte (int): Bytes to read
        """
        pass

    def readlines(self):
        """Receive the multiple rows response of the device

        Note:
            This method is overridden in the child class.
        """
        pass
