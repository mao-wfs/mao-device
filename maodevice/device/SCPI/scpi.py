# -*- coding: utf-8 -*-
from ..device import Device


class ScpiCommon(Device):
    """IEEE-488.2 common commands.

    This class is for handling IEEE-488.2 common commands.
    This class is based on 'Device'.

    Attribute:
        scpi_dict (dict): Dictionary of IEEE-488.2 common commands.
    """
    scpi_dict = {
        '*CLS': 'clear_status',
        '*ESE': 'standard_event_status_enable',
        '*ESE?': 'standard_event_status_enable_query',
        '*ESR?': 'standard_event_status_register_query',
        '*IDN?': 'identification_query',
        '*OPC': 'operation_complete',
        '*OPC?': 'operation_complete_query',
        '*PSC': 'power_on_status_clear',
        '*PSC?': 'power_on_status_clear_query',
        '*RCL': 'recall',
        '*RST': 'reset',
        '*SAV': 'save',
        '*SRE': 'service_request_enable',
        '*SRE?': 'service_request_enable_query',
        '*STB?': 'read_status_byte_query',
        '*TRG': 'trigger',
        '*TST?': '*self_test',
        '*WAI': 'wait_to_continue',
    }

    def clear_status(self):
        """*CLS: Clear Status

        This commands clear the status byte, the data questionable
        event register, the standard event status register, the
        standard operation status register, and any other registers
        that are summarized in the byte.

        Args:
            None

        Return:
            None

        Example:
            >>> s.clear_status()
        """
        self.com.send('*CLS')
        return

    def standard_event_status_enable(self, *bits):
        """*ESE: Standard Event Status Enable

        This command sets the standard event status enable register.

        Note:
            The standard event register is described below.
            - 0 (1): Operation Complete
            - 1 (2): Unused
            - 2 (4): Query Error
            - 3 (8): Device Error
            - 4 (16): Execution Error
            - 5 (32): Command Error
            - 6 (64): Unused
            - 7 (128): Power On

        Args:
            bits (:obj:`tuple` of :obj:`int`): Standard event register
                bits to be turned on.

        Return:
            None

        Example:
            Bit 4 and bit 5 of the enable register are on.
            >>> s.standard_event_status_enable(4, 5)
        """
        d_sum = self._decimal_sum_of_bits(bits)
        self.com.send(f"*ESE {d_sum}")
        return

    def standard_event_status_enable_query(self):
        """*ESE?: Standard Event Status Enable query

        This queries the status of standard event status enable
        register. This is a destructive read.

        Args:
            None

        Return:
            ret (:obj:`list` of :obj:`int`): Standard event status
                enable register.

        Example:
            When bit 1, bit 3, bit 5 are enable.
            >>> s.standard_event_status_enable_query()
            [1, 3, 5]
        """
        ret = self.com.query('*ESE?')
        ret = self._extract_bits(ret)
        return ret

    def standard_event_status_register_query(self):
        """*ESR?: Standard Event Status Register query

        This queries the value of the standard event status register.

        Args:
            None

        Return:
            ret (:obj:`list` of :obj:`int`): Standard event status
                register.

        Example:
            When bit 3 and bit 4 are going.
            >>> s.standard_event_status_register_query()
            [3, 4]
        """
        ret = self.com.query("*ESR?")
        ret = self._extract_bits(ret)
        return ret

    def identification_query(self):
        """IDN? Idntification query

        This query outputs an identifying string to the GPIB. The response
        for the signal generator will be a storing that shows the actual
        model number, serial number and firmware revision will be
        substituted.

        Args:
            None

        Return:
            ret (str): String that identify the device.
        """
        ret = self.com.query("*IDN?")
        return ret

    def operation_complete(self):
        """*OPC: Operation Complete

        This command sets bit 0 in the standard event status register
        when all pending operations have finished.

        Args:
            None

        Return:
            None
        """
        self.com.send('*OPC')
        return

    def operation_complete_query(self):
        """*OPC?: Operation Complete query

        This queries bit 0 in the standard event status register. The
        signal generator will return an ASCII '1' when all pending
        operations have finished.

        Args:
            None

        Return:
            ret (str): ASCII '1'.
        """
        ret = self.com.query('*OPC?')
        return ret

    def power_on_status_clear(self, status):
        """*PSC: Power on Status Clear

        This command turns on / off clearing of the specific enable
        register at power on.

        Args:
            status (int): 1 is on, 0 is off.

        Return:
            None
        """
        self.com.send(f"*PSC {status}")
        return

    def power_on_status_clear_query(self):
        """*PSC?: Power on Status Clear query

        This command queries the power on status clear setting.

        Args:
            None

        Return:
            ret (int): On (1) or Off (0).
        """
        ret = self.com.query('*PSC?')
        return ret

    def recall(self, mem_loc):
        """*RCL: Recall

        This command recall the complete instrument setting from memory.

        Args:
            mem_loc (int): Memory location.
                Allowed values are 0, 1, 2, 3 or 4.

        Return:
            None
        """
        self.com.send(f"*RCL {mem_loc}")
        return

    def reset(self):
        """*RST: Reset

        This command resets the instrument to a factory pre-defined
        condition.

        Args:
            None

        Return:
            None
        """
        self.com.send('*RST')
        return

    def save(self, mem_loc):
        """*SAV: Save

        This command save the complete instrument setting to memory.

        Args:
            mem_loc (int): Memory location.
                Allowed values are 0, 1, 2, 3 or 4.

        Return:
            None
        """
        self.com.send(f"*SAV {mem_loc}")
        return

    def service_request_enable(self, *bits):
        """*SRE: Service Request Enable

        This command sets the value of the service request enable
        register.

        Note:
            The status byte register is described below.
            - 0 (1): Unused
            - 1 (2): Unused
            - 2 (4): Error Queue
            - 3 (8): Questionable Data Register
            - 4 (16): Output Buffer
            - 5 (32): Standard Event Register
            - 6 (64): Status Byte Register
            - 7 (128): Unused

        Args:
            bits (:obj:`tuple` of :obj:`int`): Standard event register
                bits to be turned on.
        """
        d_sum = self._decimal_sum_of_bits(bits)
        self.com.send(f"*SRE {d_sum}")
        return

    def service_request_enable_query(self):
        """*SRE?: Service Request Enable query

        This queries the value of the service request enable
        register.

        Args:
            None

        Return:
            ret (:obj:`list` of :obj:`int`): Standard event status
                enable register.
        """
        ret = self.com.query('*SRE?')
        ret = self._extract_bits(ret)
        return ret

    def read_status_byte_query(self):
        """*STB?: Read Status Byte query

        This queries the status byte. This is a non-destructive read.

        Args:
            None

        Return:
            ret (:obj:`list` of :obj:`int`): Status byte register bits
                to be turned on.
        """
        ret = self.com.query('*STB?')
        ret = self._extract_bits(ret)
        return ret

    def trigger(self):
        """*TRG: Trigger

        This command triggers the device if, and only if, Bus
        Triggering is the type of trigger event selected. Otherwise,
        *TRG is ignored.

        Args:
            None

        Return:
            None
        """
        self.com.send('*TRG')
        return

    def self_test(self):
        """*TST?: Self-Test query

        This query returns the result of the power-up selftest.

        Args:
            None

        Return:
            ret (int): 0 (Passed) or 1 (Failed).
        """
        ret = self.com.query('*TST?')
        return ret

    def wait_to_continue(self):
        """*WAI: Wait-to-Continue

        This command causes the instrument to wait until all pending
        commands are completed, before executing any other commands.

        Args:
            None

        Return:
            None
        """
        self.com.send('*WAI')
        return

    def _decimal_sum_of_bits(self, *bits):
        """Sum of decimal bits.

        Note:
            This method is for internal use.

        Args:
            *bits (:obj:`tuple` of :obj:`int`): Bit for adding.

        Return:
            d_sum (int): Decimal sum of bits.

        Example:
            >>> s._decimal_sum_of_bits(1, 3, 5)
            42 # 0b00101010
        """
        d_sum = sum(2**i for i in bits)
        return d_sum

    def _extract_bits(self, d_sum):
        """Extract digits (bits) which is 1 in binary number.

        Note:
            This method is for internal use.

        Args:
            d_sum (int): Decimal sum of bits.

        Return:
            bits (:obj:`list` of :obj:`int`): Digits (bits) which is 1
                in binary number.

        Example:
            >>> s._extract_bits(42)
            [1, 3, 5]
        """
        bits = f"{d_sum:08b}"
        bits = [i for i, x in enumerate(reversed(bits)) if x == '1']
        return bits


