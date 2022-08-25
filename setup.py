try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup, find_packages

setup(
    include_package_data=True,
    name='Geohash tools',
    version='0.1',
    license='MIT',
    description='Geohash tools for performing geohash related tasks.',
    url="https://github.com/Jakub-Markowiak/geohash-tools",
    author='Jakub Markowiak',
    author_email='jamarkowiak@gmail.com',
    packages=find_packages(),
    install_requires=['math', 'sys', 'unittest'],
    long_description='This module provides optimized functions to perform geohash related tasks. Module includes encoding and decoding geohashes, finding neighbouring geohashes and calculating exact distance between two geohashes using haversine formula',
    long_description_content_type="text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords=['geohash', 'gis', 'location', 'distance', 'cryptography']
)