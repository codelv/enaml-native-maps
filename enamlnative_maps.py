"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 30, 2017

@author
"""
from pythonforandroid.recipe import EnamlNativeRecipe


class EnamlNativeMapsRecipe(EnamlNativeRecipe):
    version = '1.0'
    depends = ['enaml-native']
    name = 'enaml-native-maps'
    url = 'src.zip'


def get_recipe():
    return (EnamlNativeMapsRecipe(), __file__)
