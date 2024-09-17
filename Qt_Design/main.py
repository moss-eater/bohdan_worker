import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.example)

    def example(self):
        signs=''
        if self.ui.cb_alphabet.isChecked():
            signs = 'qwertyuiopasdfghjklzxcvbnm'
        if self.ui.cb_numbers.isChecked():
            signs += '1234567890'

        result = ''
        number = random.randint(5,15)
        for i in range(number):
            result += random.choice(signs)

        self.ui.result.setText(result)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()