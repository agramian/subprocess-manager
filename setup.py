#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(name='subprocess_manager',
      version='0.1.1',
      description='Python Subprocess Manager',
      long_description=read_md('README.md'),
      author='Abtin Gramian',
      author_email='abtin.gramian@gmail.com',
      url='https://github.com/agramian/subprocess-manager',
      packages=['subprocess_manager'],
      download_url = 'https://github.com/agramian/subprocess-manager/tarball/v0.1.1',
      keywords = ['subprocess', 'daemon', 'timeout', 'process', 'spawning', 'non-blocking'],
      classifiers = [],
     )
