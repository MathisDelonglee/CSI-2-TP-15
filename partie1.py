from PySide2.QtWidgets import *
from partie2 import *

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)
        self.layout = QVBoxLayout()

        self.buttonsPanel = ButtonsPanel()
        self.layout.addWidget(self.buttonsPanel)

        self.notificationPanel = QTextEdit()
        self.layout.addWidget(self.notificationPanel)

        self.resultTable = QTableWidget(5,3)
        self.layout.addWidget(self.resultTable)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setLayout(self.layout)



class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.Boutton1 = QPushButton('Configure')
        self.Boutton2 = QPushButton('Correct')
        self.Boutton3 = QPushButton('Disconnect')

        self.layout.addWidget(self.Boutton1)
        self.layout.addWidget(self.Boutton2)
        self.layout.addWidget(self.Boutton3)


        self.setLayout(self.layout)


if __name__ == "__main__":
   app = QApplication([])
   SQL2 = ConfigurationDialog()
   SQL = SQLClientWindow()
   SQL.show()
   SQL2.show()
   app.exec_()
