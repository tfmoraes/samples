import sys
import pygeocoder
import simplekml

from pygeocoder import Geocoder

with open(sys.argv[1]) as f:
    non_ok = []
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
    
