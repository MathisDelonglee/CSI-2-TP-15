from PySide2.QtWidgets import *

class LabeledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)
        self.setWindowTitle("Configuration")

        self.layout = QHBoxLayout()

        self.__QLabel = QLabel(text)
        self.__QTextEdit = QTextEdit()
        self.__QTextEdit.setMaximumHeight(30)

        self.layout.addWidget(self.__QLabel)
        self.layout.addWidget(self.__QTextEdit)

        self.setLayout(self.layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()

        self.objet1 = LabeledTextField("IP address")
        self.layout.addWidget(self.objet1)

        self.objet2 = LabeledTextField("User")
        self.layout.addWidget(self.objet2)

        self.objet3 = LabeledTextField("Password")
        self.layout.addWidget(self.objet3)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   LTF = ConfigurationDialog()
   LTF.show()
   app.exec_()
