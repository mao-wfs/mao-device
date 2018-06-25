# coding: utf-8
import telnetlib
from .. import communicator


class Telnet(communicator.Communicator):
    """Provides telnet communication based on 'Communicator'

    Note:
        This class is an override of the base class 'Communicator'
        for telnet communication.

    Attributes:
        method (str): Communication method.
        connection (bool): If True, it is connected.
        terminator (str): Termination character.
    """
    method = 'Telnet'

    def __init__(self, host, port, timeout=1.):
        """Initialize 'Telnet'

        Args:
            host (str): IP Address of a device.
            port (int): Port of a device.
            timeout (float): Set a read timeout values.
                Defaults to 1.0.
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

    def query(self, msg):
        """Query a message to a device.

        Note:
            This method is an override of the 'query' method of the base class.

        Args:
            msg (str): Message to query a device.

        Return:
            ret (bytes): The answer to the query.
        """
        self.send(msg)
        ret = self.readlines()
        return ret

    # def recv(self, expected=1024)
    #     """Receive messages from a device.
    #
    #     Note:
    #         This method is an override of the 'recv' method of the base class.
    #
    #     Args:
    #         expected (int): Number of bytes to read.
    #
    #     Return:
    #         ret (int or str): A message to receive a device.
    #     """
    #     ret = self.tn.read_until(byte, self.timeout)
    #     return

    def readlines(self):
        """Read lines of a device output.

        Note:
            This method if an override of the 'readlines' method of the base class.

        Return:
            ret (:obj:`list` of :obj:`bytes`): A message list to receive a device.
        """
        ret = self.tn.read_until(
            expected=self.terminator.encode(),
            timeout=self.timeout,
        )
        ret = ret.splitlines()
        return ret
