try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup, find_packages

_VERSION = '0.3.0'
with open("README.md", 'r') as f:
    _long_description = f.read()

setup(
    include_package_data=True,
    name='geohash_tools',
    version=_VERSION,
    license='MIT',
    description='Geohash tools for performing geohash related tasks.',
    url="https://github.com/Jakub-Markowiak/geohash-tools",
    download_url=f"https://github.com/Jakub-Markowiak/geohash-tools/archive/refs/tags/v{_VERSION}.tar.gz",
    author='Jakub Markowiak',
    author_email='jamarkowiak@gmail.com',
    packages=find_packages(),
    long_description=_long_description,
    long_description_content_type="text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords=['geohash', 'gis', 'location', 'distance', 'cryptography']
)