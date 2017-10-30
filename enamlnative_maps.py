"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 30, 2017

@author
"""
import sh
from os.path import join, abspath, exists
from pythonforandroid.recipe import PythonRecipe, current_directory


class EnamlNativeRecipe(PythonRecipe):
    version = '1.0'
    depends = ['enaml-native']
    name = 'enaml-native-maps'
    url = 'src.zip'

    def download(self):
        """ Copy it right from the source """
        #: Zip the srz
        src_root = abspath(join(self.ctx.root_dir, '..', '..', 'venv', 'packages', self.name))
        with current_directory(src_root):
            sh.zip('-r', join(self.ctx.packages_path, self.name, self.url), 'src')


def get_recipe():
    return (EnamlNativeRecipe(), __file__)
