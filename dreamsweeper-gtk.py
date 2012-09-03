# Copyright (C) 2012 by Vincent Povirk
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys

import gtk

class MainWindow(object):
    def __init__(self):
        self.window = gtk.Window()

        self.window.connect('delete-event', self.on_delete)

        self.drawing_area = gtk.DrawingArea()

        self.drawing_area.connect('expose-event', self.on_area_expose)

        self.drawing_area.show()

        self.window.add(self.drawing_area)

        self.window.show()

    def on_delete(self, widget, event):
        gtk.main_quit()

    def on_area_expose(self, widget, event):
        drawable = widget.window
        allocation = widget.get_allocation()
        gc = drawable.new_gc()
        drawable.draw_rectangle(gc, True, 0, 0, allocation.width, allocation.height)
        return True


def main(argv):
    window = MainWindow()

    gtk.main()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

