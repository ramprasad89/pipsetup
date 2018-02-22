#!/usr/bin/env python
from setuptools import find_packages, setup

setup (
	author='Ram',
	author_email='ram082.iacr@gmai.com',
	entry_points = {
		'console_scripts': ['helloworld=helloworld:main'],
	},
	install_requires=['PyYAML-3.12', 'awscli-1.14.44', 'boto3-1.5.34', 'botocore-1.8.48', 'colorama-0.3.7', 'docutils-0.14', 'helloworld-1.0', 'jmespath-0.9.3', 'pyasn1-0.4.2', 'python-dateutil-2.6.1', 'rsa-3.4.2', 's3transfer-0.1.13', 'six-1.11.0'],
	license='GNU',
	name='helloworld',
	packages=find_packages(),
	version=1.0,
)
