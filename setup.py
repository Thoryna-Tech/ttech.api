#!/usr/bin/env python

import sys, os
from setuptools import setup, find_packages

setup(
        name = "ttech.api",
        version = "0.3",
        description = "Python API bindings for both utilizing and hosting the secure RPC mechanism.",
        author = "Thoryna Valays",
        author_email = "info@thorynatech.info",
        license = "CLP",
        
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        namespace_packages = ['ttechapi'],
        
        tests_require = ['nose', 'webtest', 'coverage'],
        test_suite = 'nose.collector',
        
        install_requires = [
                'WebOb',
                'marrow.util',
                'ecdsa',
                'futures'
            ],
        
    )
