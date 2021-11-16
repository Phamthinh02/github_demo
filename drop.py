import sys
import os
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class ImageLabel(QLabel):
    def __init__(self, parent = None):
        super(ImageLabel, self).__init__(parent)
        self.setAcceptDrops(True)
        
        self.setAlignment(Qt.AlignCenter)
        
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)
    
    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()
        
    def dragLeaveEvent(self, event):
        event.accept()
        
    def dropEvent(self, event):
        event.accept()
        item = QGraphicsPixmapItem(QPixmap("images/{}".format("x")))
        item.setFlags(QGraphicsItem.ItemIsSelectable|
                      QGraphicsItem.ItemIsMovable)
        position = QCursor.pos()
        item.setOffset(QPointF(position))
        self.addItem(item)
        

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)

    def pictureDropped(self, l):
        pixel = [500,500]
        for url in l:
            if os.path.exists(url):
                print(url)
                icon = QIcon(url)
                pixmap = icon.pixmap(72, 72)
                icon = QIcon(pixmap)
                item = QListWidgetItem(url, self.view)
                item.setIcon(icon)
                item.setStatusTip(url)
                
    # def dropEvent(self, event):
    #     pos = [0,0]
    #     pixel = [500,500]
    #     event.setDropActions(Qt.CopyAction)
        
    #     if event.mimeData().hasUrls:
    #         file_path = event.mimeData().urls()[0].toLocalFile()
    #         img = QtGui.QImage(file_path)
    #         img = img.scaled(pixel[0], pixel[1])
    #         self.photoViewer.setPixmap(QPixmap(img))


    #         event.accept()
    #     else:
    #         event.ignore()


        
        
app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())