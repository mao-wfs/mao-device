# -*- coding: utf-8 -*-
from maodevice.core import BaseDeviceHandler
from maodevice.validators import OctadSValidator


class OctadS(BaseDeviceHandler, metaclass=OctadSValidator):
    """Control "OCTAD-S".

    The OCTAD-S is the FPGA-based correlator.

    Note:
        This class is based on "maodevice.core.BaseDeviceHandler".

    Args:
        com (maodevice.communicator):
            Communicator instance to control the device.

    Attributes:
        MANUFACTURER (str): Manufacturer of the device.
        PRODUCT_NAME (str): Name of the device.
        CLASSIFICATION (str): Classification of the device.
    """
    MANUFACTURER = "Elecs"
    PRODUCT_NAME = "OCTAD-S"
    CLASSFICATION = "Correlator"

    CORRELATION_MODE = {
        "Auto1":    0x01,
        "Auto2":    0x02,
        "Cross1-2": 0x10,
    }

    def __init__(self, com):
        super().__init__(com)
        self.com.set_terminator(";")

    def calibrate_de_multiplexer(self, n):
        """Calibrate the data transfer from the ADC to the FPGA.

        Notes:
            - Execute this method only when "show_status" shows
              "DBBC_module_adc_de-multiplexer_bit-alignment_error".
            - This method may take up to several minutes to complete.
            - You must execute "synchronize_with_external"
              after executing this method.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.

        Return:
            None
        """
        self.com.send(f"ctl_dmxcal{n}")
        return

    def restart(self):
        """Restart "OCTAD-S".

        Return:
            None
        """
        self.com.send("reset=system")
        return

    def select_correlation_scaling(self, n, scale=0):
        """Set scaling of X (Correlation) part.

        Note:
            The mean of thread ID are as follows.
            1. Auto-correlation of channel 1
            2. Auto-correlation of channel 2
            5. Cross-correlation of channels 1 and 2

        Args:
            n (int): Thread ID.
                Allowed values are 1, 2 or 5.
            scale (int): Scaling of X (Correlation) part.
                Set within the range of 0 - 31.
                Defaults to 0.

        Return:
            None
        """
        self.com.send(f"set_scaling{n}={scale}")
        return

    def select_integration_time(self, integ_time=5):
        """Select integration time.

        Args:
            integ_time (int): Integration time.
                Allowed values are 5 or 10 (msec).
                Defaults to 5.

        Return:
            None
        """
        self.com.send(f"set_iplen={integ_time}")
        return

    def select_repeat_response(self, is_repeat=False):
        """Select whether to output the repeat message.

        Args:
            is_repeat (bool): Response indicator.
                If it is true, output the repeat message.

        Return:
            None
        """
        is_output = "on" if is_repeat else "off"
        self.com.send(f"set_ipreq={is_output}")
        return

    def select_requantization_scaling(self, n, scale=0):
        """Set scaling of Y (Requantization) part.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.
            scale (int): Scaling of Y (Requantization) part.
                Set within the range of 0 - 31.
                Defaults to 0.

        Return:
            None
        """
        self.com.send(f"set_requantization{n}={scale}")
        return

    def set_adc_delay_offset(self, n, offset=16384):
        """Set the delay offset of ADC.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.
            offset (int): Delay offset of ADC.
                You must set within the range of 0 - 32767.
                Defaults to 16384.

        Return:
            None
        """
        self.com.send(f"set_dlyoffset{n}={offset}")
        return

    def set_adc_dynamic_range(self, n, d_range=256., offset=0.):
        """Set dynamic range of ADC.

        Note:
            Do not change the dynamic range as much as possible.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.
            d_range (float): Dynamic range of ADC.
                Set within the range of 240.0 - 270.0.
                Defaults to 256.0.
            offset (float): Offset voltage of ADC dynamic range.
                Set within the range of -128.0 - 128.0.
                Defaults to 0.0.

        Return:
            None
        """
        self.com.send(f"set_adc{n}={d_range}:{offset}")
        return

    def set_control_port_ip(self, ip):
        """Set IP address of the control port.

        Note:
            You must restart after executing thie method.

        Args:
            ip (str): IP address of the control port.

        Return:
            None
        """
        self.com.send(f"set_ctlip={ip}")
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
        self.com.send(f"set_ctlmask={mask}")
        return

    def set_date(self, year, doy, hour, minute, second):
        """Set the date to add to sampling data.

        Notes:
            - You must execute this method after the method
              "synchronize_with_external".
            - You do not need to execute this method
              if you use a NTP server.

        Args:
            year (int): Year.
            doy (int): Day of the year.
            hour (int): Hour.
            minute (int): Minute.
            second (int): Second.

        Return:
            None
        """
        self.com.send(
            f"set_smpdate={year}y{doy}d{hour}h{minute}m{second:.0f}s"
        )
        return

    def set_gigabit_ethernet_ip(self, ip):
        """Set IP address of the Gigabit ethernet.

        Note:
            You must restart after executing this method.

        Args:
            ip (str): IP address of the Gigabit ethernet.

        Return:
            None
        """
        self.com.send(f"set_gbeip={ip}")
        return

    def set_mask_time_of_integration(self, mask_time=0):
        """Set the time to mask integration.

        Note:
            You set this time by FFT segment unit.
            (e.g. 2000 FFT segment is 2 ms)

        Args:
            mask_time (int): Time to mask integration.
                You must set within the range of 0 - 2000.

        Return:
            None
        """
        self.com.send(f"set_ipmask={mask_time}")
        return

    def set_ntp_ip(self, ip):
        """Set IP address of a NTP server.

        Notes:
            - You must restart or execute "synchronize_with_external"
              after execution of this method.
            - You set the IP address "0.0.0.0" to disable the SNTP function.

        Args:
            ip (str): IP address of a NTP server.

        Return:
            None
        """
        self.com.send(f"set_ntp={ip}")
        return

    def set_vdif_destination_ip(self, n, ip):
        """Set the destination IP address of VDIF.

        Note:
            The mean of thread ID are as follows.
            1. Auto-correlation of channel 1
            2. Auto-correlation of channel 2
            5. Cross-correlation of channels 1 and 2

        Args:
            n (int): Thread ID.
                Allowed values are 1, 2 or 5.
            ip (str): Destination IP address of VDIF.

        Return:
            None
        """
        self.com.send(f"set_vdifdes{n}={ip}")
        return

    def set_vdif_destination_port(self, n, port):
        """Set the destination UDP port of VDIF.

        Note:
            The mean of thread ID are as follows.
            1. Auto-correlation of channel 1
            2. Auto-correlation of channel 2
            5. Cross-correlation of channels 1 and 2

        Args:
            n (int): Thread ID.
                Allowed values are 1, 2 or 5.
            port (int): Destination UDP port of VDIF.

        Return:
            None
        """
        self.com.send(f"set_vdifdesport{n}={port}")
        return

    def set_window_function(self, win_func="none"):
        """Set the window function of FFT.

        Note:
            You can choose window functions as follows.
            - None
            - Hamming
            - Hanning
            - Blackman

        Args:
            win_func (str): Window function of FFT.
                Select one of "nont", "hamming", "hanning" or "blackman".
                Defaults to "none".

        Return:
            None
        """
        self.com.send(f"set_window={win_func}")
        return

    def show_1pps_gap(self):
        """Show the gap between internal 1PPS and external one.

        Return:
            ret (bytes): The 1PPS gap (ns).
        """
        ret = self.com.query("show_1ppsgap?")
        return ret

    def show_adc_sampling_bit(self, n):
        """Show the bit distribution after sampling with ADC.

        Args:
            n (int): ADC number.
                Allowed values are 1 or 2.

        Return:
            ret (bytes): Bit distribution.
        """
        ret = self.com.query(f"show_adcsmpbit{n}?")
        return ret

    def show_fpga_power(self, n):
        """Show the power supply voltage measured by FPGA.

        Args:
            n (int): Module number.
                If n = 1 to 4, it corresponds to DSP module <n>, and
                when n = 5 it corresponds to output module.
                Allowed values are 1, 2, 3, 4 or 5.

        Return:
            ret (bytes): Power supply voltage.
        """
        ret = self.com.query(f"show_fpga_power{n}?")
        return ret

    def show_status(self):
        """Show malfunctions occured now or in the past.

        Note:
            Since it is READ & CLEAR, alarms that occured in the past
            are displayed only once. Regarding the current ongoing
            alram, no matter how many times this command is issued,
            the alarm will be displayed.

        Return:
            ret (bytes): Status string.
        """
        ret = self.com.query("show_status?")
        return ret

    def show_system(self):
        """Show various information of "OCTAD-S".

        Return:
            ret (bytes): Information of "OCTAD-S".
        """
        ret = self.com.query("show_system?")
        return ret

    def show_temperature(self):
        """Show FPGA junction temperature.

        Return:
            ret (bytes): FPGA junction temperature.
        """
        ret = self.com.query("show_temp?")
        return ret

    def start_correlation(self, time, *mode):
        """Start correlation.
        """
        pass

    def stop_correlation(self, time):
        """Stop correlation.
        """
        pass

    def synchronize_with_external(self):
        """Synchronize the device to an external synchronization signal.

        Return:
            None
        """
        self.com.send("ctl_sync")
        return