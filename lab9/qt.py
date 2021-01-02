from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

# w = QWidget()
# w.resize(250, 150)
# app = QApplication([])
# button = QPushButton()
# button.setFixedSize(QSize(20, 15))
# button.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
# x = button.width()
# y = button.height()
# points = [QPoint(0, 0), QPoint(x/2, 0), QPoint(x, y/2), QPoint(x/2, y), QPoint(0, y)]
# button.setMask(QRegion(QPolygon(points)))
# button.show()
# app.exec_()

# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a tooltip on 
a window and a button.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        button = QPushButton(self)
        button.setFixedSize(QSize(45, 150))
        button.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        x = button.width()
        y = button.height()
        points = [QPoint(0, 0), QPoint(0,y), QPoint(x,y), QPoint(x, y/2), QPoint(x-20, y/2), QPoint(x-20,0)]
        button.setMask(QRegion(QPolygon(points)))
        button.setStyleSheet("QPushButton {background-color: black}"
                             "QPushButton:pressed { background-color: gray }")


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
