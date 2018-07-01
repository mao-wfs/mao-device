# coding: utf-8
class Device(object):
    """Control a device

    This is the base class of device controller.

    Note:
        This class itself is not used, but it is inherited by
        child classes and used.

    Args:
        com: Communicator instance to control the device

    Attributes:
        manufacturer (str): Manufacturer of the device
        product_name (str): Name of the device
        classification (str): Classification of the device
        _shortcut_command (dict): Dictionary of methods and its shortcuts
    """
    manufacturer = ''
    product_name = ''
    classification = ''

    _shortcut_command = {}

    def __init__(self, com):
        self.com = com
        self.com.open()
        self._add_shorcut_command()

    def _add_shorcut_command(self):
        """Add shortcut commands to control device

        Note:
            This method is only for the internal use.
            You can add shortcuts by editting '_shortcut_command'.

        Return:
            None
        """
        _items = self._shortcut_command.items()
        for shortcut, method in _items:
            self.__setattr__(shortcut, self.__getattribute__(method))
        return
