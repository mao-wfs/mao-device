# coding: utf-8
import serial
from . import communicator


class Rs232C(communicator.Communicator):
    """Provide serial communication based on 'Communicator'

    Note:
        This class is an override of the base class 'Communicator' for serial
        communication.

    Attributes:
        method (str): Communication method, 'Rs232C'.
        connection (bool): If True, it is connected.
        terminator (str): Termination character. (Default: '\n')
    """
    method = 'RS-232C'

    def __init__(
        self,
        port,
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1.,
        timeout=1.,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False,
        write_timeout=1.,
        inter_byte_timeout=None,
    ):
        """Initialize 'Rs232C'.
        
        Args:
            port (str): Device name or None
            baudrate (int): Baud rate. (Default: 9600)
            byteize (int): Number of data bits. (Default: 8)
                (Allowed values: 5, 6, 7, 8.)
            parity (str): Enable parity checking. (Default: 'N')
                (Allowed values: 'N', 'E', 'O', 'M', 'S')
            stopbits (float): Number of stop bits. (Default: 1.)
                (Allowed values: 1., 1.5, 2.)
            timeout (float): Set a read timeout values. (Default: 1.)
            xonxoff (bool): Enable software flow control. (Default: False)
            rtscts (bool): Enable hardware (RTS/CTS) flow control. (Default: False)
            dsrdtr (bool): Enable hardware (DSR/DTR) flow control. (Default: False)
            write_timeout (float): Set a write timeout value. (Default: 1.)
            inter_byte_timeout (float or None): (Default: None)
                Inter-character timeout, None to disable.
        """
        self.port = port
        self.baudrate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        self.xonxoff = xonxoff
        self.rtscts = rtscts
        self.dsrdtr = dsrdtr
        self.write_timeout = write_timeout
        self.inter_byte_timeout = inter_byte_timeout

    def open(self):
        """Connect to a device via serial communication.

        Note:
            This method is an override of the 'open' method of the base class.

        Return:
            None
        """
        if not self.connection:
            self.ser = serial.Serial(
                self.port,
                self.timeout,
                self.parity,
                self,stopbits,
                self.timeout,
                self.xonxoff,
                self.rtscts,
                self.dsrdtr,
                self.write_timeout,
                self.inter_byte_timeout,
            )
            self.connection = True
        return

    def close(self):
        """Close the connection.

        Note:
            This method is an override of the 'close' method of the base class.

        Return:
            None
        """
        self.ser.close()
        del(self.ser)
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
        self.ser.write((msg + self.terminator).encode())
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
        ret = self.ser.readinto(byte)
        return ret

    def readline(self):
        """Read a line of a device output.

        Note:
            This method is an override of the 'readline' method of the base
            class.

        Return:
            ret (): A message to receive a device.
        """
        self.ser.readline()
        return ret
