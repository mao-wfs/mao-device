#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


MAJOR = 1
MINOR = 0
VERSION = f"{MAJOR}.{MINOR}"
CLASSIFIERS = [
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: MIT License",
]
REQUIREMENTS = [
    "pyserial>=3.4",
]


try:
    with open("README.md") as f:
        readme = f.read()
except IOError:
    readme = ""


setup(
    name="maodevice",
    url="https://github.com/mao-wfs/maodevice",
    version=VERSION,
    author="Project MAO Contributors",
    author_email="tueda1207@gmail.com",
    description="Python 3 package to control MAO devices",
    long_description=readme,
    license="MIT",
    packages=find_packages(exclude=("docs", "tests")),
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
)