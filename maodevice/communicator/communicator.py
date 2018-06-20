# coding: utf-8
class Communicator(object):
    """The base class of communicator.

    This is the base class of communicator.
    Various communicator are created by overriding this class.

    Note:
        You do not use this class itself. You override this class
        and create a class for each communication format.

    Attributes:
        method (str): Communication method. (Default: 'communicator_base_class')
        connection (bool): If True, it is connected.
        terminator (str): Termination character. (Default: '\n')
    """
    method = 'communicator_base_class'
    connection = False
    terminator = '\n'

    def __init__(self, *args):
        """Initialize and establish communication.
        
        Args:
            *args: Variable length argument list.
        """
        if len(args) != 0:
            self.open(*args)
            
    def set_terminator(self, term_char):
        """Set the termination character.
        
        Args:
            term_char (str): Termination Character (Default: '\n')

        Return:
            None
        """
        self.terminator = term_char
        return

    def open(self, *args):
        """Connect to a device.

        Note:
            This method is what is override to the 'open' method of child
            class.
        """
        pass

    def close(self):
        """Close the connection.

        Note:
            This method is what is override to the 'close' method of child
            class.
        """
        pass

    def send(self, msg):
        """Send a message to a device.
        
        Note:
            This method is what is override to the 'send' method of child
            class.
        """
        pass

    def recv(self, byte):
        """Receive messages from a device.

        Note:
            This method is what is override to the 'recv' method of child
            class.
        """
        pass

    def readline(self):
        """Read a line of a device output.

        Note:
            This method is what is override to the 'readline' method of child
            class.
        """
        pass
