# coding: utf-8
import telnetlib
from . import communicator


class Telnet(communicator.Communicator):
    """Provides telnet communication based on 'Communicator'

    Note:
        This class is an override of the base class 'Communicator'
        for telnet communication.

    Attributes:
        method (str): Communication method.
        connection (bool): If True, it is connected.
        terminator (str): Termination character. (Default: '\n')
    """
    method = 'Telnet'

    def __init__(self, host, port, timeout=3.):
        """Initialize 'Telnet'

        Args:
            host (str): IP Address of a device.
            port (int): Port of a device.
            timeout (float): Set a read timeout values. Default: 3.)
        """
        self.host = host
        self.port = port
        self.timeout = timeout

    def open(self):
        """Connect to a device via telnet communication.

        Note:
            This method is an override of the 'open' method of the base class.

        Return:
            None
        """
        if self.connection == False:
            self.tn = telnetlib.Telnet(self.host, self.port, self.timeout)
            self.tn.open(self.host, self.port, self.timeout)
            self.connection = True
        return

    def close(self):
        """Close the connection.

        Note:
            This method is an override of the 'close' method of the base class.

        Return:
            None
        """
        self.tn.close()
        del(self.tn)
        self.connection = False
        return
    
    def send(self, msg):
        """Send a message to a device.

        Note:
            This method is an override of the 'send' method of the base class.

        Args:
            msg (str): Message to send a device.

        Return:
            None
        """
        self.tn.write((msg + self.terminator).encode())
        return

    def recv(self, byte=1024):
        """Receive messages from a device.

        Note:
            This method is an override of the 'recv' method of the base class.

        Args:
            byte (int): Number of bytes to read.

        Return:
            ret (int or str): A message to receive a device.
        """
        ret = self.tn.read_until(byte, self.timeout)
        return

    def readline(self):
        """Read a line of a device output.

        Note:
            This method is an override of the 'readline' method of the base
            class.

        Return:
            ret (str): A message to receive a device.
        """
        ret = self.tn.expect(f'{self.terminator}$', self.timeout).decode()
        return ret
