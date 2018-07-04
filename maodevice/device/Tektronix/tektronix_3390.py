# -*- coding: utf-8 -*-
from ..SCPI import scpi


class Tektronix3390(scpi.ScpiFamily):
    """Control '3390'

    This class control the Function Generator '3390'.
    This class is based on 'ScpiFamily'.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = 'Tektronix'
    product_name = '3390'
    classification = 'Function Generator'
    _scpi_enable = '*CLS *ESE *ESE? *ESR? *IDN? *LRN? *OPC *OPC? *PSC? *RCL' +\
                   '*RST *SAV *SRE *SRE? *STB? *TRG *TST? *WAI'

    def set_function(self, func):
        """Set function of the signal.

        Args:
            func (str): Function of the signal.

        Return:
            None
        """
        self.com.send(f'FUNC {func}')
        return

    def query_function(self):
        """Query the function of the signal.

        Return:
            ret (str): Function of the signal.
        """
        ret = self.com.query('FUNC?')
        return ret

    def set_frequency(self, freq, unit='Hz'):
        """Set frequency of the signal.

        Args:
            freq (float): Value of the frequency.

        Return:
            None
        """
        _unit_converter = {
            'uHz': 10 ** -6,
            'mHz': 10 ** -3,
            'Hz': 1,
            'kHz': 10 ** 3,
            'MHz': 10 ** 6,
        }
        self.com.send(f'FREQ {freq * _unit_converter[unit]:.10f}')
        return

    def query_frequency(self):
        """Query frequency of the signal.

        Return:
            ret (float): The frequency value in Hz.
        """
        ret = self.com.query('FREQ?')
        return ret

    def set_voltage(self, volt, unit='dBm'):
        """Set voltage of the signal.

        Args:
            volt (float): An voltage value.
            unit (str): An unit of the voltage. (Default: 'dBm')

        Return:
            None
        """
        self.com.send(f'VOLT {volt:.10f}')
        self.com.send(f'VOLT:UNIT {unit}')
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
        self.com.send(f'VOLT:OFFS {v_off:.10f}')
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
        self.com.send(f'VOLT:HIGH {v_hi:.10f}')
        self.com.send(f'VOLT:LOW {v_low:.10f}')
        return

    def query_pulse_high_low_levels(self):
        """Query pulse high and low levels.

        Return:
            ret (dict): Dictionary of Pulse high and low levels.
        """
        self.com.send('VOLT:HIGH?')
        __v_hi = self.com.readline()
        self.com.send('VOLT:LOW?')
        __v_low = self.com.readline()
        ret = {'HIGH': float(__v_hi), 'LOW': float(__v_low)}
        return ret

    def set_waveform_polarity(self, invert=False):
        """Set waveform polarity.

        Args:
            invert (bool): If True, waveform polarity is specified inverted.

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

    def set_termination(self, termination):
        """aaa
        """
