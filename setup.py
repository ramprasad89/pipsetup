#!/usr/bin/env python

import helloworld
from setuptools import find_packages, setup

setup (
	author='Ram',
	author_email='ram082.iacr@gmai.com',
	entry_points = {
		'console_scripts': ['helloworld=helloworld.helloworld:main'],
	},
	install_requires=['boto3', 'awscli'],
	license='GNU',
	name='helloworld',
	description='hello world python script for testing python packaging',
	url='https://github.com/ramprasad89/pipsetup',
	packages=find_packages(),
	version=1.0,
	project_urls={
		'Reference-repo': 'https://github.com/pypa/sampleproject',
		'Reference-web': 'https://packaging.python.org/tutorials/distributing-packages/',
	},
)
