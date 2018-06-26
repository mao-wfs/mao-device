# coding: utf-8
__all__ = [
    'decoder',
    'filter',
    'increments',
]

from functools import wraps
from inspect import Parameter, signature
from warnings import warn

def decoder(func):
    """Decode bytes objects.

    Note:
        This function is intended to be used as a decorator like follows.
        >>> @decoder
        >>> def func(*args, **kwargs):
        >>>     # Do something.
        >>>     return ret

    Args:
        func (function) A function to be wrapped.

    Return:
        wrapper (function): A wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        from warnings import warn

        ret = func(*args, **kwargs)
        if isinstance(ret, bytes):
            ret = ret.decode()
        elif isinstance(ret, list) and all(isinstance(elem, bytes) for elem in ret):
            ret = [elem.decode() for elem in ret]
        else:
            warnings.warn('You should not use this decorator.')

        return ret
    return wrapper


class Check(object):
    """The base class to check the value of specified argument.

    This is the base class to check the value of specified argument.
    Various classes to check it are created inheriting this class.

    Note:
        You do not use this class itself. You override this class
        and create the child class for each decorator. 
    """
    def __init__(self, name):
        """Initialize 'Check'.

        Args:
            name (str): Name of the specified argument.
        """
        self.name = name

    def __call__(self, func):
        """Function like a decorator.

        Note:
            This method is overrided "__call__" to function as a decorator.

        Args:
            func (function) A function to be wrapped.

        Return:
            wrapper (function): A wrapped function.
        """
        sig = signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            params = sig.parameters
            for i, (key, val) in enumerate(params.items()):
                if not val.kind is Parameter.POSITIONAL_OR_KEYWORD:
                    break
                try:
                    kwargs.update({key: args[i]})
                except IndexError:
                    kwargs.setdefault(key, val.default)

            if self.name in kwargs.keys():
                self._check(kwargs)
            else:
                raise KeyError(
                    f'"{func.__name__}" does not have the argument "{self.name}"'
                )

            return func(**kwargs)
        return wrapper

    def _check(self, kwargs_):
        """Check the value to set a device.

        This method is the base method to check the value of specified
        argument.
        This method is used in "__call__" method.

        Note:
            You override this method in child class.
        
        Args:
            kwargs_ (dict): Arbitrary keyword arguments.
        """
        pass


class filter(Check):
    """Filter the setting value.

    This class is based on 'Check'

    Note:
        This class is intended to be used as a decorator like follows.
        >>> @filter('name', 0.01, 4.99)
        >>> def func(name, *args, **kwargs):
        >>>     # Do something.
        >>>     return
    """
    def __init__(self, name, min_, max_):
        """Initialize 'filter'.

        Args:
            name (str): Name of the specified argument.
            min_ (int or float): Minimum value of setting to a device.
            max_ (int or float): Maximum value of setting to a device.
        """
        super().__init__(name)
        self.min = min_
        self.max = max_

    def _check(self, kwargs_):
        """Check the value to set a device.

        Note:
            This method is overrided "_check" in the base class.

        Args:
            kwargs_ (dict): Arbitrary keyword arguments.

        Return:
            None
        """
        if not isinstance(kwargs_[self.name], (int, float)):
            raise TypeError(f'"{self.name}" must be int or float.')

        value = kwargs_[self.name]
        if not self.min <= value <= self.max:
            warn(
                f'\n\tSet value: {value}' + \
                f'\n\tYou should set "{self.name}" {self.min} - {self.max}.'
            )
            kwargs_[self.name] = self.min if value < self.min else self.max
        return


class increments(Check):
    """Check and modify the increments of the value to set a device.

    This class is based on 'Check'.

    Note:
        This class is intended to be used as a decorator like follows.
        >>> @increments('name', 0.5)
        >>> def func(name, *args, **kwargs):
        >>>     # Do something.
        >>>     return
    """
    def __init__(self, name, inc):
        """Initialize 'increments'.

        Args:
            name (str): Name of the specified argument.
            inc (int or float): The increments of the value to set a device.
        """
        super().__init__(name)
        self.inc = inc

    def _check(self, kwargs_):
        """Check the value to set a device.

            Note:
                This method is overrided "_check" in the base class.

            Args:
                kwargs_ (dict): Arbitrary keyword arguments.

            Return:
                None
        """
        if not isinstance(kwargs_[self.name], (int, float)):
            raise TypeError(f'"{self.name}" must be int or float.')

        value = kwargs_[self.name]
        reminder = value % self.inc
        if not reminder == 0:
            warn(
                f'\n\tSet value: {value}' + \
                f'\n\tYou should set "{self.name}" in multiples of {self.inc}.'
            )
            if reminder <= self.inc/ 2:
                kwargs_[self.name] = value - reminder
            else:
                kwargs_[self.name] = value - reminder + self.inc
        return
