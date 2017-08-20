#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='openworm-model-dashboard',
    # GETTING-STARTED: set your app name:
    version='0.1',
    # GETTING-STARTED: set your app description:
    description='OpenWorm Model Completion Dashboard',
    # GETTING-STARTED: set author name (your name):
    author='OpenWorm',
    # GETTING-STARTED: set author name (your name):
    author_email='info@openworm.org',
    # GETTING-STARTED: set author name (your name):
    url='https://github.com/openworm/model-completion-dashboard',
    # GETTING-STARTED: define required django version:
    install_requires=['Django<=1.8', 'djangorestframework', 'django-webpack-loader'],
)