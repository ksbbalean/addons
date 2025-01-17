# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
#from pip.req import parse_requirements
import re, ast

# get version from __version__ variable in addons/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('addons/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

#requirements = parse_requirements("requirements.txt", session="")

setup(
	name='addons',
	version=version,
	description='ERPNext addons app, extra doctypes and customizations',
	author='Ebkar Technology & Management Solutions',
	author_email='info@ebkar.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=("frappe",),
	#dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
