# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.org') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='hgl',
    version='0.1.0',
    description='Simple helper library for testing out opengl code',
    long_description=readme,
    author='Oliver Marks',
    author_email='oly@digitaloctave.com',
    url='https://github.com/olymk2/hgl',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

