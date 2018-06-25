# coding: utf-8
import socket
from .. import communicator


class Socket(communicator.Communicator):
    """Provides socket communication based on 'Communicator'.

    Note:
        This class is an override of the base class 'Communicator'
        for socket communication.

    Attributes:
        method (str): Communication method.
        connection (bool): If True, it is connected.
        terminator (str): Termination character.
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
        """Initialize 'Socket'.
        
        Args:
            host (str): IP Address of a device.
            port (int): Port of a device.
            timeout (float): A read timeout values.
                Defaults to 1.0.
            family (socket.AddressFamily): A constant indicating the address
                (and protocol) family.
                Defaults to socket.AF_INET.
            type (socket.SocketKind): A Constant indicating the socket type.
                Defaults to socket.SOCK_STREAM.
            proto (int): Protocol number.
                If family=socket.AF_CAN, either socket.CAN_RAW or
                socket.CAN_BCM should be specified.
                Defaults to 0.
            fileno (None or int): File descriptor.
                If it is specified, the other arguments are ignored, causing
                the socket with the specified file descriptor to return.
                Unlike socket.fromfd(), fileno will return the same socket and
                not a duplicate. This may help close a detached socket using
                socket.close().
                Defaults to None.
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
        """Close the connection.

        Note:
            This method is an override of the 'close' method of the base class.

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
            msg (str): A Message to send a device.

        Return:
            None
        """
        self.sock.send((msg + self.terminator).encode())
        return


    def recv(self, byte=1024):
        """Receive messages from a device.

        Note:
            This method is an override of the 'recv' method of the base class.

        Args:
            byte (int): Bytes to read. Defaults to 1024.

        Return:
            ret (bytes): Byte string received from a device.
        """
        ret = self.sock.recv(bufsize=byte)
        return ret

    def readlines(self):
        """Read lines of a device output.

        Note:
            This method if an override of the 'readlines' method of the base class.

        Return:
            ret (:obj:`list` of :obj:`bytes`): A message list to receive a device.
        """
        ret = self.sockfp.readlines()
        return ret
