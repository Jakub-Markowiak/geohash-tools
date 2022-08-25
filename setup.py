try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup, find_packages

setup(
    include_package_data=True,
    name='geohash_tools',
    version='0.1.1',
    license='MIT',
    description='Geohash tools for performing geohash related tasks.',
    url="https://github.com/Jakub-Markowiak/geohash-tools",
    download_url="https://github.com/Jakub-Markowiak/geohash-tools/archive/refs/tags/v0.1.tar.gz",
    author='Jakub Markowiak',
    author_email='jamarkowiak@gmail.com',
    packages=find_packages(),
    long_description='This module provides optimized functions to perform geohash related tasks. Module includes encoding and decoding geohashes, finding neighbouring geohashes and calculating exact distance between two geohashes using haversine formula',
    long_description_content_type="text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords=['geohash', 'gis', 'location', 'distance', 'cryptography']
)