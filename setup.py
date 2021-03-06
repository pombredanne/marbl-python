#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as f:
    readme = f.read()


install_requires = [
    'msgpack-python >=0.4.2, <1.0.0',
    'numpy >=1.8.1, <2.0.0'
]
tests_require = [
    'pytest',
    'coverage'
]


setup(
    name="marbl-python",
    version='2.0.3',
    description=('A Python implementation of the Marbl specification for '
                 'normalized representations of Markov blankets in Bayesian '
                 'networks.'),
    author='Will Mayner',
    author_email='wmayner@gmail.com',
    long_description=readme,
    url="https://github.com/wmayner/marbl-python",
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    py_modules=['marbl'],
    package_data={'': ['LICENSE']},
    license='GNU General Public License v3.0',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
    ]
)
