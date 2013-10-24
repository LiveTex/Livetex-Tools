#!/usr/bin/python3

import os
import shutil
import jstuff
from setuptools import setup, find_packages


configPath = '/etc/jstuff'

if not os.path.exists(configPath):
    os.makedirs(configPath)
else:
    shutil.rmtree(configPath)
    os.makedirs(configPath)

shutil.copyfile('./etc/config.json', configPath + os.sep + 'config.json')
shutil.copytree('./etc/templates/', configPath + os.sep + 'templates')


setup(name='jstuff',
      version=jstuff.__version__,
      author='Valeria Lepina',
      author_email='divergence082@gmail.com',
      url='https://github.com/divergence082/Jstuff',
      description='Stuff for generating documentation from JsDocs.',
      long_description=jstuff.__doc__,
      install_requires=["jinja2 >= 2.7.1"],
      package_dir={'Jstuff': 'jstuff'},
      packages=find_packages(),
      entry_points={
          'console_scripts': ['jstuff = jstuff.jstuff:main']
      }
)
