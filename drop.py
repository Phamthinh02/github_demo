import sys
import os
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)

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
        pos = [0,0]
        pixel = [500,500]
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            img = QtGui.QImage(file_path)
            img = img.scaled(pixel[0], pixel[1])
            self.photoViewer.setPixmap(QPixmap(img))
            self.set_image(img)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
                


        
        
app = QApplication(sys.argv)
main = Mainwindow()
main.show()
sys.exit(app.exec_())