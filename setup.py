#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Wei Sun"
__copyright__ = "Copyright (C) 2019 GFLoan Co. LTD"
__license__ = "Private"
__version__ = "1.0"

import setuptools

long_description = ""

setuptools.setup(
    name="fill_portrait".replace('_', '.'),
    version="1.0.0",
    author="Sun Wei",
    author_email="sw@gfloan.com",
    description="fill_portrait",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[

    ],
    entry_points={
        'console_scripts': ['fill_portrait=fill_portrait.test_fill_portrait:main']
    }
)
pass