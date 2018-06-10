# coding: utf-8
class Device(object):
    """The base class to control devices.
    
    This is the base class for controlling devices.
    Various classes to control devices are created inheriting this class.

    Note:
        You do not use this class itself. You override this class and create a
        class corresponding to each device. 

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
        com (Communicator): Communicator for controlling the device.
        _shortcut_command (dict): Dictionary of methods and its shortcuts
    """
    manufacturer = ''
    product_name = ''
    classification = ''

    com = None
    _shortcut_command = {}

    def __init__(self, com):
        """Initialize 'Device'.

        Args:
            com (): Communicator to control the device.
        """
        self.com = com
        self.com.open()
        self._add_shorcut_command()

    def _add_shorcut_command(self):
        """Add shortcut commands to control device.
        
        Note:
            This method is only for the internal use.
            User can add shortcuts by editting '_shortcut_command'.
        """
        items = self._shortcut_command.items()
        for shortcut, method in items:
            self.__setattr__(shortcut, self.__getattribute__(method))
        return
