from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox

app = QApplication([])

def peremoha():
    victory = QMessageBox()
    victory.setText("Ви виграли зустріч з творцями каналу!")
    victory.show()
    victory.exec_()

def zrada():
    loss = QMessageBox()
    loss.setText("Пощастить іншим разом!")
    loss.show()
    loss.exec_()

my_wind = QWidget()
my_wind.setWindowTitle("пЕтання")
my_wind.move(100, 100)
my_wind.resize(400, 200)

question = QLabel("Як звали першого ютуб-блогера, який набрав 100000000 підписників?")
btn_ans1 = QRadioButton("Рет і Лінк")
btn_ans2 = QRadioButton("TheBrianMaps")
btn_ans3 = QRadioButton("EeOneGuy")
btn_ans4 = QRadioButton("SlivkiShow")
btn_ans5 = QRadioButton("PewDiePie")
btn_ans6 = QRadioButton("Mister Max")

layoutV = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()

layoutH1.addWidget(question, alignment = Qt.AlignCenter)

layoutH2.addWidget(btn_ans1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_ans2, alignment = Qt.AlignCenter)

layoutH3.addWidget(btn_ans3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_ans4, alignment = Qt.AlignCenter)

layoutH4.addWidget(btn_ans5, alignment = Qt.AlignCenter)
layoutH4.addWidget(btn_ans6, alignment = Qt.AlignCenter)

layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
layoutV.addLayout(layoutH4)

my_wind.setLayout(layoutV)

btn_ans5.clicked.connect(peremoha)
btn_ans1.clicked.connect(zrada)
btn_ans2.clicked.connect(zrada)
btn_ans4.clicked.connect(zrada)
btn_ans3.clicked.connect(zrada)
btn_ans6.clicked.connect(zrada)

my_wind.show()
app.exec_()