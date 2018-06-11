# coding: utf-8
from setuptools import setup

setup(
    name='maoDevice',
    version='0.0.1',
    description='Python3.6 package to control MAO devices.',
    author='Tetsutaro Ueda',
    author_email='tueda1207@gmail.com',
    install_requires=['pyserial>=3.4']
    url='https://github.com/mao-wfs/mao-device',
    # packages=find_packages(exclude=('tests', 'docs')),
    packages=['maodevice']
    test_suite='tests',
)
