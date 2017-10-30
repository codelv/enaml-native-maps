"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 30, 2017

@author
"""
import os
import fnmatch
from setuptools import setup


def find_data_files(dest, *folders):
    matches = {}
    #: Want to install outside the venv volder in the packages folder
    dest = os.path.join('packages', dest)

    excluded_types = ['.pyc', '.enamlc', '*.apk', '*.iml']
    excluded_dirs = ['android/build']
    for folder in folders:
        for dirpath, dirnames, files in os.walk(folder):
            #: Skip build folders and exclude hidden dirs
            if ([d for d in dirpath.split("/") if d.startswith(".")] or
                    [pattern for pattern in excluded_dirs if fnmatch.fnmatch(dirpath,pattern)]):
                continue
            k = os.path.join(dest,dirpath)
            if k not in matches:
                matches[k] = []
            for f in fnmatch.filter(files, '*'):
                if [p for p in excluded_types if f.endswith(p)]:
                    continue
                m = os.path.join(dirpath, f)
                matches[k].append(m)
    return matches.items()


setup(
    name="enaml-native-maps",
    version="1.0",
    author="Jairus Martin",
    author_email="frmdstryr@gmail.com",
    license='MIT',
    url="",
    description="enaml-native-maps package for enaml-native-cli",
    long_description=open("README.md").read(),
    py_modules=['enamlnative_maps'],
    data_files=find_data_files("enaml-native-maps", 'android', 'ios', 'src'),
    install_requires=['enaml-native-cli'],
    entry_points={
        'p4a_recipe': [
            'enaml_native_maps = enamlnative_maps:get_recipe'
        ]
    },
)
