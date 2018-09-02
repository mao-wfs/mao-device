# -*- coding: utf-8 -*-
import pytest
from maodevice.utils.decorators import (
    chooser,
    decoder,
    get_arg_value,
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


def test_get_arg_value():
    """Test function of 'maodevice.utils.decorator.get_arg_value'
    """
    # Test using "chooser"
    @chooser("foo", (1, 2, 3))
    def chooser_func(arg):
        return "Hello world!"

    with pytest.raises(TypeError):
        chooser_func(arg=2)

    # Test using "limitter"
    @limitter("foo", 0.01, 4.99, 0.01)
    def limitter_func(arg):
        return "Hello world!"

    with pytest.raises(TypeError):
        limitter_func(arg=2.37)


class TestLimitter(object):
    """Test class of 'maodevice.utils.decorators.decoder'
    """
    @pytest.mark.parametrize(
        "arg, min_val, max_val, step, expected",
        [
            (1024, 1, 32768, 1, "Hello world!"),
            (3.27, 0.01, 4.99, 0.01, "Hello world!"),
        ],
    )
    def test_success(self, arg, min_val, max_val, step, expected):
        """Test method for success
        """
        @limitter("arg", min_val, max_val, step)
        def func(arg):
            return "Hello world!"

        assert func(arg=arg) == expected

    @pytest.mark.parametrize(
        "arg, min_val, max_val, step, expected",
        [
            (3.27, 1, 1024, 1, pytest.raises(AssertionError)),
            (3, 0.01, 4.99, 0.01, pytest.raises(AssertionError)),
            ("foo",  1, 1024, 1, pytest.raises(AssertionError)),
            ("foo", 0.01, 4.99, 0.01, pytest.raises(AssertionError)),
            (6, 1, 50, 5, pytest.raises(AssertionError)),
            (3.235, 0.01, 4.99, 0.01, pytest.raises(AssertionError)),
        ]
    )
    def test_exception(self, arg, min_val, max_val, step, expected):
        """Test method for success
        """
        @limitter("arg", min_val, max_val, step)
        def func(arg):
            return "Hello world!"

        with expected:
            func(arg=arg)


if __name__ == "__main__":
    pytest.main()
