from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in roir_ts/__init__.py
from roir_ts import __version__ as version

setup(
	name="roir_ts",
	version=version,
	description="ss",
	author="thirvusoft",
	author_email="thirvusoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
