"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 10, 2017

@author
"""
from .map_view import MapView, MapMarker, MapPolygon, MapPolyline, MapCircle


def install():

    from enamlnative.widgets import api

    setattr(api, 'MapView', MapView)
    setattr(api, 'MapMarker', MapMarker)
    setattr(api, 'MapPolygon', MapPolygon)
    setattr(api, 'MapPolyline', MapPolyline)
    setattr(api, 'MapCircle', MapCircle)