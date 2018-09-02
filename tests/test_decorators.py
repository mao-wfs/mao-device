# -*- coding: utf-8 -*-
import pytest
from maodevice.utils.decorators import (
    chooser,
    decoder,
    limitter,
)


def test_chooser():
    """Test function of 'maodevice.utils.decorators.chooser'
    """
    @chooser("arg", (1, 2, 3))
    def func(arg):
        return "Hello world!"

    assert func(arg=2) == "Hello world!"

    with pytest.raises(AssertionError):
        func(arg=10)


def test_decoder():
    """Test function of 'maodevice.utils.decorators.decoder'
    """
    @decoder
    def success_func():
        return b"Hello world!"

    @decoder
    def exception_func():
        return "Hello world!"

    assert success_func() == "Hello world!"

    with pytest.raises(AssertionError):
        exception_func()


def test_limitter():
    """Test function of 'maodevice.utils.decorators.limitter'
    """
    @limitter("arg", 0.01, 4.99, 0.01)
    def func(arg):
        return "Hello world!"

    assert func(3.22) == "Hello world!"

    @pytest.mark.parametrize(
        "arg, expected",
        [
            ("foo", pytest.raises(AssertionError)),
            (5.00, pytest.raises(AssertionError)),
            (3.235, pytest.raises(AssertionError)),
        ],
    )
    def test_exception(arg, expected):
        with expected:
            func(arg=arg)
