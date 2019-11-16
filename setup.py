#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

from pyalgotrade_tushare import __version__


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = parse_requirements('requirements.txt')
test_requirements = requirements
test_requirements.append('pytest')
setup_requirements = requirements

setup(
    name='pyalgotrade_tushare',
    version=__version__,
    description="pyalgotrade tushare module",
    long_description=readme + '\n\n',
    author="bopo.wang",
    author_email='ibopo@126.com',
    url='https://github.com/bopo/pyalgotrade_tushare',
    packages=find_packages(include=['pyalgotrade_tushare','pyalgotrade_tushare.*']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pyalgotrade_tushare',
    entry_points={
        'console_scripts': [
            'pyalgotrade_tushare = pyalgotrade_tushare.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
