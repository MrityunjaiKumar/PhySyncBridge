#!/usr/bin/python3

from setuptools import setup,find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='phySyncFirmata',
    version='3.0.3',
    description="Use your Arduino as a data acquisition card under Python",
    long_description=long_description,
    author='Mrityunjai Kumar',
    author_email='mrityunjai.kmr@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pyserial','matplotlib','numpy'],
    zip_safe=False,
    url='https://github.com/cedt/PhySyncBridge',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)