class ScpiFamily(Device):
    """Handle IEEE-488.2 common commands

    This class is based on 'Device'.

    Note:
        If you limit IEEE-488.2 common commands, write it as follows
        before instantiation.

        - When you use only *CLS and *RST
        >>> _scpi_enable = ('*CLS', '*RST')

        - When you use all IEEE-488.2 common commands.
        >>> _scpi_enable = 'ALL'

    Args:
        com: Communicator instance to control the device.

    Attribute:
        _scpi_enable (str or :obj:`list` of :obj:`str`):
            IEEE-488.2 common commands to use.
    """
    _scpi_enable = 'ALL'

    def __init__(self, com):
        super().__init__(com)
        self._scpi = ScpiCommon(com)
        self._add_scpi_methods()

    def _add_scpi_methods(self):
        """Add methods of IEEE-488-2 common commands.

        Note:
            This method is only for the internal use.

        Return:
            None
        """
        scpi_dict = self._scpi.scpi_dict
        if self._scpi_enable == 'ALL':
            add_items = scpi_dict.items()
        else:
            add_items = [
                [enable, scpi_dict[enable]] for enable in self.scpi_enable
            ]

        for cmd, verbose_cmd in add_items:
            self.__setattr__(
                verbose_cmd,
                self._scpi.__getattribute__(verbose_cmd),
            )
            fix_cmd = cmd.replace('*', '').replace('?', 'Q')
            self.__setattr__(fix_cmd, self.__getattribute__(verbose_cmd))

        return
