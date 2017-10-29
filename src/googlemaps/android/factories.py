'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 29, 2017

@author: jrm
'''


def map_marker_factory():
    from .android_map_view import AndroidMapMarker
    return AndroidMapMarker


def map_circle_factory():
    from .android_map_view import AndroidMapCircle
    return AndroidMapCircle


def map_polyline_factory():
    from .android_map_view import AndroidMapPolyline
    return AndroidMapPolyline


def map_polygon_factory():
    from .android_map_view import AndroidMapPolygon
    return AndroidMapPolygon


def map_view_factory():
    from .android_map_view import AndroidMapView
    return AndroidMapView


def install():
    from enamlnative.android import factories
    
    factories.ANDROID_FACTOIRES.update({
        'MapMarker': map_marker_factory,
        'MapCircle': map_circle_factory,
        'MapPolyline': map_polyline_factory,
        'MapPolygon': map_polygon_factory,
        'MapView': map_view_factory,
    })