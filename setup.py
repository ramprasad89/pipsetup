#!/usr/bin/env python

import helloworld
from setuptools import find_packages, setup

setup (
	author='Ram',
	author_email='ram082.iacr@gmai.com',
	entry_points = {
		'console_scripts': ['helloworld=helloworld.helloworld:test'],
	},
	install_requires=['boto3', 'awscli'],
	license='GNU',
	name='helloworld',
	packages=find_packages(),
	version=1.0,
)
