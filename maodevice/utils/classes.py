# coding: utf-8
from types import FunctionType


class ErrorHandler(object):
    """Error Handler of devices.

    This is the base class for handling errors of a device.

    Note:
        This class itself is not used, but it is inherited by
        child classes and used.
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
        """Handle error of a device

        Note:
            This method is overridden in the child class.

        Args:
            method (function): A method to be wrapped
        """
        pass
