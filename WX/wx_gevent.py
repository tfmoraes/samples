import sys
import wx
import gevent

class MyApp(wx.App):
    def MainLoop(self):
        # Create an event loop and make it active.  If you are
        # only going to temporarily have a nested event loop then
        # you should get a reference to the old one and set it as
        # the active event loop when you are done with this one...
        evtloop = wx.EventLoop()
        old = wx.EventLoop.GetActive()
        wx.EventLoop.SetActive(evtloop)

        # This outer loop determines when to exit the application,
        # for this example we let the main frame reset this flag
        # when it closes.
        while self.keepGoing:
            # At this point in the outer loop you could do
            # whatever you implemented your own MainLoop for.  It
            # should be quick and non-blocking, otherwise your GUI
            # will freeze.  
            # This inner loop will process any GUI events
            # until there are no more waiting.
            while evtloop.Pending():
                evtloop.Dispatch()

            # Send idle events to idle handlers.  You may want to
            # throttle this back a bit somehow so there is not too
            # much CPU time spent in the idle handlers.  For this
            # example, I'll just snooze a little...
            gevent.sleep()
            self.ProcessIdle()
        wx.EventLoop.SetActive(old)

    def OnInit(self):
        #frame = MyFrame(None, -1, "This is a test")
        #frame.Show(True)
        #self.SetTopWindow(frame)

        self.keepGoing = True
        return True


class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Gevent")
        self._do_interface()

    def _do_interface(self):
        self.editor = wx.TextCtrl(self, style=wx.TE_MULTILINE)

    def append_text(self, text):
        self.editor.AppendText(text)


def read_text_append(frame, filename):
    # It's tail -f like
    with open(filename) as file_text:
        while True:
            where = file_text.tell()
            line = file_text.readline()
            if not line:
                file_text.seek(where)
            else:
                frame.append_text(line)
            gevent.sleep()


def main():
    app = MyApp(0)
    frame = Main()
    frame.Show(True)
    app.SetTopWindow(frame)

    # the trick
    gevent.joinall([gevent.spawn(app.MainLoop), 
                    gevent.spawn(read_text_append, frame, sys.argv[-1])])


if __name__ == '__main__':
    main()
