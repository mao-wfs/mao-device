# -*- coding: utf-8 -*-
import json
from functools import partial
from pathlib import Path
from ..device import Device

SCPI_JSON_PATH = Path('./scpi.json').expanduser()


class ScpiCommon(Device):
    """Common SCPI commands.

    This class is for handling common SCPI commands.
    This class reads SCPI commands from 'scpi.json' and attributes them.
    This is based on 'Device'.

    Note:

    Args:
        com: Communicator instance to control the device.
    """
    _scpi_enable = 'ALL'

    def __init__(self, com):
        super().__init__(com)
        with SCPI_JSON_PATH.open(mode='r') as f:
            scpi_dict = json.load(f)

        self._add_scpi_methods(scpi_dict)

    def _add_scpi_methods(self, scpi_dict):
        """Add common SCPI commands.

        Example:
            These 2 commands are equivalent as follows.
            >>> scpi = ScpiCommon(com)
            >>> # *AAD: Accept Address
            >>> scpi.AAD == scpi.accept_address
            True
            >>> # *CAL?: Calibration Query
            >>> scpi.CALQ == scpi.calibrate_query # ? -> Q
            True

        Args:
            scpi_dict (dict): SCPI commands dictionary.

        Return:
            None
        """
        if self._scpi_enable == 'ALL':
            add_items = scpi_dict.items()
        else:
            add_items = (
                (enable_cmd, scpi_dict[enable_cmd])
                for enable_cmd in self._scpi_enable.split(' ')
            )

        for scpi_cmd, cmd_dict in add_items:
            if cmd_dict['type'] == 'command':
                method = self.com.send
            elif cmd_dict['type'] == 'query':
                method = self.com.query

            method = partial(method, msg=scpi_cmd)
            method.__doc__ = cmd_dict['doc']

            self.__setattr__(
                scpi_cmd.replace('*', '').replace('?', 'Q'),
                method,
            )
            self.__setattr__(cmd_dict['verbose_cmd'], method)

        return
