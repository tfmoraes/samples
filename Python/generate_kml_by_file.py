#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This script take as parameter a file with a place by line. A search for each
# place is done using pygeocoder[1]. To each place it generates a markers. The set
# of marker are then saved in kml file using simplekml. This script prints on
# the screen all the places pygeocoder were not able to find.
# [1] - http://code.xster.net/pygeocoder/wiki/Home
# [2] - http://code.google.com/p/simplekml/
import sys
import pygeocoder
import simplekml

from pygeocoder import Geocoder

with open(sys.argv[1]) as f:
    kml = simplekml.Kml()
    for h in f:
        try:
            hname = h.strip().decode('utf8')
            results = Geocoder.geocode(hname)
            kml.newpoint(name=hname, coords=[(results[0].longitude,
                                              results[0].latitude)])
        except pygeocoder.GeocoderError, e:
            print hname

    kml.save(sys.argv[2])
    
