# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="maodevice",
    version="0.0.1",
    description="Python 3.7 package to control MAO devices",
    long_description=readme,
    author="Project MAO Contributors",
    author_email="tetsu3191@a.phys.nagoya-u.ac.jp",
    url="https://github.com/mao-wfs/maodevice",
    license=license,
    packages=find_packages(exclude=("docs", "tests")),
    install_requires=["pyserial>=3.4"],
)
