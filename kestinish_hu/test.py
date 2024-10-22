import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

#startbutton stopbutton
#autostart
#calendarium, widget

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.widget)
        vid = QMediaContent(QUrl.fromLocalFile("Video\\8.avi"))
        self.media.setMedia(vid)
        self.media.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
