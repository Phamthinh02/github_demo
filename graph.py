# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphic = QtWidgets.QPushButton(self.centralwidget)
        self.graphic.setGeometry(QtCore.QRect(250, 420, 311, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.graphic.setFont(font)
        self.graphic.setObjectName("graphic")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 780, 400))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.graphic.clicked.connect(self.ghapic)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.graphic.setText(_translate("MainWindow", "GRAPHIC"))

    def ghapic (self):
        filenames,_ = QtWidgets.QFileDialog.getOpenFileNames()
        self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)
        pos = [0,0]
        k = 0
        i = 0
        for file in filenames:
            img = QtGui.QImage(file)
            i += 1
            k = int(len(filenames))
            
            if i <= round(k/2):
                img = img.scaled(760/round(k/2),380/2)
                Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
                a = self.scene.addItem(Pimax_Item)
                
                pos[0] += 765/round(k/2)
                
                Pimax_Item.setOffset(pos[0], pos[1])
                
            elif i > round(k/2):
                pos[1] = 385/2
                img = img.scaled(760/round(k/2),380/2)
                Pimax_Item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(img))
                a = self.scene.addItem(Pimax_Item)
                
                Pimax_Item.setOffset(pos[0], pos[1])
                
                pos[0] -= 765/round(k/2)
                
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
