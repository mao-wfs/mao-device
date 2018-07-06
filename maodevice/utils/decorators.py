# -*- coding: utf-8 -*-
__all__ = [
    'decoder',
    'filter',
    'chooser',
]

import decimal
from functools import wraps
from inspect import signature


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
        elif isinstance(ret, list) and all(
            isinstance(elem, bytes) for elem in ret
        ):
            ret = [elem.decode() for elem in ret]
        else:
            raise TypeError(
                'The return value is not `bytes` and `list` of `bytes`.'
            )

        return ret
    return wrapper


def get_argument_value(arg_name, func, *func_args, **func_kwargs):
    """Get the value of the specified argument from the function.

    Args:
        arg_name (str): Name of the specified argument.
        func (function): Function with 'arg_name'.
        *func_args: Variable length arguments of 'func'.
        *func_kwargs: Arbitary keyword arguments of 'func'.

    Return:
        arg_val: Value of 'arg_name'.

    Raises:
        TypeError: If 'func' does not have the argument 'arg_name'.
    """
    sig = signature(func)
    bound_args = sig.bind(*func_args, **func_kwargs)

    if arg_name in bound_args.arguments.keys():
        arg_val = bound_args.arguments[arg_name]
    else:
        raise TypeError(
            f"'{func.__name__}' does not have the argument '{arg_name}'."
        )

    return arg_val


def filter(arg_name, min_val, max_val, step):
    """Filter the value of the specified argument.

    Note:
        Thie function is intended to used as a decorator like follows.
        >>> @filter('arg_name', 0.01, 4.99, 0.01)
        >>> def func(*args, **kwargs):
        >>>     # Do something.
        >>>     return

    Args:
        arg_name (str): Name of the specified value.
        min_val (int or float): Minimum number of the range.
        max_val (int or float): Maximum number of the range.
        step (int or float): Step number.

    Raises:
        AssertionError: If the value of 'arg_name'
            is not the expected type and value.
    """
    def _filter(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_val = get_argument_value(arg_name, func, *args, **kwargs)

            assert isinstance(arg_val, (int, float)), \
                f"'{arg_name}' is expected to be `int` or `float`."

            assert min_val <= arg_val <= max_val, \
                f"'{arg_name}' is expected to be in the range of" \
                f" {min_val} - {max_val}."

            assert not (
                isinstance(arg_val, float) and isinstance(step, int)
            ), \
                f"'{arg_name}' is expected to be `int` if 'step' is `int`."

            if isinstance(arg_val, int):
                correct_step = arg_val % step is 0
            else:
                arg_val_ = decimal.Decimal(str(arg_val))
                step_ = decimal.Decimal(str(step))
                correct_step = (arg_val_ % step_).is_zero()

            assert correct_step, \
                f"'{arg_name}' is expected to be a multiple of {step}."

            return func(*args, **kwargs)
        return wrapper
    return _filter


def chooser(arg_name, choice_list):
    """Check whether the value in the choices.

    Note:
        This function is intended to be used as a decorator like follows.
        >>> @chooser('arg_name', some_choice_list):
        >>> def func(*args, **kwargs):
        >>>     # Do something.
        >>>     return

    Args:
        arg_name (str): Name of the specified argument.
        choice_list (list): List of choices.

    Raises:
        AssertionError: If the value of 'arg_name'
            is not in the 'choice_list'.
    """
    def _chooser(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_val = get_argument_value(arg_name, func, *args, **kwargs)

            assert arg_val in choice_list, \
                f"'{arg_name}' is expected to be in {choice_list}."

            return func(*args, **kwargs)
        return wrapper
    return _chooser
