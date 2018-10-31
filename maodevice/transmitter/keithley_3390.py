# -*- coding: utf-8 -*-
from maodevice.scpi import ScpiHandler
from maodevice.validators import Keithley3390Validator


class Keithley3390(ScpiHandler, metaclass=Keithley3390Validator):
    """Control "Model 3390 Arbitrary Waveform Generator".

    Note:
        This class is based on "maodevice.scpi.ScpiHandler".

    Attributes:
        MANUFACTURER (str): Manufacturer of the device.
        PRODUCT_NAME (str): Name of the device.
        CLASSIFICATION (str): Classification of the device.
        enable_cmds (:obj:`list` of :obj:`str`):
            IEEE-488.2 common commands to use.
    """
    MANUFACTURER = "Keithley"
    PRODUCT_NAME = "Model 3390 Arbitrary Waveform Generator"
    CLASSIFICATION = "Function generator"

    enable_cmds = ["*CLS", "*ESE", "*OPC", "*PSC", "*RCL",
                   "*RST", "*SAV", "*SRE", "*TRG", "*WAI",
                   "*ESE?", "*ESR?", "*IDN?", "*LRN?",
                   "*OPC?", "*PSC?", "*SRE?", "*STB?", "*TST?"]

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator("\n")

    def set_function(self, func):
        """Set function of the signal.

        Args:
            func (str): Function of the signal.

        Return:
            None
        """
        self.com.send(f"FUNC {func}")
        return

    def query_function(self):
        """Query the function of the signal.

        Return:
            ret (bytes): Function of the signal.
        """
        ret = self.com.query('FUNC?')
        return ret

    def set_frequency(self, freq):
        """Set frequency of the signal.

        Args:
            freq (float): Value of the frequency.

        Return:
            None
        """
        self.com.send(f"FREQ {freq}")
        return

    def query_frequency(self):
        """Query frequency of the signal.

        Return:
            ret (bytes): The frequency value in Hz.
        """
        ret = self.com.query('FREQ?')
        return ret

    def set_voltage(self, volt, unit="dBm"):
        """Set voltage of the signal.

        Args:
            volt (float): An voltage value.
            unit (str): An unit of the voltage. (Default: 'dBm')

        Return:
            None
        """
        self.com.send(f"VOLT {volt}")
        self.com.send(f"VOLT:UNIT {unit}")
        return

    def query_voltage(self):
        """Query voltage of the signal.

        Return:
            ret (float): The voltage value in the specified unit.
        """
        ret = self.com.query('VOLT?')
        return ret

    def set_dc_offset_voltage(self, v_off):
        """Set DC offset voltage of the signal.

        Args:
            v_off (float): The DC offset voltage values.

        Return:
            None
        """
        self.com.send(f"VOLT:OFFS {v_off}")
        return

    def query_offset_voltage(self):
        """Query the DC offset voltage of the signal.

        Return:
            ret (float): The DC offset voltage value.
        """
        ret = self.com.query('VOLT:OFFS?')
        return ret

    def set_pluse_high_low_levels(self, v_hi, v_low):
        """Set pulse high and low levels.

        Args:
            v_hi (float): Pulse high level.
            v_low (float): Pulse low level.

        Return:
            None
        """
        self.com.send(f"VOLT:HIGH {v_hi}")
        self.com.send(f"VOLT:LOW {v_low}")
        return

    def query_pulse_high_low_levels(self):
        """Query pulse high and low levels.

        Return:
            ret (dict): Dictionary of Pulse high and low levels.
        """
        self.com.send('VOLT:HIGH?')
        _v_hi = self.com.readline()
        self.com.send('VOLT:LOW?')
        _v_low = self.com.readline()
        ret = {'HIGH': float(_v_hi), 'LOW': float(_v_low)}
        return ret

    def set_waveform_polarity(self, invert=False):
        """Set the waveform polarity.

        Args:
            invert (bool): If it is True,
                the waveform polarity is specified inverted.

        Return:
            None
        """
        _polarity = 'NORM' if not invert else 'INV'
        self.com.send(f'OUTP:POL {_polarity}')
        return

    def query_waveform_polarity(self):
        """Query waveform polarity.

        Return:
            ret (str): The waveform polarity.
        """
        ret = self.com.query('OUTP:POL?')
        return ret

    def set_output_termination(self, ohms):
        """Set the output termination.
        """
        self.com.send(f"OUTP:LOAD {ohms}")
        return

    def enable_output(self):
        """Enables the RF output.

        Return:
            None
        """
        self.com.send('OUTP ON')
        return

    def disable_output(self):
        """Disable the RF output.

        Return:
            None
        """
        self.com.send('OUTP OFF')
        return

    def enable_synchronize(self):
        """Enable synchronization.

        Return:
            None
        """
        self.com.send('OUTP:SYNC ON')
        return

    def disable_synchronize(self):
        """Disable synchronization.

        Return:
            None
        """
        self.com.send('OUTP:SYNC OFF')
        return
