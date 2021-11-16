import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QGraphicsScene, QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class SceneView(QGraphicsScene):

    def __init__(self, parent=None):
        super(SceneView, self).__init__(parent)

    def dragEnterEvent(self, event):
        event.accept()
        print("drag enter")

    def dropEvent(self, event):
        event.accept()
        item = QGraphicsPixmapItem(QPixmap("images/{}".format("x")))
        item.setFlags(QGraphicsItem.ItemIsSelectable|
                      QGraphicsItem.ItemIsMovable)
        position = QCursor.pos()
        item.setOffset(QPointF(position))
        self.addItem(item)
        print("drop")
        

    def dragMoveEvent(self, event):
        event.accept()
        print("drag move")

    def dragLeaveEvent(self, event):
        event.accept()
        print("drag leave")

class mainWindow(QMainWindow):
    
    def __init__(self, parent = None):
        super(mainWindow, self).__init__(parent)
        
        #populate QListwidget
        path = os.path.dirname(sys.argv[0])
        for image in sorted(os.listdir(os.path.join(path, "images"))):
            if image.endswith(".png"):
                item = QListWidgetItem(image.split(".")[0].capitalize())
                item.setIcon(QIcon(os.path.join(path,
                                   "images/{}".format(image))))
                self.listWidget.addItem(item)

        self.scene = SceneView()
        self.scene.setSceneRect(0, 0, 630, 555)
        self.nodeDropGraphicsView.setSceneRect(0, 0, 630, 555)
        self.nodeDropGraphicsView.setAcceptDrops(True)
        self.nodeDropGraphicsView.setScene(self.scene)
        self.nodeDropGraphicsView.showMaximized()
        self.scene.addText("HI")
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = mainWindow()
    form.show()
    app.exec_()