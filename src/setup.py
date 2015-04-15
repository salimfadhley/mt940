#! /usr/bin/env python
from setuptools import setup
import os

SRC_DIR, _ = os.path.split(__file__)
PROJECT_ROOT, _ = os.path.split(SRC_DIR)
REVISION = '0.0.2'
PROJECT_NAME = 'mt940parser'
PROJECT_AUTHORS = "Salim Fadhley"
PROJECT_EMAILS = 'salimfadhley@gmail.com'
PROJECT_URL = "https://github.com/salimfadhley/mt940"
SHORT_DESCRIPTION = 'MT940 / MT942 message parser implemented as a context-free grammar in PLY.'

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, "readme.md")).read()
except IOError:
    DESCRIPTION = SHORT_DESCRIPTION

setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    packages=['mt940', 'mt940_tests'],
    zip_safe=True,
    include_package_data=False,
    install_requires=['ply'],
    test_suite='nose.collector',
    tests_require=['mock', 'nose', 'coverage'],
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
        ],
)
