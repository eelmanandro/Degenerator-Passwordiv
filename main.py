from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from PyQt5 import QtCore

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Degenerate.clicked.connect(self.generate_password)

    def generate_password(self):
        import random
        import string

        length = 12  # You can set desired password length here
        characters = ""

        if self.ui.UseNumba.isChecked():
            characters += string.digits
        if self.ui.UseLeta.isChecked():
            characters += string.ascii_letters

        if not characters:
            self.ui.Resultiit.setText("Виберіть хоча б один тип символів!")
            return

        password = ''
        for _ in range(length):
            password += random.choice(characters)

        self.ui.Resultiit.setText(password)
        self.ui.Resultiit.setAlignment(QtCore.Qt.AlignCenter) 

app = QApplication([])
window = Widget()
window.show()
app.exec_()