Here I'll put some samples and tests.

The samples:

* WX/wx_gevent.py - A sample about how to use wxPython with gevent. It's GUI
  with a tail -f functionality.  Here I have to create a new class inheriting
  wx.App and override the Mainloop method.

* Go/test_mmap.go - It's a sample about the use of mmap to map an array into a file. The array use here is of type float64 with dimension 100x3.

* Python/generate_kml_by_file.py - Given a file with one place for line, it searches each place on google maps using [pygeocoder](http://code.xster.net/pygeocoder/wiki/Home) and creates and a marker. The set of generated markers are then saved on a kml file using [simplekml](http://code.google.com/p/simplekml/).

* Python/plotting.py - So far, there are two functions to ease the plotting of a set of vectors (2D and 3D).

* Qt/qt_draw_np_array.py - It show how use Qt5 (PySide) to draw in a numpy array.
