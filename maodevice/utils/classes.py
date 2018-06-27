# coding: utf-8
from types import FunctionType
from functools import wraps


class ErrorHandler(object):
    """Error Handler of devices.

    This is the base class for handling error of a device.
    Various classes to handle error of devices are created inheriting this class.

    Note:
        - This class is used as metaclass.
        - This class itself is not used, but it is used by inheriting in
          a child class.
    """
    def __new__(meta, classname, bases, classDict):
        """
        """
        newClassDict = {}
        for attributeName, attribute in classDict.items():
            if isinstance(attribute, FunctionType):
                attribute = self._error_handler(attribute)
            newClassDict[attributeName] = attribute
        return object.__new__(meta, classname, bases, newClassDict)

    def _error_handler(self, method):
        """Handle error of a device.

        Note:
            This method is used to override in child classes.

        Args:
            method (function): A method to be wrapped.
        """
        pass
