import sys
import numpy as np
import matplotlib.pyplot as plt

from PySide import QtGui, QtCore

def draw_to_array():
    # It's RGBA image, 8bit each band. 8x4=32
    arr = np.zeros((1000, 1000, 4), dtype='uint8')
    img = QtGui.QImage(arr, 1000, 1000, QtGui.QImage.Format_ARGB32)

    p = QtGui.QPainter()
    p.begin(img)
    p.setPen(QtGui.QColor(255, 128, 0, 255))
    p.setBrush(QtGui.QColor(22, 55, 50, 255))
    p.setFont(QtGui.QFont('Decorative', 32))
    p.drawText(300, 300, 'Manolo doido')
    p.drawLine(1000, 1000, 0, 0)
    p.drawEllipse(500, 500, 250, 250)
    p.end()

    # Showing using Matplotlib
    plt.imshow(arr)
    plt.show()


def main():
    # Without the creation of QApplication the script crashes when drawing
    # text.
    app = QtGui.QApplication(sys.argv)
    draw_to_array()


if __name__ == "__main__":
    main()
