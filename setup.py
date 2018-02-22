#!/usr/bin/env python

from os.path import dirname, join
import helloworld
import os

from setuptools import find_packages, setup

dir = join(dirname(__file__), 'helloworld')

setup (
	author='Ram',
	author_email='ram082.iacr@gmai.com',
	entry_points = {
		'console_scripts': ['helloworld=helloworld:main'],
	},
	install_requires=['boto3', 'awscli'],
	license='MIT',
	name='helloworld',
	packages=find_packages(),
	version=1.0,
)
