# coding: utf-8
import math
from .. import device


class OctadS(device.Device):
    """Control 'OCTAD-S'.

    This class control the FPGA-based correlator 'OCTAD-S'.
    This class is based on 'Device'.

    Attributes:
        manufacturer (str): Manufacturer of the device.
        product_name (str): Name of the device.
        classification (str): Classification of the device.
    """
    manufacturer = 'Elecs'
    producct_name = 'OCTAD-S'
    classification = 'Correlator'

    def __init__(self, com):
        """Initialize 'OctadS'.
        
        Args:
            com (Communicator): Communicator to control 'OCTAD-S'

        Example:
            Initialize and start VDIF transmission.

            >>> octad = OctadS(
                    Telnet(host='192.168.1.1', port='5653', timeout=1.),
                )
            >>> octad.start_vdif_transmission()
        """
        super().__init__(com)
        self.com.set_terminator(';')

    def calibrate_demultiplexer(self, n):
        """Calibrate the data transfer from the ADC to the FPGA.

        Notes:
            - Execute this method only when 'show_status' shows 
              'DBBC_module_adc_de-multiplexer_bit-alignment_error'.
            - This method may take up to several minutes to complete.
            - After this method is executed, you must execute 
              'synchronize_with_external'.

        Args:
            n (int): ADC number. (Allowed values: 1, 2)

        Return:
            None
        """
        self.com.send(f'ctl_dmxcal{n}')
        return

    def select_adc_sampling_bit_response(self, n, response=False):
        """Select whether to the bit distribution after sampling with ADC.

        Args:
            n (int): ADC number. (Allowed values: 1, 2)
            response (bool): (Default: False)
                If True, output this data from 'Control Port' to TCP port 60000
                every 1PPS.

        Return:
            None
        """
        __output = 'on' if response else 'off'
        self.com.send(f'sel_dbbcsmpbitreq{n}={__output}')
        return

    def set_control_port_ip(self, ip):
        """Set IP address of 'Control Port'.

        Note:
            You must restart after executing this method.

        Args:
            ip (str): IP address of 'Control Port'.

        Return:
            None
        """
        self.com.send(f'set_ctlip={ip}')
        return

    def set_control_port_subnet_mask(self, mask):
        """Set subnet mask of 'Control Port'.

        Notes:
            - You must restart after executing this method.
            - The subnet mask of the 10G port is the same as this one.

        Args:
            mask (str): Subnet mask of 'Control Port'.

        Return:
            None
        """
        self.com.send(f'set_ctlmask={mask}')
        return

    def select_dbbc_adc(self, n, ch):
        """Select ADC of sampling data source of each channel.

        あとで書く（りかいしてから）
        """
        self.com.send(f'select_dbbc_adc{n}={ch}')
        return

    def select_dbbc_band(self, n, band='USB'):
        """Select DBBC band from USB or LSB.

        Args:
            n (int): DBBC number. (Allowed values: 1, 2, 3, 4)
            band (str): DBBC band. (Default: 'USB')
                (Allowed values: 'USB', 'LSB')

        Return:
            None
        """
        self.com.send(f'sel_dbbcband{n}={band}')
        return

    def select_dbbc_sampling_bit_response(self, n, response=False):
        """Select whether to output the bit distribution after DBBC output.

        Args:
            n (int): DBBC number. (Allowed values: 1, 2, 3, 4)
            response (bool): (Default: False)
                If True, output this data from 'Control Port' to TCP port 60000
                every 1PPS.

        Return:
            None
        """
        __output = 'on' if response else 'off'
        self.com.send(f'sel_dbbcsmpbitreq{n}={__output}')
        return

    def select_filter_band(self, n, band):
        """Select the digital filter's band combination.
        
        Args:
            n (int): DBBC number. (Allowed values: 1, 2, 3, 4)
            あとで書く
        """
        self.com.send(f'sel_filband{n}={band}')
        return

    def select_sampling_date_response(self, response=False):
        """Select whether to output the date to add to sampling data.

        Args:
            response (bool): (Default: False)
                If True, output this date from 'Control Port' to TCP port 60000
            every 1PPS.

        Return:
            None
        """
        __output = 'on' if response else 'off'
        self.com.send(f'sel_smpdatereq{n}={output}')
        return

    def select_sampling_mode(self, mode, rate, bit):
        self.com.send(f'sel_smpmode={mode}:{rate}:{bit}')
        return

    def set_10G_port_ip(sefl, n, ip):
        """Set IP address of '10G port'.

        Note:
            You must restart after executing this method.

        Args:
            n (int): ADC number. (Allowed values: 1, 2)
            ip (str): IP address of 10G port.

        Return:
            None
        """
        self.com.send(f'set_xgip{n}={ip}')
        return

    def set_adc_dynamic_range(self, n, drange, offset=0.):
        """Set dynamic range of ADC.

        Args:
            n (int): ADC number. (Allowed values: 1, 2)
            drange (float): Dynamic range of ADC. (Allowed values: 240.0 - 270.0)
            offset (float): Offset voltage of ADC dynamic range.
                (Allowed values: -128.0 - 128.0)
        """
        if 240.0 <= drange <= 270.0:
            raise ValueError('Set dynamic range 240.0 - 270.0.')
        if -128.0 <= offset <= 128.0:
            raise ValueError('Set offset voltage -128.0 - 128.0.')
        self.com.send(f'set_adc{n}={drange:.1f}:{offset:.1f}')
        return

    def set_dbbc_nco_freq(self, n, nco_freq):
        """Set NCO frequency of the DBBC.

        Note:
            Set NCO frequency in units of 1000Hz. Below 1000Hz is truncated.

        Args:
            n (int): DBBC number. (Allowed values: 1, 2, 3, 4)
            nco_freq (int): NCO frequency of the DBBC.
                (Allowed values: 0 - 16,383,999,000)

        Return:
            None
        """
        if not 0 < nco_freq < 16383999000:
            raise ValueError('Set NCO frequency 0 < nco_freq < 16,383,999,000.')
        self.com.send(f'set_dbbcnco{n}={nco_freq}')
        return

    def set_dbbc_gain(self, n, gain):
        """Set DBBC gain of requantize part.
        
        Note:
            Set DBBC gain in increments of 0.5 dB. 

        Args:
            n (int): DBBC number. (Allowed values: 1, 2, 3, 4)
            gain (float): DBBC gain of requantize part.
                (Allowed vaulues: -40.0 - 40.0)

        Return:
            None
        """
        if not -40.0 < gain < 40.0:
            raise ValueError('Set the gain -40.0 < gain < 40.0.')

        __gain_decimal = math.modf(gain)[0]
        if __gain_decimal != 0.0 and __gain_decimal != 0.5:
            raise ValueError('You must specify DBBC gain in 0.5 increments.')

        self.com.send(f'set_dbbcgain{n}={gain}')
        return

    def set_sampling_date(self, year, doy, hour, minute, second):
        """Set the date to add to sampling data.

        Note:
           You must execute this method after Synchronizing 1PPS with
           'synchronize_with_external'.

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
            f'set_smpdate={year}y{doy}d{hour}h{minute}m{second:.0f}s'
        )
        return

    def set_vdif_ip(self, n, ip):
        """Set IP address of the destination of VDIF.

        Args:
            n (int): DBBC number. (Allowed values: 1, 2, 3, 4)
            ip (str): IP address of the destination of VDIF.

        Return:
            None
        """
        self.com.send(f'set_vdifdes{n}={ip}')
        return

    def set_vdifdesport(self, n, port):
        """Set UDP port number of the destination of VDIF.

        Args:
            n (int): DBBC number. (Allowed values: 1, 2, 3, 4)
            port (int): UDP port number of the destination of VDIF.

        Return:
            None
        """
        self.com.send(f'set_vdifdesport{n}={port}')
        return

    def select_vtp(self, vtp=False):
        """Select ON/OFF of VTP at VDIF transmission.

        Args:
            vtp (bool): If True, VTP is ON. If False, VTP is OFF.

        Return:
            None
        """
        if vtp:
            __vtp == 'vtp'
        else:
            __vtp == 'none'
        self.com.send(f'sel_vdifhead={vtp}')
        return

    def show_alarm(self):
        """Show failures occured now or in the past.

        Return:
            ret (str): Strings indicating occured failures.
        """
        self.com.send('show_alarm?')
        ret = self.com.readline()
        return ret

    def show_status(self):
        """Show malfunctions occured now or in the past.

        Return:
            ret (str): Strings indicating malfunctions.
        """
        self.com.send('show_status?')
        ret = self.com.readline()
        return ret

    def start_vdif_transmission(self, port1='0000', port2='0000'):
        """Set and start VDIF transmission.

        Args:
            port1 (str): 10G port1 threads 1-4.
            port2 (str): 10G port2 threads 1-4.

        Return:
            None

        Example:
            >>> vdif_transmission_start(port1='1111', port2='1111')
        """
        self.com.send(f'ctl_vdiftx=start:{port1}:{port2}')
        return

    def stop_vdif_transmission(self):
        """Stop VDIF transmission.

        Return:
            None
        """
        self.com.send('ctl_vdiftx=stop')
        return

    def synchronize_with_external(self):
        """Synchronize the device to an external synchronization signal.

        Return:
            None
        """
        self.com.send('ctl_sync')
        return
