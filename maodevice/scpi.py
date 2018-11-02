# -*- coding: utf-8 -*-
from maodevice.core import BaseDeviceHandler


class ScpiCommonCommands(BaseDeviceHandler):
    """IEEE-488.2 common commands.

    This class is for handling IEEE-488.2 common commands.

    Attribute:
        SCPI_DICT (dict): Dictionary of IEEE-488.2 common commands.
    """
    SCPI_DICT = {
        "*CLS":  "clear_status",
        "*ESE":  "standard_event_status_enable",
        "*OPC":  "operation_complete",
        "*PSC":  "power_on_status_clear",
        "*RCL":  "recall",
        "*RST":  "reset",
        "*SAV":  "save",
        "*SRE":  "service_request_enable",
        "*TRG":  "trigger",
        "*WAI":  "wait_to_continue",
        "*ESE?": "standard_event_status_enable_query",
        "*ESR?": "standard_event_status_register_query",
        "*IDN?": "identification_query",
        "*LRN?": "learn_device_setup_query",
        "*OPC?": "operation_complete_query",
        "*PSC?": "power_on_status_clear_query",
        "*SRE?": "service_request_enable_query",
        "*STB?": "read_status_byte_query",
        "*TST?": "self_test",
    }

    def clear_status(self):
        """CLS: Clear Status

        This commands clear the status byte, the data questionable
        event register, the standard event status register, the
        standard operation status register, and any other registers
        that are summarized in the byte.

        Args:
            None

        Return:
            None
        """
        self.com.send("*CLS")
        return

    def standard_event_status_enable(self, bit):
        """ESE: Standard Event Status Enable

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
            bit (int): Standard event register bits to be turned on.

        Return:
            None

        Example:
            Bit 4 and bit 5 of the enable register are on::

                >>> standard_event_status_enable(24) # 0b11000, 0x18
        """
        self.com.send(f"*ESE {bit}")
        return

    def operation_complete(self):
        """OPC: Operation Complete

        This command sets bit 0 in the standard event status register
        when all pending operations have finished.

        Args:
            None

        Return:
            None
        """
        self.com.send("*OPC")
        return

    def power_on_status_clear(self, status):
        """PSC: Power on Status Clear

        This command turns on / off clearing of the specific enable
        register at power on.

        Args:
            status (int): 1 is on, 0 is off.

        Return:
            None
        """
        self.com.send(f"*PSC {status}")
        return

    def recall(self, mem_loc):
        """RCL: Recall

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
        """RST: Reset

        This command resets the instrument to a factory pre-defined
        condition.

        Args:
            None

        Return:
            None
        """
        self.com.send("*RST")
        return

    def save(self, mem_loc):
        """SAV: Save

        This command save the complete instrument setting to memory.

        Args:
            mem_loc (int): Memory location.
                Allowed values are 0, 1, 2, 3 or 4.

        Return:
            None
        """
        self.com.send(f"*SAV {mem_loc}")
        return

    def service_request_enable(self, bit):
        """SRE: Service Request Enable

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
            bit (int): Standard event register bits to be turned on.
        """
        self.com.send(f"*SRE {bit}")
        return

    def trigger(self):
        """TRG: Trigger

        This command triggers the device if, and only if, Bus
        Triggering is the type of trigger event selected. Otherwise,
        TRG is ignored.

        Args:
            None

        Return:
            None
        """
        self.com.send("*TRG")
        return

    def wait_to_continue(self):
        """WAI: Wait-to-Continue

        This command causes the instrument to wait until all pending
        commands are completed, before executing any other commands.

        Args:
            None

        Return:
            None
        """
        self.com.send("*WAI")
        return

    def standard_event_status_enable_query(self):
        """ESE?: Standard Event Status Enable query

        This queries the status of standard event status enable
        register. This is a destructive read.

        Args:
            None

        Return:
            ret (bytes): Standard event status enable register.
        """
        ret = self.com.query("*ESE?")
        return ret
    
    def standard_event_status_register_query(self):
        """ESR?: Standard Event Status Register query

        This queries the value of the standard event status register.

        Args:
            None

        Return:
            ret (bytes): Standard event status register.
        """
        ret = self.com.query("*ESR?")
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
            ret (bytes): String that identify the device.
        """
        ret = self.com.query("*IDN?")
        return ret

    def learn_device_setup_query(self):
        """LRN? Learn Device Setup query

        This query returns instrument settings by binary block data
        (same as Save/Recall state file contents) with "SYSTem:SET"
        prefix.
        The returned data is the same as the contents of state file
        which can be saved by the SCPI.MMEMory.STORe.STATe. Therefore,
        the returned data contents is changed according to the setting
        of SCPI.MMEMory.STORe.STYPe.

        Args:
            None

        Return:
            ret (bytes): Instruments settings by binary block data
        """
        ret = self.com.query("*LRN?")
        return ret
 
    def operation_complete_query(self):
        """OPC?: Operation Complete query

        This queries bit 0 in the standard event status register. The
        signal generator will return an ASCII "1" when all pending
        operations have finished.

        Args:
            None

        Return:
            ret (bytes): ASCII "1".
        """
        ret = self.com.query("*OPC?")
        return ret

    def power_on_status_clear_query(self):
        """PSC?: Power on Status Clear query

        This command queries the power on status clear setting.

        Args:
            None

        Return:
            ret (bytes): On (1) or Off (0).
        """
        ret = self.com.query("*PSC?")
        return ret

    def service_request_enable_query(self):
        """SRE?: Service Request Enable query

        This queries the value of the service request enable
        register.

        Args:
            None

        Return:
            ret (bytes): Status byte register.
        """
        ret = self.com.query("*SRE?")
        return ret

    def read_status_byte_query(self):
        """STB?: Read Status Byte query

        This queries the status byte. This is a non-destructive read.

        Args:
            None

        Return:
            ret (bytes): Status byte register bits to be turned on.
        """
        ret = self.com.query("*STB?")
        return ret

    def self_test(self):
        """TST?: Self-Test query

        This query returns the result of the power-up selftest.

        Args:
            None

        Return:
            ret (int): 0 (Passed) or 1 (Failed).
        """
        ret = self.com.send("*TST?")
        return ret


