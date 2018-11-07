# -*- coding: utf-8 -*-
from maodevice.scpi import ScpiHandler
from maodevice.validators import Model3390AWGValidator


class Model3390AWG(ScpiHandler, metaclass=Model3390AWGValidator):
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

    def enable_output(self):
        """Enable the output of a signal.

        Return:
            None
        """
        self.com.send("OUTP ON")
        return

    def disable_output(self):
        """Disable the output of a signal.

        Return:
            None
        """
        self.com.send("OUTP OFF")
        return

    def enable_digital_pattern(self):
        """Enable the digital pattern signal.

        Rerturn:
            None
        """
        self.com.send("DIG:PATT ON")
        return

    def disable_digital_pattern(self):
        """Disable the digital pattern signal.

        Return:
            None
        """
        self.com.send("DIG:PATT OFF")
        return

    def set_data_pattern_volatile(self, *values):
        """TBD
        """
        str_values = ",".join(map(str, values))
        self.com.send(f"DATA:PATTERN VOLATILE, {str_values}")
        return

    def set_digital_pattern_function(self, func):
        """Set function of the digital pattern signal.

        Args:
            func (str): Function of the digital pattern signal.

        Return:
            None
        """
        self.com.send(f"FUNC:PATT {func}")
        return

    def query_digital_pattern_function(self):
        """Query function of the digital pattern signal.

        Return:
            ret (bytes): Function of the digital pattern signal.
        """
        ret = self.com.query("FUNC:PATT?")
        return ret

    def set_digital_pattern_frequency(self, freq):
        """Set frequency of the digital pattern signal.

        Args:
            freq (float): Value of the frequency.

        Return:
            None
        """
        self.com.send(f"DIG:PATT:FREQ {freq}")
        return

    def query_digital_pattern_frequency(self):
        """Query the frequency of the digital pattern signal.

        Return:
            ret (bytes): Frequency of the digital pattern signal.
        """
        ret = self.com.query("DIG:PATT:FREQ?")
        return ret

    def set_digital_pattern_start_address(self, addr):
        """TBD
        """
        self.com.send(f"DIG:PATT:STAR {addr}")
        return

    def query_digital_pattern_start_address(self):
        """TBD
        """
        ret = self.com.query("DIG:PATT:STAR?")
        return ret

    def set_digital_pattern_stop_address(self, addr):
        """TBD
        """
        self.com.send(f"DIG:PATT:STOP {addr}")
        return

    def query_digital_pattern_stop_address(self):
        """TBD
        """
        ret = self.com.query("DIG:PATT:STOP?")
        return ret

    def enable_digital_pattern_repeat(self):
        """TBD
        """
        self.com.send("DIG:PATT:REP ON")
        return

    def disable_digital_pattern_repeat(self):
        """TBD
        """
        self.com.send("DIG:PATT:REP OFF")
        return

    def query_digital_pattern_repeat(self):
        """TBD
        """
        ret = self.com.query("DIG:PATT:REP?")
        return ret

    def set_digital_pattern_clock_positive(self):
        """TBD
        """
        self.com.send("DIG:PATT:CLOC POS")
        return

    def set_digital_pattern_clock_negative(self):
        """TBD
        """
        self.com.send("DIG:PATT:CLOC NEG")
        return

    def query_digital_pattern_clock(self):
        """TBD
        """
        ret = self.com.query("DIG:PATT:CLOC?")
        return ret

    def set_digital_pattern_trigger_source(self, source):
        """TBD
        """
        self.com.send(f"DIG:PATT:TRIG:SOUR {source}")
        return

    def query_digital_pattern_trigger_source(self):
        """TBD
        """
        ret = self.com.query("DIG:PATT:TRIG:SOUR?")
        return ret

    def set_digital_pattern_trigger_slope_positive(self):
        """TBD
        """
        self.com.send("DIG:PATT:TRIG:SLOP POS")
        return

    def set_digital_pattern_trigger_slope_negative(self):
        """TBD
        """
        self.com.send("DIG:PATT:TRIG:SLOP NEG")
        return

    def query_digital_pattern_trigger_slope(self):
        """TBD
        """
        ret = self.com.query("DIG:PATT:TRIG:SLOP?")
        return ret

    def set_digital_pattern_output_trigger_slope_positive(self):
        """TBD
        """
        self.com.send("DIG:PATT:OUTP:TRIG:SLOP POS")
        return

    def set_digital_pattern_output_trigger_slope_negative(self):
        """TBD
        """
        self.com.send("DIG:PATT:OUTP:TRIG:SLOP NEG")
        return

    def query_digital_pattern_output_trigger_slope(self):
        """TBD
        """
        ret = self.com.query("DIG:PATT:OUTP:TRIG:SLOP?")
        return ret

    def enable_digital_pattern_trigger_output(self):
        """TBD
        """
        self.com.send("DIG:PATT:OUTP:TRIG ON")
        return

    def disable_digital_pattern_trigger_output(self):
        """TBD
        """
        self.com.send("DIG:PATT:OUTP:TRIG OFF")
        return

    def query_digital_pattern_output_trigger(self):
        """TBD
        """
        ret = self.com.query("DIG:PATT:OUTP:TRIG?")
        return ret