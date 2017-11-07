"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 30, 2017

@author
"""
from setuptools import setup, find_packages

#: Put your library dependencies here
setup(
    name="enaml-native-maps",
    version="1.0",
    author="jrm",
    author_email="",
    license='MIT',
    url="",
    entry_points={
        'enaml_native_widgets': [
            'enaml-native-maps = googlemaps.widgets.api:install'
        ],
        'enaml_native_android_factories': [
            'enaml-native-maps = googlemaps.android.factories:install'
        ],
    },
    description="enaml-native-maps package for enaml-native",
    packages=find_packages(),
    install_requires=['enaml-native'],
)
