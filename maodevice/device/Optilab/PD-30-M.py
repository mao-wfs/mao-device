# coding: utf-8
class PD_30_M(object):
    manufacturer = 'Optilab'
    product = 'PD-30-M'
    classification = 'O/E Converter'

    def __init__(self, com):
        self.com.set_terminator('\r\n')

    def show_status(self):
        self.com.send('READP')
        ret = self.com.recv()
        return ret
