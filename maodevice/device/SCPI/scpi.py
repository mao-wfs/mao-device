# -*- coding: utf-8 -*-
from .. import device


class ScpiCommon(device.Device):
    """Common SCPI commands

    This class is for handling common SCPI commands.

    Attribute:
        _scpi_dict (dict): The dictionary of common SCPI commands.
    """
    def accept_address(self):
        """*AAD: Accept Address Command

        This command, in conjuction with the Address Set protocol, allows the
        controller to detect all address-configurable devices (that is, devices
        that implement this command) and assign an IEEE 488.1 address to each
        of those devices. An address-configurable device is detected when the
        controller has completed a byte-by-byte search of the device's
        identifer, after which time the address is assigned. The Address Set
        protocol causes this identifer search to be executed repeatedly until
        all address-configurable devices have been detected.

        Return:
            None
        """
        self.com.send('*AAD')
        return

    def calibration_query(self):
        """*CAL?: Calibration Query

        The Calibration query causes a device to perform an internal
        self-calibration and generate a response that indicates whether or not
        the device completed the self-calibration without error.

        Return:
            ret (int): Exit status (No-error: 1)
        """
        self.com.send('*CAL?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def clear_status(self):
        """*CLS: Clear Status Command

        The Clear Status command clears status data structures, and forces the
        device to the Operation Complete Command Idle State and the Operation
        Complete Query Idle State.

        Return:
            None
        """
        self.com.send('*CLS')
        return

    def define_device_trigger(self):
        """*DDT: Define Device Trigger Command

        The Define Device Trigger command stores a command sequence that is
        executed when a group execute trigger (GET), IEEE 488.1 interface
        message, or *TRG common command is received. The *RST common command
        shall set the command sequence to a device-defined state.

        Return:
            None
        """
        self.com.send('*DDT')
        return

    def define_device_trigger_query(self):
        """*DDT?: Define Device Trigger Query

        The Define Device Trigger query allows the programmer to examine the
        command sequence which will be executed when a GET or *TRG command is
        received.

        Return:
            ret (str): The query response.
        """
        self.cmd.send('*DDT?')
        ret = self.com.readline()
        ret = ret.strip()
        return ret

    def disable_listener_function(self):
        """*DLF: Disable Listener Function

        The Disable Listener Function command causes a device to cease being a
        listener (change to L0 subset). If this command is the first
        device-specific message received after the device leaves IEEE 488.1
        DCAS state, the device shall cease being a listener within 100 ms after
        the acceptance of the <PROGRAM MESSAGE TERMINATOR>. A subsequent DCL
        message shall restore listener capability. The device shall resume
        listening within 100 ms after entering IEEE 488.1 DCAS state.

        Return:
            None
        """
        self.com.send('*DLF')
        return

    def define_macro(self):
        """*DMC: Define Macro Command

        The Define Macro command allows the programmer to assign a sequence of
        zero or more <PROGRAM MESSAGE UNIT> elements to a macro label.
        The sequence is executed when the label is received as a
        <COMMAND PROGRAM HEADER> or <QUERY PROGRAM HEADER>.

        Return:
            None
        """
        self.com.send('*DMC')
        return

    def enable_macro(self):
        """*EMC: Enable Macro Command

        The Enable Macro command enables and disables expansion of macros.
        Macro definitions are not affected by this command. One use of this
        command is to turn off macro expansion in order to execute a
        device-specific command with the same name as a macro. The *RST command
        disables the expansion of macros.

        Return:
            None
        """
        self.com.send('*EMC')
        return

    def enable_macro_query(self):
        """*EMC?: Enable Macro Query

        The Enable Macro query allows the programmer to query whether the
        macros are enabled. A returned value of zero indicates that macros are
        disabled. A returned value of one indicates that macros are enabled.

        Return:
            ret (int): The query response.
        """
        self.com.send('*EMC?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def standard_event_status_enable(self):
        """*ESE: Standard Event Status Enable Command

        The Standard Event Status Enable command sets the Standard Event Status
        Enable Register bits.

        Return:
            None
        """
        self.com.send('*ESE')
        return

    def enable_macro_query(self):
        """*ESE?: Standard Event Status Enable Query

        The Standard Event Status Enable query allows the programmer to
        determine the current contents of the Standard Event Status Enable
        Register.

        Return:
            ret (int): The query response.
        """
        self.com.send('*ESE?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def standard_event_status_register_query(self):
        """*ESR?: Standard Event Status Register Query

        The Standard Event Status Register query allows the programmer to
        determine the current contents of the Standard Event Status Register.
        Reading the Standard Event Status Register clears it.

        Return:
            ret (int): The query response.
        """
        self.com.send('*ESR?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def get_macro_contents_query(self):
        """*GMC?: Get Macro Contents Query

        The Get Macro Contents query allows the current definition of a macro
        to be retrieved from a device.

        Return:
            ret (str): The query response.
        """
        self.com.send('*GMC?')
        ret = self.com.readline()
        ret = ret.strip()
        return ret

    def identification_query(self):
        """*IDM?: Identification Query

        The intent of the Identification query is for the unique identification
        of devices over the system interface.

        Return:
            ret (str): The query response.
        """
        self.com.send('*IDM?')
        ret = self.com.readline()
        ret = ret.strip().strip(',')
        return ret

    def individual_status_query(self):
        """*IST?: Individual Status Query

        The Individual Status query allows the programmer to read the current
        state of the IEEE 488.1 defined "ist" local message in the device.

        Return:
            ret (int): The query response.
        """
        self.com.send('*IST?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def learn_macro_query(self):
        """*LMC?: Learn Macro Query

        This query returns the currently defined macro labels.

        Return:
            ret (str): The query response.
        """
        self.com.send('*LMC?')
        ret = self.com.readline()
        ret = ret.strip()
        return ret

    def learn_device_setup_query(self):
        """*LRN?: Learn Device Setup Query

        The Learn Device Setup query allows the programmer to obtain a sequence
        of <RESPONSE MESSAGE UNIT> elements that may later be used as
        <PROGRAM MESSAGE UNIT> elements to place the device in the state it was
        in when the *LRN? common query was made.

        Return:
            ret (str): The query response.
        """
        self.com.send('*LRN?')
        ret = self.com.readline()
        ret = ret.strip()
        return ret

    def operation_complete(self):
        """*OPC: Operation Complete Command

        The Operation Complete command causes the device to generate the
        operation complete message in the Standard Event Status Register
        when all pending selected device operations have been finished.

        Return:
            None
        """
        self.com.send('*OPC')
        return

    def operation_complete_query(self):
        """*OPC?: Operation Complete Query

        The Operation Complete query places an ASCII character "1" into the
        device's Output Queue when all pending selected device operations have
        been finished.

        Return:
            ret (int): The query response.
        """
        self.com.send('*OPC?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def option_identification_query(self):
        """*OPT?: Option Identification Query

        The Option Identification query is for identifying reportable device
        options over the system interface.

        Return:
            ret (int): The query response.
        """
        self.com.send('*OPT?')
        ret = self.com.readline()
        ret = ret.strip()
        return ret

    def pass_control_back(self):
        """*PCB: Pass Control Back

        The Pass Control Back command is used by a controller to tell a device,
        being a potential controller, to which address the control is to be
        passed back when the device (acting as a controller) sends the
        IEEE 488.1 interface message, take control (TCT).

        Return:
            None
        """
        self.com.send('*PCB')
        return

    def purge_macros(self):
        """*PMC: Purge Macros Command

        The Purge Macros command causes the device to delete all macros that
        may have been previously defined using the *DMC command. All stored
        macro command sequences and labels shall be removed from the device's
        memory by this command.

        Return:
            None
        """
        self.com.send('*PMC')
        return

    def parallel_poll_enable_register(self):
        """*PRE: Parallel Poll Enable Register Command

        The Parallel Poll Enable Register command sets the Parallel Poll
        Enable Register bits.

        Return:
            None
        """
        self.com.send('*PRE')
        return

    def parallel_poll_enable_register_query(self):
        """*PRE?: Parallel Poll Enable Register Query

        The Parallel Poll Enable Register query allows the programmer to
        determine the current contents of the Parallel Poll Enable Register.

        Return:
            ret (int): The query response.
        """
        self.com.send('*PRE?')
        ret = self.com.readline()
        ret = int(ret)
        return

    def power_on_status_clear_query(self):
        """*PSC?: Power-On Status Clear Query

        The Power-On Status Clear query allows the programmer to query
        the device's power-on-status-clear flag. A returned value of zero
        indicates that the Standard Event Status Enable Register, Service
        Request Enable Register, and the Parallel Poll Enable Register will
        retain their status when power is restored to the device. A returned
        value of one indicates that the registers listed above will be cleared
        when power is restored to the device.

        Return:
            ret (int): The query response.
        """
        self.com.send('*PSC?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def protected_user_data(self):
        """*PUD: Protected User Data Command

        The Protected User Data command stores data unique to the device such
        as calibration date, usage time, environmental conditions, and
        inventory control numbers. A minimum of 63 bytes shall be provided.
        The size of this area shall be specified in the device documentation.

        Return:
            None
        """
        self.com.send('*PUD')
        return

    def protected_user_data_query(self):
        """*PUD?: Protected User Data Query

        The Protected User Data query allows the programmer to retrieve
        the contents of the *PUD storage area. See *PUD command.

        Return:
            ret (str): The query response.
        """
        self.com.send('*PUD?')
        ret = self.com.readline()
        ret = ret.strip()
        return ret

    def recall(self):
        """*RCL: Recall Command

        The *RCL command restores the current settings of a device from a
        copy stored in local memory. The scope of the *RCL command is the
        same as *RST and the *LRN? response. Device documentation shall
        explicitely mention the device settings that are restored by *RCL.

        Return:
            None
        """
        self.com.send('*RCL')
        return

    def resource_description_transfer(self):
        """*RDT: Resource Description Transfer

        The Resource Description Transfer command allows a Resource
        Description to be stored in a device.

        Return:
            None
        """
        self.com.send('*RDT')
        return

    def resource_description_transfer_query(self):
        """*RDT?: Resource Description Transfer Query

        The Resource Description Transfer query allows a Resource Description
        to be retrieved from a device. The Resource Description may be memory
        or in a read-write memory settable by the *RDT command.

        Return:
            ret (str): The query response.
        """
        self.com.send('*RDT?')
        ret = self.readline()
        ret = ret.strip()
        return

    def reset(self):
        """*RST: Reset Command

        Notes:
            - The Reset Command shell do the following:
                1. Except as explicitly exclude below, set the device-specific
                   functions to a known state that is independent of the
                   past-use history of the device. Device-specific commands
                   may be provided to program a different reset state than
                   the original factory-supplied one.
                2. Set the macro defined by *DDT to a device-defined state.
                3. Disable macros.
                4. Force the device into the OCIS state.
                5. Force the device into the OQIS state.

            - The reset command explicityly shall NOT affect the following:
                1. The state of the IEEE 488.1 interface.
                2. The selected IEEE 488.1 address of the device.
                3. The Output Queue.
                4. Any Event Enable Register setting, including the Standard
                   Event Status Enable Register settings.
                5. Any Event Register setting, including the Standard Event
                   Status Register settings.
                6. The power-on-status-clear flag setting.
                7. Macros defined with the Define Macro Contents command.
                8. Calibration data that affects device specifications.
                9. The Protected User Data query response.
                10. The Resource Description Transfer query response.
                11. The Service Request Enable Register setting.
                12. The Parallel Poll Enable Register setting.
                13. The memory register(s) associated with *SAV.

        Return:
            None
        """
        self.com.send('*RST')
        return

    def save(self):
        """*SAV: Save Command

        The *SAV command stores the current settings of the device in local
        memory. The scope of the *SAV command is the same as *RST and the
        *LRN? response. Device documentation shall explicitly mention the
        device settings that are restored by *RCL.

        Return:
            None
        """
        self.com.send('*SAV')
        return

    def service_request_enable(self, bit):
        """*SRE: Service Request Enable Command

        The Service Request Enable command sets the Service Request Enable
        Register bits.

        Argss:
            bit (int): The Service Request Enable Register bits.

        Return:
            None
        """
        self.com.send(f'*SRE {bit}')
        return

    def service_request_enable_query(self):
        """*SRE?: Service Request Enable Query

        The Service Request Enable query allows the programmer to determine
        the current contents of the Service Request Enable Register.

        Return:
            ret (int): The query response.
        """
        self.com.send('*SRE?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def read_status_byte_query(self):
        """*STB?: Read Status Byte Query

        The Read Status Byte query allows the programmer to read the status
        byte and Master Summary Status bit.

        Return:
            ret (int): The query response.
        """
        self.com.send('*STB?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def trigger(self):
        """*TRG: Trigger Command

        The Trigger command is the device-specific analog of the IEEE 488.1
        defined Group Execute Trigger (GET) interface message, and has exactly
        the same effect as a GET when received, parsed, and executed by the
        device.

        Return:
            None
        """
        self.com.send('*TRG')
        return

    def self_test_query(self):
        """*TST?: Self-Test Query

        The self-test query causes an internal self-test and places a response
        into the Output Queue indicating whether or not the device completed
        the self-test without any detected errors. Optionally, information
        on why the self-test was not completed may be contained in the
        response.

        Return:
            ret (int): The query response.
        """
        self.com.send('*TST?')
        ret = self.com.readline()
        ret = int(ret)
        return ret

    def wait_to_continue(self):
        """*WAI: Wait-to-Continue Command

        The Wait-to-Continue command shall prevent the device from executing
        any further commands or queries until the no- operation-pending flag
        is TRUE.

        Return:
            None
        """
        self.com.send('*WAI')
        return

    def remove_individual_macro(self):
        """*RMC: Remove Individual Macro Command

        The Remove Individual Macro command removes a single macro definition
        from the device.

        Return:
            None
        """
        self.com.send('*RMC')
        return

    def save_default_device_settings(self):
        """*SDS: Save Default Device Settings Command

        The Save Default Device Settings command initializes the contents
        of a save/recall register. The register contents are set to a known
        state that is independent of the past use history of the device.

        Return:
            None
        """
        self.com.send('*SDS')
        return

    _scpi_dict = {
        '*AAD': 'accept_address',
        '*CAL?': 'calibration_query',
        '*CLS': 'clear_status',
        '*DDT': 'define_device_trigger',
        '*DDT?': 'define_device_trigger_query',
        '*DLF': 'disable_listener_function',
        '*DMC': 'define_macro',
        '*EMC': 'enable_macro',
        '*EMC?': 'enable_macro_query',
        '*ESE': 'standard_event_status_enable',
        '*ESE?': 'standard_event_status_enable_query',
        '*ESR?': 'standard_event_status_register_query',
        '*GMC?': 'get_macro_contents_query',
        '*IDN?': 'identification_query',
        '*IST?': 'individual_status_query',
        '*LMC?': 'learn_macro_query',
        '*LRN?': 'learn_device_setup_query',
        '*OPC': 'operation_complete',
        '*OPC?': 'operation_complete_query',
        '*OPT?': 'option_identification_query',
        '*PCB': 'pass_control_back',
        '*PMC': 'purge_macros',
        '*PRE': 'parallel_poll_enable_register',
        '*PRE?': 'parallel_poll_enable_register_query',
        '*PSC?': 'power_on_status_clear_query',
        '*PUD': 'protected_user_data',
        '*PUD?': 'protected_user_data_query',
        '*RCL': 'recall',
        '*RDT': 'resource_description_transfer',
        '*RDT': 'resource_description_transfer_query',
        '*RST': 'reset',
        '*SAV': 'save',
        '*SRE': 'service_request_enable',
        '*SRE?': 'service_request_enable_query',
        '*STB?': 'read_status_byte_query',
        '*TRG?': 'trigger',
        '*TST?': 'self_test_query',
        '*WAI': 'wait_to_continue',
        '*RMC': 'remove_individual_macro',
        '*SDS': 'save_default_device_settings',
    }


class ScpiFamily(device.Device):
    """Handle SCPI commands with the appropriate communicator.

    Note:
        If you limit SCPI commands to use, write it as follows before
        instantiation. (Below, when you use only *CLS and *RST.)

        >>> _scpi_enable = '*CLS *RST'

    Attribute:
        _scpi_enable (str): SCPI commands to use. (Delimiter: Space)
    """
    _scpi_enable = 'ALL'

    def __init__(self, com):
        """Initialize 'ScpiFamily'
        
        Args:
            com (Communicator): Communicator to control the device.
        """
        super().__init__(com)
        self._scpi = ScpiCommon(com)
        self._add_scpi_methods()

    def _add_scpi_methods(self):
        """Add methods of SCPI which you use.
        
        Note:
            Thie method is only for the internal use.
            User can add methods by editting '_scpi_enable'.

        Return:
            None
        """
        sdic = self._scpi._scpi_dict
        if self._scpi_enable == 'ALL':
            add = sdic.items()
        else:
            add = [
                [enable, sdic[enable]]
                for enable in self._scpi_enable.split(' ')
            ]
        
        for call, method in add:
            self.__setattr__(
                method,
                self._scpi.__getattribute__(method),
            )
            shortcut = call.replace('*', '').replace('?', 'Q')
            self.__setattr__(shortcut, self.__getattribute__(method))
        return
