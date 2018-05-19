from setuptools import setup, find_packages
import os

version = open("version.txt").read().strip()

setup(name="t4.sql",
      version=version,
      description=("This module provides a simple "
                   "wrapper for SQL within Python."),
      long_description=open("README.rst").read(),
      
      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: SQL",
      ],      
      keywords="Database SQL",
      
      author="Diedrich Vorberg",
      author_email="diedrich@tux4web.de",
      url="https://github.com/dvorberg/t4.sql",
      
      license="GPL",
      
      packages=find_packages(),
      namespace_packages=["t4"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "setuptools",
          # -*- Extra requirements: -*-
      ]
)
