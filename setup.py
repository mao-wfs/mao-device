# coding: utf-8
from setuptools import setup

setup(
    name='mao_communicator',
    version='0.0.1',
    description='The package to control devices using MAO',
    long_description='README.md',
    author='Tetsutaro Ueda',
    author_email='tueda1207@gmail.com',
    install_requires=['pyserial==3.4']
    # dependency_links = '',
    url='https://github.com/Scizor-master/mao_communicator',
    license=license,
    # packages=find_packages(exclude=('tests', 'docs')),
    packages=['mao_communicator']
    test_suite='tests',
)
