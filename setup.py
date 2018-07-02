# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='maoDevice',
    version='0.1',
    description='Python3.7 package to control MAO devices.',
    url='https://github.com/mao-wfs/mao-device',
    author='Tetsutaro Ueda',
    author_email='tueda1207@gmail.com',
    packages=['maodevice'],
    install_requires=['pyserial>=3.4'],
    classifiers=['Programing Language :: Python :: 3.7'],
)
