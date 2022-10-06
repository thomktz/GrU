from setuptools import setup, find_packages
import os


setup(name='GrU',
      version='0.1.0',
      description='Graph Utils for Python',
      author='Thomas Kientz',
      author_email='thomas@kientz.net',
      # install_requires=required,
      packages=['GrU'],
      package_dir={'': 'src'},
     )