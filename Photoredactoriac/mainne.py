import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QHBoxLayout,  QLabel, QListWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageFilter import SHARPEN, BLUR, EDGE_ENHANCE

app = QApplication([])
window = QWidget()
window.resize(1000, 500)
window.setWindowTitle("Легкий Фоторедактор")

label_image = QLabel("Тут буде зображенння, оберіть будь ласка у папці")
button_directory = QPushButton("Обрати папку")
list_offiles = QListWidget()

button_lefte = QPushButton("Повернути наліво")
button_rigt = QPushButton("Повернути напрво")
button_mirrore = QPushButton("Відзеркалити")
button_distoratum = QPushButton("Різкість")
button_bluuricon = QPushButton("Розмиття")
button_ejjinium = QPushButton("Контури")
button_blachwicht = QPushButton("Чорнобілий")

rowlow = QHBoxLayout()
rowlow.addWidget(button_lefte)
rowlow.addWidget(button_rigt)
rowlow.addWidget(button_mirrore)
rowlow.addWidget(button_distoratum)
rowlow.addWidget(button_bluuricon)
rowlow.addWidget(button_ejjinium)
rowlow.addWidget(button_blachwicht)


column1 = QVBoxLayout()
column1.addWidget(button_directory)
column1.addWidget(list_offiles)

column2 = QVBoxLayout()
column2.addWidget(label_image, 90)
column2.addLayout(rowlow)

rowhigh = QHBoxLayout()
rowhigh.addLayout(column1, 20)
rowhigh.addLayout(column2, 80)

window.setLayout(rowhigh)

window.show()

workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.bpm', '.gif']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)

    list_offiles.clear()
    for filename in filenames:
        list_offiles.addItem(filename)

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.dir = None
        self.image = None
        self.save_dir = "Modified/"

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        label_image.hide()
        pixmapimage = QPixmap(path)
        width, height = label_image.width(), label_image.height()
        pixmapimage = pixmapimage.scaled(width, height, Qt.KeepAspectRatio)
        label_image.setPixmap(pixmapimage)
        label_image.show()
    
    def do_blachwachen(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_leftenk(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_rightangh(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_mirrorei(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_enhansechin(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_bluuriconna(self):
        self.image = self.image.filter(BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_ejjiniumhau(self):
        self.image = self.image.filter(EDGE_ENHANCE)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

workimage = ImageProcessor()

def showChosenItem():
    if list_offiles.currentRow() >= 0:
        filename = list_offiles.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

button_directory.clicked.connect(showFilenamesList)
list_offiles.currentRowChanged.connect(showChosenItem)
button_blachwicht.clicked.connect(workimage.do_blachwachen)
button_bluuricon.clicked.connect(workimage.do_bluuriconna)
button_lefte.clicked.connect(workimage.do_leftenk)
button_ejjinium.clicked.connect(workimage.do_ejjiniumhau)
button_rigt.clicked.connect(workimage.do_rightangh)
button_distoratum.clicked.connect(workimage.do_enhansechin)
button_mirrore.clicked.connect(workimage.do_mirrorei)

app.exec_()