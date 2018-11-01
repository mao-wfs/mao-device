# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="maodevice",
    version="1.0",
    description="Python 3 package to control MAO devices",
    long_description=readme,
    author="Project MAO Contributors",
    author_email="tueda1207@gmail.com",
    url="https://mao-wfs.github.io/maodevice",
    license=license,
    packages=find_packages(exclude=("docs", "tests")),
    install_requires=["pyserial>=3.4"],
)
