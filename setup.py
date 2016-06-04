#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="python-template",
    version="0.1",
    description="Template of Python Project.",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/python-template.git",
    packages=find_packages(),
    install_requires=[],
    dependency_links=[],
    entry_points={
        "console_scripts": []
    },
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
