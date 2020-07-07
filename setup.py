# This software is available under the terms of the MIT license.
# See the file `LICENSE` in the project directory for the full legal text.

from setuptools import setup, find_packages


setup(
    name                = 'svec',
    version             = '1.1.1',
    description         = 'A simple 2D vector manipulation library for Python, type annotations included',
    author              = 'Alexander Korzun',
    author_email        = 'sahhash33@gmail.com',
    license             = 'MIT',
    packages            = find_packages(),
    install_requires    = [],
    package_data        = {'svec': ['py.typed']},
    tests_require       = ['pytest']
)
