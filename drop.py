import sys
import os
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class Mainwindow(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.resize(1000, 1000)
        self.setAcceptDrops(True)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.setWindowTitle('Drag & drop')
        self.setScene(self.scene)
        self.setAcceptDrops(True)
        self.pos = [0,0]
        self.pos_2 = [0,0]
        self.pixel = [100,100]

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            file_path = event.mimeData().urls()[0].toLocalFile()
            img = QtGui.QImage(file_path)
            img = img.scaled(self.pixel[0],self.pixel[1])
            self.set_image(img)

            event.accept()
        else:
            event.ignore()

    def set_image(self, img):
        Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
        self.scene.addItem(Pimax_Item)
        Pimax_Item.setOffset(self.pos[0], self.pos[1]) 
        self.pos[0] += self.pixel[0] + 5
        self.pos[1] += self.pixel[1] + 5        


        
        
app = QApplication(sys.argv)
main = Mainwindow()
main.show()
sys.exit(app.exec_())