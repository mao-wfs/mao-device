# coding: utf-8
import socket
from ... import communicator


class Socket(communicator.Communicator):
    """Provides socket communication based on 'Comunicator'.

    Note:
        This class is an override of the base class 'Communicator' for socket
        communication.

    Attributes:
        method (str): Communication method, 'Socket'.
        connection (bool): If True, it is connected.
        terminator (str): Termination character. (Default: '\n')
    """
    method = 'Socket'

    def __init__(
        self,
        host,
        port,
        timeout=3.,
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=0,
        fileno=None,
    ):
        """Initialize 'Socket'.
        
        Args:
            host (str): IP Address of a device.
            port (int): Port of a device.
            timeout (float): Set a read timeout values. (Default: 3.)
            family (): A constant indicating the address (and protocol) family.
                (Default: socket.AF_INET)
            type (): A Constant indicating the socket type.
                (Default: socket.SOCK_STREAM)
            proto (): Protocol number. (Default: 0)
                      If family=socket.AF_CAN, either socket.CAN_RAW or
                      socket.CAN_BCM should be specified.
                      fileno (): (Default: None)
                If fileno=True, another argument is ignored, so the socket of
                the specified file descriptor is returned.
                Unlike socket.fromfd(), fileno returns the same socket,
                not socket replicas. This may be useful to close a
                detached socket with socket.close().
        """
        self.host = host
        self.port = port
        self.timeout = timeout
        self.family = family
        self.type = type
        self.proto = proto
        self.fileno = fileno

    def open(self):
        """Connect to a device via socket communication.

        Note:
            This method is an override of the 'open' method of the base class.

        Return:
            None
        """
        if not self.connection:
            self.sock = socket.Socket(
                self.family,
                self.type,
                self.proto,
                self.fileno,
            )
            self.sock.settimeout(self.timeout)
            self.sock.connect((self.host, self.port))
            self.sockfp = self.sock.makefile()
            self.connection = True
        return

    def close(self):
        """Close the connection.

        Note:
            This method is an override of the 'close' method of the base
            class.

        Return:
            None
        """
        self.sock.close()
        del(self.sock)
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
        self.sock.send(msg + self.terminator)
        return

    def recv(self, byte=1024):
        """Receive messages from a device.

        Note:
            This method is an override of the 'recv' method of the base class.

        Args:
            byte (int): Number of bytes to read.

        Return:
            ret (): A message to receive a device.
        """
        ret = self.sock.recv(byte)
        return

    def readline(self):
        """Read a line of a device output.

        Note:
            This method is an override of the 'readline' method of the base
            class.

        Return:
            ret (): A message to receive a device.
        """
        ret = self.sockfp.readline()
        return ret
