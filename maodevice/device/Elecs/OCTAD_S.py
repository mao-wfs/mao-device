# -*- coding: utf-8 -*-
from ..device import Device
from ... import utils


class OctadS(Device):
    """Control 'OCTAD-S'.

    This class control the FPGA-based correlator 'OCTAD-S'.
    This class is based on 'Device'.

    Args:
        com: Communicator instance to control the device.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = 'Elecs'
    product_name = 'OCTAD-S'
    classification = 'Correlator'

    CORRELATION_MODE = {
        'AUTO1': 0x01,
        'AUTO2': 0x02,
        'CROSS1-2': 0x10,
    }

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator(';')

    def restart(self):
        """Restart the device.

        Return:
            None
        """
        self.com.send('reset=system')
        return

    def set_control_port_ip(self, ip):
        """Set IP address of the control port.

        Note:
            You must restart after executing this method.

        Args:
            ip (str): IP address of the control port.

        Return:
            None
        """
        self.com.send(f'set_ctlip={ip}')
        return

    def set_control_port_subnet_mask(self, mask):
        """Set subnet mask of the control port.

        Notes:
            - You must restart after executing this method.
            - The subnet mask of the 10G port is the same as this one.

        Args:
            mask (str): Subnet mask of the control port.

        Return:
            None
        """
        self.com.send(f'set_ctlmask={mask}')
        return

    def set_gigabit_ethernet_ip(self, ip):
        """Set IP address of the Gigabit Ethernet.

        Note:
            You must restart after executing this method.

        Args:
            ip (str): IP address of the Gigabit ethernet.

        Return:
            None
        """
        self.com.send(f'set_gbeip={ip}')
        return

    def calibrate_de_multiplexer(self, n):
        """Calibrate the data transfer from the ADC to the FPGA.

        Notes:
            - Execute this method only when 'show_status' shows
              'DBBC_module_adc_de-multiplexer_bit-alignment_error'.
            - This method may take up to several minutes to complete.
            - You must execute 'synchronize_with_external'
              after executing this method.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.

        Return:
            None
        """
        self.com.send(f'ctl_dmxcal{n}')
        return

    @utils.filter('d_range', 240., 270., 0.1)
    @utils.filter('offset', -128., 128., 0.1)
    def set_adc_dynamic_range(self, n, d_range=256., offset=0.0):
        """Set dynamic range of ADC.

        Note:
            Do not change the dynamic range as much as possible.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.
            d_range (float): Dynamic range of ADC.
                Set within the range of 240.0 - 270.0.
                Defaults to 256.
            offset (float): Offset voltage of ADC dynamic range.
                Set within the range of -128.0 - 128.0.
                Defaults to 0.0.

        Return:
            None
        """
        self.com.send(f'set_adc{n}={d_range:.1f}:{offset:.1f}')
        return

    def set_date(self, year, doy, hour, minute, second):
        """Set the date to add to sampling data.

        Notes:
            - You must execute this method after the method
              'synchronize_with_external'.
            - You do not need to execute this method
              if you use a NTP server.

        Args:
            year (int): Year.
            doy (int): Day of the year.
            hour (int): Hour.
            minute (int): Minute.
            second (int): Second.

        Return
            None
        """
        self.com.send(
            f'set_smpdate={year}y{doy}d{hour}h{minute}m{second:.0f}s'
        )
        return

    def synchronize_with_external(self):
        """Synchronize the device to an external synchronization signal.

        Return:
            None
        """
        self.com.send('ctl_sync')
        return

    def set_vdif_destination_ip(self, n, ip):
        """Set the destination IP address of VDIF.

        Note:
            The mean of thread ID are as follows.

            1. Autocorrelation of channel 1
            2. Autocorrelation of channel 2
            5. Cross-correlation of channels 1 and 2

        Args:
            n (int): Thread ID.
                Allowed values are 1, 2 or 5.
            ip (str): Destination IP address of VDIF.

        Return:
            None
        """
        self.com.send(f'set_vdifdes{n}={ip}')
        return

    def set_vdif_destination_port(self, n, port):
        """Set the destination UDP port of VDIF.

        Note:
            The mean of thread ID are as follows.

            1. Autocorrelation of channel 1
            2. Autocorrelation of channel 2
            5. Cross-correlation of channels 1 and 2

        Args:
            n (int): Thread ID.
                Allowed values are 1, 2 or 5.
            port (int): Destination UDP port of VDIF.

        Return:
            None
        """
        self.com.send(f'set_vdifdesport{n}={port}')
        return

    def set_ntp_ip(self, ip):
        """Set IP address of a NTP server.

        Notes:
            - You must restart or execute 'synchronize_with_external'
              after execution of this method.
            - You set the IP address '0.0.0.0' to disable
              the SNTP function.

        Args:
            ip (str): IP address of a NTP server.

        Return:
            None
        """
        self.com.send(f'set_ntv={ip}')
        return

    def set_window_function(self, win_func='none'):
        """Set the window function of FFT.

        Note:
            You can choose window functions as follows.

            - None
            - Hamming
            - Hanning
            - Blackman

        Args:
            win_func (str): Window function of FFT.
                Select one of 'none', 'hamming' 'hanning' or 'blackman'.

        Return:
            None
        """
        self.com.send(f'set_window={win_func}')
        return

    @utils.filter('scale', 0, 31, 1)
    def select_x_scaling(self, n, scale=0):
        """Set scaling of X part.

        Args:
            n (int): Thread ID.
                Allowed values are 1, 2 or 5.
            scale (int): Scaling of X part.
                Set within the range of 0 - 31.
                Defaults to 0.

        Return:
            None
        """
        self.com.send(f'set_scaling{n}={scale}')
        return

    @utils.filter('scale', 0, 31, 1)
    def select_f_scaling(self, n, scale=0):
        """Set scaling of F part.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.
            scale (int): Scaling of X part.
                Set within the range of 0 - 31.
                Defaults to 0.

        Return:
            None
        """
        self.com.send(f'set_requantization{n}={scale}')
        return

    def select_integration_time(self, integ_time=5):
        """Select integration time.

        Args:
            integ_time (int): Integration time.
                Allowed values are 5 or 10 (msec).
                Defaults to 0.

        Return:
            none
        """
        self.com.send(f'set_iplen={integ_time}')
        return

    @utils.filter('mask_time', 0, 2000, 1)
    def set_mask_time_of_integration(self, mask_time=0):
        """Set the time to mask integration.

        Note:
            You set this time by FFT segment unit.
            (e.g. 2000 FFT segment is 2 ms)

        Args:
            mask_time (int): Time to mask integration.
                You must set within the range of 0 - 2000.
        """
        self.com.send(f'set_ipmask={mask_time}')
        return

    @utils.filter('offset', 0, 32767,  1)
    def set_adc_delay_offset(self, n, offset=16384):
        """Set the delay offset of ADC.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.
            offset (int): Delay offset of ADC.
                You must set within the range of 0 - 32767.
                Defaults to 16384.
        """
        self.com.send(f'set_dlyoffset{n}={offset}')
        return

    def start_correlation(self, time, *mode):
        """Start correlation.
        """
        pass

    def stop_correlation(self, time):
        """Stop correlation.
        """
        pass

    def select_repeat_response(self, response=False):
        """Select whether to output the repeat message.

        Args:
            response (bool): Response indicator.
                If it is true, output the repeat message.

        Return:
            None
        """
        _output = 'on' if response else 'off'
        self.com.send(f'set_ipreq={_output}')
        return

    @utils.decoder
    def show_alarm(self):
        """Show failures occured now or in the past.

        Note:
            Since it is READ & CLEAR, alarms that occured in the past
            are displayed only once. Regarding the current ongoing
            alram, no matter how many times this command is issued,
            the alarm will be displayed.

        Return:
            ret (:obj:`list` of :obj:`bytes`): Alarms strings.
        """
        ret = self.com.query('show_alarm?')
        return ret

    @utils.decoder
    def show_status(self):
        """Show malfunctions occured now or in the past.

        Note:
            Since it is READ & CLEAR, alarms that occured in the past
            are displayed only once. Regarding the current ongoing
            alram, no matter how many times this command is issued,
            the alarm will be displayed.

        Return:
            ret (:obj:`list` of :obj:`bytes`): Status strings.
        """
        ret = self.com.query('show_status?')
        return ret

    def show_adc_sampling_bit(self, n):
        """Show the bit distribution after sampling with ADC.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.

        Return:
            ret (:obj:'list' of :obj:`bytes`): Bit distribution.
        """
        ret = self.com.query(f'show_adcsmpbit{n}?')
        return ret

    def show_1pps_gap(self):
        """Show the gap between internal 1PPS and external one.

        Return:
            ret (:obj:'list' of :obj:`bytes`): The 1PPS gap (ns).
        """
        ret = self.com.query('show_1ppsgap?')
        return ret

    def show_temperature(self):
        """Show FPGA junction temperature.

        Return:
            ret (:obj:'list' of :obj:`bytes`): FPGA junction temperature.
        """
        ret = self.com.query('show_temp?')
        return ret

    def show_fpga_power(self, n):
        """Show the power supply voltage measured by FPGA.

        Args:
            n (int): Module number.
                If n = 1 to 4, it corresponds to DSP module <n>, and
                when n = 5 it corresponds to Output module.
                Allowed values are 1, 2, 3, 4 or 5.

        Return:
            ret (:obj:'list' of :obj:`bytes`): Power supply voltage.
        """
        ret = self.com.query(f'show_fpga_power{n}?')
        return ret

    def show_system(self):
        """Show various information of 'OCTAD-S'.

        Return:
            ret (:obj:'list' of :obj:`bytes`): Information of 'OCTAD-S'.
        """
        ret = self.com.query('show_status?')
        return ret
