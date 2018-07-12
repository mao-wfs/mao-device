# -*- coding: utf-8 -*-
from types import FunctionType


class ErrorHandler(type):
    """Error Handler of devices.

    This is the base class for handling errors of a device.

    Note:
        This class itself is not used, but it is inherited by
        child classes and used.
    """
    def __new__(meta, class_name, bases, class_dict):
        """
        """
        new_class_dict = {}
        for attribute_name, attribute in class_dict.items():
            if isinstance(attribute, FunctionType):
                if not attribute_name.startswith('__'):
                    attribute = meta._error_handler(attribute)
            new_class_dict[attribute_name] = attribute
        return type.__new__(meta, class_name, bases, new_class_dict)

    @classmethod
    def _error_handler(cls, method):
        """Handle error of a device.

        Note:
            This method is overridden in the child class.

        Args:
            method (function): A method to be wrapped
        """
        pass
