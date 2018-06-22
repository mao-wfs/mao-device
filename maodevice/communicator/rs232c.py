# coding: utf-8
import serial
from . import communicator


class Rs232C(communicator.Communicator):
    """Provides serial communication based on 'Communicator'

    Note:
        This class is an override of the base class 'Communicator'
        for serial communication.

    Attributes:
        method (str): Communication method.
        connection (bool): If True, it is connected.
        terminator (str): Termination character.
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
            port (str): Device name.
            baudrate (int): Baud rate.
                Defaults to 9600.
            byteize (int): Number of data bits.
                Defaults to serial.EIGHTBITS.
            parity (str): Enable parity checking.
                Defaults to serial.PARITY_NONE.
            stopbits (float): Number of stop bits.
                Defaults to serial.STOPBITS_ONE.
            timeout (float): A read timeout values.
                Defaults to 1.0.
            xonxoff (bool): Enable software flow control.
                Defaults to False.
            rtscts (bool): Enable hardware (RTS/CTS) flow control.
                Defaults to False.
            dsrdtr (bool): Enable hardware (DSR/DTR) flow control.
                Defaults to False.
            write_timeout (float): Set a write timeout value.
                Defaults to None.
            inter_byte_timeout (float or None): Inter-character timeout.
                Defaults to None (None to disable).
            exclusive (bool): Set exclusive access mode (POSIX only).
                A port cannot be opened in exclusive access mode
                if it is already open in exclusive access mode.
                Defaults to None.
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
            byte (int): Bytes to read. Defaults to 1024.

        Return:
            ret (bytes): A message to receive a device.
        """
        ret = self.ser.read(size=byte)
        return ret

    def readline(self):
        """Read a line of a device output.

        Note:
            This method if an override of the 'readlines' method of the base class.

        Return:
            ret (bytes): A Message line to receive a device.
        """
        ret = self.ser.readline()
        return ret
