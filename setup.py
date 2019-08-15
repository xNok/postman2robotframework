#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='postman2robot',
      version='0.0.1',
      description='Generate robotframework libraries based on postman configurations',
      author='xNok',
      author_email='nokwebspace@gmail.com',
      packages=find_packages(exclude=['doc', 'test*']),
      entry_points = {
        'console_scripts': [
            'postman2robot=cli.postman2robot:main'
        ],
      }
     )