class ScpiHandler(BaseDeviceHandler):
    """Handle IEEE-488.2 common commands.

    Note:
        If you limit IEEE-488.2 common commands, write it as follows
        before instantiation.
        When you use only CLS and RST,::

            >>> enable_cmds = ["*CLS", "*RST"]

    Args:
        com (maodevice.communicator):
            Communicator instance to control the device.

    Attribute:
        enable_cmds (:obj:`list` of :obj:`str`):
            IEEE-488.2 common commands to use.
    """
    enable_cmds = ["*CLS", "*ESE", "*OPC", "*PSC", "*RCL",
                   "*RST", "*SAV", "*SRE", "*TRG", "*WAI",
                   "*ESE?", "*ESR?", "*IDN?", "*LRN?",
                   "*OPC?", "*PSC?", "*SRE?", "*STB?", "*TST?"]

    def __init__(self, com):
        super().__init__(com)
        self._scpi = ScpiCommonCommands(com)
        self._add_scpi_methods()

    def _add_scpi_methods(self):
        """Add methods of IEEE-488.2 common commands.

        Note:
            This method is only for the internal use.

        Return:
            None
        """
        scpi_dict = self._scpi.SCPI_DICT
        add_cmds = [(cmd, scpi_dict[cmd]) for cmd in self.enable_cmds]

        for cmd, verbose_cmd in add_cmds:
            self.__setattr__(
                verbose_cmd,
                self._scpi.__getattribute__(verbose_cmd),
            )
            fix_cmd = cmd.replace("*", "").replace("?", "Q")
            self.__setattr__(fix_cmd, self.__getattribute__(verbose_cmd))

        return