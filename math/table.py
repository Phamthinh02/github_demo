from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout, QTableWidgetItem, QTableWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600,600,800,300)
        self.setWindowTitle("Bảng só sánh áp suất")

        self.table_analysis()


        
    def table_analysis(self):
        vbox = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(5)
        table_widget.setColumnCount(6)
        
# column
        table_widget.setItem(0,0, QTableWidgetItem("Xylanh"))
        table_widget.setItem(0,1, QTableWidgetItem("Pc max"))
        table_widget.setItem(0,2, QTableWidgetItem("P nạp "))
        table_widget.setItem(0,3, QTableWidgetItem("P nạp (lý thuyết)"))
        table_widget.setItem(0,4, QTableWidgetItem("% Chênh lệch"))
        table_widget.setItem(0,5, QTableWidgetItem("Trạng thái"))

# Row
        table_widget.setItem(1,0, QTableWidgetItem("Xylanh 1"))
        table_widget.setItem(2,0, QTableWidgetItem("Xylanh 2"))
        table_widget.setItem(3,0, QTableWidgetItem("Xylanh 3"))
        table_widget.setItem(4,0, QTableWidgetItem("Xylanh 4"))

# Value
        value_1 = 123
        name_1 = "{}".format(value_1)

        value_2 = 234
        name_2 = "{}".format(value_2)

# Add value
        table_widget.setItem(1,1, QTableWidgetItem(name_1))
        table_widget.setItem(2,1, QTableWidgetItem(name_2))



# Display
        vbox.addWidget(table_widget)
        self.setLayout(vbox)
    
App = QApplication(sys.argv)
window = Window()
    
window.show()
sys.exit(App.exec())