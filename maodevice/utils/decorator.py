# -*- coding: utf-8 -*-
__all__ = [
    'chooser',
    'decoder',
    'limitter',
]

import decimal
from functools import wraps
from inspect import signature


def chooser(arg_name, choice_list):
    """Check whether the value in the choices.

    Note:
        This function is intended to be used as a decorator like follows.
        >>> @chooser('arg_name', some_choice_list):
        >>> def func(*args, **kwargs):
        >>>     # do something
        >>>     return

    Args:
        arg_name (str): Name of the specified argument.
        choice_list (list): List of choices.

    Raises:
        AssertionError: If the value of 'arg_name' is not in the 'choice_list'.
    """
    def _chooser(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_val = get_arg_value(arg_name, func, *args, **kwargs)

            assert arg_val in choice_list, \
                f"{arg_name}: expected to be in 'choice_list'."

            return func(*args, **kwargs)
        return wrapper
    return _chooser


def decoder(func):
    """Decode bytes objects.

    Note:
        This function is intended to be used as a decorator like follows.
        >>> @decoder
        >>> def func(*args, **kwargs):
        >>>     # do something
        >>>     return ret

    Args:
        func (function): Function to be wrapped.

    Return:
        wrapper (function): A wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)

        assert isinstance(ret, bytes), \
            "The return value is expected to be `bytes`."

        ret.decode()
        return ret
    return wrapper


def get_arg_value(arg_name, func, *func_args, **func_kwargs):
    """Get the value of the specified argument from the function.

    Args:
        arg_name (str): Name of the specified argument.
        func (function): Function with 'arg_name'.
        *func_args: Variable lengh arguments of 'func'.
        *func_kwargs: Arbitary keyword arguments of 'func'.

    Return:
        arg_val: Value of 'arg_name'.

    Raises:
        TypeError: If 'func' does not have the argument 'arg_name'.
    """
    sig = signature(func)
    bound_args = sig.bind(*func_args, **func_kwargs)

    if arg_name in bound_args.keys():
        arg_val = bound_args.argument[arg_name]
    else:
        raise TypeError(
            f"{func.__name__}: does not have the argument '{arg_name}'."
        )

    return arg_val


def limitter(arg_name, min_val, max_val, step):
    """Limit the value of the specified argument.

    Note:
        This function is intended to be used as a decorator like follows.
        >>> @limitter('arg_name', 0.01, 4.99, 0.01)
        >>> def func(*args, **kwargs):
        >>>     # do something
        >>>     return

    Args:
        arg_name (str): Name of the specified value.
        min_val (int or float): Minimum number of the range.
        max_val (int or float): Maximum number of the range.
        step (int or float): Step number.

    Raises:
        AssertionError: If the value of 'arg_name'
            is not expected type and value.
    """
    def _limitter(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_val = get_arg_value(arg_name, func, *args, **kwargs)

            assert isinstance(arg_val, (int, float)), \
                f"{arg_name}: expected to be `int` of `float`"

            assert min_val <= arg_val <= max_val, \
                f"{arg_name}: expected to be in the range of" \
                f" {min_val} - {max_val}"

            if isinstance(arg_val, int):
                is_correct_step = arg_val % step == 0
            else:
                arg_val_ = decimal.Decimal(str(arg_val))
                step_ = decimal.Decimal(str(step))
                is_correct_step = (arg_val_ % step_).is_zero()

            assert is_correct_step, \
                f"{arg_name}: expected to be a multiple of {step}."

            return func(*args, **kwargs)
        return wrapper
    return _limitter
