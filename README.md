Here I'll put some samples and testing with.

The samples:

* WX/wx_gevent.py - A sample about how to use wxPython with gevent. It's GUI
  with a tail -f functionality.  Here I have to create a new class inheriting
  wx.App and override the Mainloop method.

* Go/test_mmap.go - It's a sample about the use of mmap to map an array into a file. The array use here is of type float64 with dimension 100x3.
