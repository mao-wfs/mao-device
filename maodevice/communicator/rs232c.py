# coding: utf-8
import serial
from . import communicator


class Rs232C(communicator.Communicator):
    """Provide serial communication based on 'Communicator'

    Note:
        This class is an override of the base class 'Communicator' for serial
        communication.

    Attributes:
        method (str): Communication method.
        connection (bool): If True, it is connected.
        terminator (str): Termination character. (Default: '\n')
    """
    method = 'RS-232C'

    def __init__(
        self,
        port,
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1.,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False,
        write_timeout=None,
        inter_byte_timeout=None,
        exclusive=None,
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
            exclusive (bool): Set exclusive access mode (POSIX only).
                A port cannot be opened in exclusive access mode
                if it is already open in exclusive access mode.
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
        self.exclusive = exclusive

    def open(self):
        """Connect to a device via serial communication.

        Note:
            This method is an override of the 'open' method of the base class.

        Return:
            None
        """
        if not self.connection:
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                parity=self.parity,
                stopbits=self.stopbits,
                timeout=self.timeout,
                xonxoff=self.xonxoff,
                rtscts=self.rtscts,
                dsrdtr=self.dsrdtr,
                write_timeout=self.write_timeout,
                inter_byte_timeout=self.inter_byte_timeout,
                exclusive=self.exclusive,
            )
            self.connection = True
        else:
            print('The Communication is already established.')
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

    def recv(self, size=1024):
        """Receive messages from a device.

        Note:
            This method is an override of the 'recv' method of the base class.

        Args:
            size (int): Number of bytes to read.

        Return:
            ret (): A message to receive a device.
        """
        ret = self.ser.read(size)
        return ret

    def readlines(self):
        """Read lines of a device output.

        Note:
            This method if an override of the 'readlines' method of the base
            class.

        Return:
            ret (str): Messages to receive a device.
        """
        if self.timeout is None:
            raise ValueError('You must set "timeout".')
        ret = ','.join(self.ser.readlines())
        return ret
