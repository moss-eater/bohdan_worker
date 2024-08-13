from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox

app = QApplication([])

def peremoha():
    victory = QMessageBox()
    victory.setText("Правильно!\nВи виграли гіроскутер")
    victory.show()
    victory.exec_()

def zrada():
    loss = QMessageBox()
    loss.setText("Ні, в 2015 році.\nВи виграли фірмовий плакат")
    loss.show()
    loss.exec_()

my_wind = QWidget()
my_wind.setWindowTitle("Конкурс від Crazy People")
my_wind.move(100, 100)
my_wind.resize(400, 200)

question = QLabel("В якому році канал отримав 'золоту кнопку' від YouTube?")
btn_ans1 = QRadioButton("2005")
btn_ans2 = QRadioButton("2010")
btn_ans3 = QRadioButton("2015")
btn_ans4 = QRadioButton("2020")

layoutV = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment = Qt.AlignCenter)

layoutH2.addWidget(btn_ans1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_ans2, alignment = Qt.AlignCenter)

layoutH3.addWidget(btn_ans3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_ans4, alignment = Qt.AlignCenter)

layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)

my_wind.setLayout(layoutV)

btn_ans3.clicked.connect(peremoha)
btn_ans1.clicked.connect(zrada)
btn_ans2.clicked.connect(zrada)
btn_ans4.clicked.connect(zrada)

my_wind.show()
app.exec_()