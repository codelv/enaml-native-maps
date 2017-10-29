#: ====================================================================
#: Created with 'enaml-native init-package'
#: Modify as needed
#: ====================================================================
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
            'install = googlemaps.widgets.api:install'
        ],
        'enaml_native_android_factories': [
            'install = googlemaps.android.factories:install'
        ],
    },
    description="enaml-native-maps package for enaml-native",
    packages=find_packages(),
    install_requires=['enaml-native'],
)
