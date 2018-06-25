# coding: utf-8
__all__ = [
    'decoder',
]

from functools import wraps

def decoder(func):
    """Decode bytes objects.

    Note:
        This function is intended to be used as a decorator like follows.
        >>> @decoder
        >>> def func(*args, **kwargs):
        >>>     # Do something.
        >>>     return ret

    Args:
        func (function): Function to be wrapped.

    Return:
        wrapper (function): Wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        import warnings
        ret = func(*args, **kwargs)
        if isinstance(ret, bytes):
            ret = ret.decode()
        elif isinstance(ret, list) and all(isinstance(elem, bytes) for elem in ret):
            ret = [elem.decode() for elem in ret]
        else:
            warnings.warn('You should not use this function.')
        return ret
    return wrapper
