# -*- coding: utf-8 -*-
__all__ = [
    'decoder',
    'filter',
]

from functools import wraps
from inspect import signature
import numpy as np


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
        ret = func(*args, **kwargs)

        if isinstance(ret, bytes):
            ret = ret.decode()
        elif isinstance(ret, list) and all(isinstance(elem, bytes) for elem in ret):
            ret = [elem.decode() for elem in ret]
        else:
            raise TypeError(
                'The return value is not `bytes` and `list` of `bytes`.'
            )

        return ret
    return wrapper


class Check(object):
    """Check the value of the specified argument.

    This is the base class to check the value of the specified argument.

    Note:
        This class itself is not used, but it is inherited by
        child classes and uses.

    Args:
        arg_name (str): Name of the specified argument.
    """
    def __init__(self, arg_name):
        self.arg_name = arg_name

    def __call__(self, func):
        """Function like a decorator.

        Note:
            This method is overrided '__call__' to function as a decorator.

        Args:
            func (function): A function to be wrapped.

        Raises:
            KeyError: If 'func' does not have the argument 'self.arg_name'.

        Return:
            wrapper (function): A wrapped function.
        """
        sig = signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)

            if self.arg_name in bound_args.arguments.keys():
                arg_val = bound_args.arguments[self.arg_name]
                self._check(arg_val)
            else:
                raise KeyError(
                    f"'{func.__name__}' does not have"
                    f" the argument '{self.arg_name}'."
                )

            return func(*args, **kwargs)
        return wrapper

    def _check(self, val):
        """Check the specified value.

        This is the base method to check the specified value.

        Note:
            This method is overridden in the child class.

        Args:
            val (int or float or str): Value to check.
        """
        pass


class filter(Check):
    """Filter the value of the specified argument.

    This class is based on 'Check'.

    Note:
        This class is intended to be used as a decorator like follows.
        >>> @filter('arg_name', 0.01, 4.99, 0.01)
        >>> def func(*args, **kwargs):
        >>>     # Do something.
        >>>     return

    Args:
        arg_name (str): Name of the specified value.
        min_val (int or float): Minimum number of the range.
        max_val (int or float): Maximum number of the range.
        step (int or float): Step number.
    """
    def __init__(self, arg_name, min_val, max_val, step):
        super().__init__(arg_name)
        self.min_val = min_val
        self.max_val = max_val
        self.step = step

    def _check(self, val):
        """Check the specified value.

        Note:
            This method is override the `_check` in the base class.

        Args:
            val (int or float): Value to check.

        Raises:
            AssertionError: If 'val' is not the expected type and value.

        Return:
            None
        """
        assert isinstance(val, (int, float)), \
            'The specified value is expected to be `int` or `float`.'

        _specified_range = np.arange(
            self.min_val,
            self.max_val + self.step,
            self.step,
        )
        assert val in _specified_range, \
            'The specified value is expected to be in tha range of' \
            f' {self.min_val} - {self.max_val} of the step {self.step}.'

        return
