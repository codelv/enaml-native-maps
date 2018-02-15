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

    excluded_types = ['.pyc', '.enamlc', '.apk', '.iml', '.zip', '.tar.gz', '.so', '.gif', '.svg']
    excluded_dirs = ['android/build', 'android/captures', 'android/assets']
    for folder in folders:
        if not os.path.isdir(folder):
            k = os.path.join(dest, dirpath)
            matches[k].append(os.path.join(dest,folder))
            continue
        for dirpath, dirnames, files in os.walk(folder):
            #: Skip build folders and exclude hidden dirs
            if ([d for d in dirpath.split("/") if d.startswith(".")] or
                    [excluded_dir for excluded_dir in excluded_dirs if excluded_dir in dirpath]):
                continue
            k = os.path.join(dest, dirpath)
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
    version="1.2",
    author="CodeLV",
    author_email="frmdstryr@gmail.com",
    license='MIT',
    url="https://github.com/codelv/enaml-native-maps",
    description="enaml-native-maps package for enaml-native-cli",
    long_description=open("README.md").read(),
    py_modules=['enaml_native_maps'],
    data_files=find_data_files("enaml-native-maps", 'android', 'ios', 'src'),
    install_requires=['enaml-native>=3.0.0'],
    entry_points={
        'p4a_recipe': [
            'enaml_native_maps = enaml_native_maps:get_recipe'
        ]
    },
)
