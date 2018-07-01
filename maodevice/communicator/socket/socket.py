# coding: utf-8
import socket
from ..communicator import Communicator


class Socket(Communicator):
    """Communicate with the device via 'Socket'

    This is a child class of the base class 'Communicator'.

    Args:
        host (str): IP Address of a device
        port (int): Port of a device
        timeout (float): A read timeout values
            Defaults to 1.0.
        family (socket.AddressFamily): A constant indicating
            the address (and protocol) family
            Defaults to socket.AF_INET.
        type (socket.SocketKind): A Constant indicating the socket type
            Defaults to socket.SOCK_STREAM.
        proto (int): Protocol number
            If family=socket.AF_CAN, either socket.CAN_RAW or
            socket.CAN_BCM should be specified.
            Defaults to 0.
        fileno (None or int): File descriptor
            If it is specified, the other arguments are ignored, causing
            the socket with the specified file descriptor to return.
            Unlike socket.fromfd(), fileno will return the same socket and
            not a duplicate. This may help close a detached socket using
            socket.close().
            Defaults to None.

    Attributes:
        method (str): Communication method
        connection (bool): Connection indicator
            If it is true, the connection has been established.
        terminator (str): Termination character
    """
    method = 'Socket'

    def __init__(
            self,
            host,
            port,
            timeout=1.,
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=0,
            fileno=None,
    ):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.family = family
        self.type = type
        self.proto = proto
        self.fileno = fileno

    def open(self):
        """Open the connection to the device

        Note:
            This method override the 'open' in the base class.

        Return:
            None
        """
        if not self.connection:
            self.sock = socket.socket(
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
        """Close the connection to the device

        Note:
            This method override the 'close' in the base class.

        Return:
            None
        """
        self.sock.close()
        del(self.sock)
        self.connection = False
        return

    def send(self, msg):
        """Send a message to the device

        Note:
            This method override the 'send' in the base class.

        Args:
            msg (str): A Message to send the device

        Return:
            None
        """
        self.sock.send((msg + self.terminator).encode())
        return


    def recv(self, byte=1024):
        """Receive the response of the device

        Note:
            This method override the 'recv' in the base class.

        Args:
            byte (int): Bytes to read. Defaults to 1024

        Return:
            ret (bytes): The response of the device
        """
        ret = self.sock.recv(bufsize=byte)
        return ret

    def readlines(self):
        """Receive the multiple rows response of the device

        Note:
            This method override the 'readlines' in the base class.

        Return:
            ret (:obj:`list` of :obj:`bytes`): The response of the device
        """
        ret = self.sockfp.readlines()
        return ret
