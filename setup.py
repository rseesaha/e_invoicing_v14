from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in e_invoicing/__init__.py
from e_invoicing import __version__ as version

setup(
	name="mru_einvoicing",
	version=version,
	description="Mauritius Einvoice - MRA E-Invoicing",
	author="Arylist Technologies",
	author_email="seesaharoopesh@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)