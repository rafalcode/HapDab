#!/usr/bin/env python3

from setuptools import setup, find_packages, Extension
import os
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

import io
import re

def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name = 'hapdab',
    version = find_version('hapdab','__init__.py'),
    packages = find_packages(),
    scripts = [
    ],
    ext_modules = [],
    cmdclass = {
    },

    package_data = {
        '':['*.cyx'],    
        'beagle':'include/beagle/beagle.08Jun17.d8b.jar'
    },
    python_requires='>=3.6',
    setup_requires=[
        'setuptools>=18.0',
    ],
    install_requires = [		
        'minus80>=0.2.0',
        'locuspocus>=0.1.1',
        'scipy>=1.1.0',
        'pandas>=0.23.4',
        'numpy>=1.15.0',
        'pysam>=0.15.0',
        'cassandra-driver>=3.14.0',
        'aiofiles>=0.4.0'
    ],
    include_package_data=True,

    author = 'Rob Schaefer',
    author_email = 'rob@linkage.io',
    description = 'An library for managing and analyzing genotypes and haplotypes',
    license = "Copyright Linkage Analytics 2017. Available under the MIT License",
    url = 'linkage.io'
)
