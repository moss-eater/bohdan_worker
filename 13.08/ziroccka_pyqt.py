from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox

app = QApplication([])

def peremoha():
    victory = QMessageBox()
    victory.setText("Правильно!\nВи отримали шоколадку за навчання!")
    victory.show()
    victory.exec_()

def zrada():
    loss = QMessageBox()
    loss.setText("Ні, ніфіга.\nВи маєте вчитись далі!")
    loss.show()
    loss.exec_()

def create_hbox_layout(label, widget):
    hbox = QHBoxLayout()
    hbox.addWidget(label)
    hbox.addWidget(widget)
    return hbox


my_wind = QWidget()
my_wind.setWindowTitle("пЕтання по нашій темі")
my_wind.move(100, 100)
my_wind.resize(400, 200)

question = QLabel("Якою версією бібліотеки PyQt ми користувались?")
btn_ans1 = QRadioButton("6")
btn_ans2 = QRadioButton("5")
btn_ans3 = QRadioButton("1")
btn_ans4 = QRadioButton("9")

layout = QVBoxLayout()

layout.addWidget(question, alignment = Qt.AlignCenter)
layout.addLayout(create_hbox_layout(btn_ans1, btn_ans2))
layout.addLayout(create_hbox_layout(btn_ans3, btn_ans4))

my_wind.setLayout(layout)

btn_ans2.clicked.connect(peremoha)
btn_ans1.clicked.connect(zrada)
btn_ans3.clicked.connect(zrada)
btn_ans4.clicked.connect(zrada)

my_wind.setStyleSheet("""
        QLabel {
            font-family: Arial, sans-serif;
            font-size: 16px;
            color: #333;
                           
        }
                           
        QRadioButton {
            font-size: 24px;
            background-color: #ffc800;
            border: none;
            padding: 4px;
        }                 
        """)

my_wind.show()
app.exec_()