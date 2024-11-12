import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QHBoxLayout,  QLabel, QListWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter

app = QApplication([])
window = QWidget()
window.resize(1000, 500)
window.setWindowTitle("Heasia Editorricume")

label_image = QLabel("pic")
button_directory = QPushButton("folde")
list_offiles = QListWidget()

button_left = QPushButton("turn lefte")
button_right = QPushButton("turn rigt")
button_mirror = QPushButton("mirrore")
button_sharp = QPushButton("radicalise")
button_bw = QPushButton("black|white")

rowlow = QHBoxLayout()
rowlow.addWidget(button_left)
rowlow.addWidget(button_right)
rowlow.addWidget(button_mirror)
rowlow.addWidget(button_sharp)
rowlow.addWidget(button_bw)

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
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    # saves file in a subfolder
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

workimage = ImageProcessor()

def showChosenItem():
    if list_offiles.currentRow() >= 0:
        filename = list_offiles.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

button_directory.clicked.connect(showFilenamesList)
button_bw.clicked.connect(workimage.do_bw)
list_offiles.currentRowChanged.connect(showChosenItem)

app.exec_()