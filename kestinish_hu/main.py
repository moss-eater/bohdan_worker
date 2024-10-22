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
        self.configure()
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.widget)
        self.get_date()

    def configure(self):
        self.ui.startbutton.clicked.connect(self.media_play)
        self.ui.stopbuttton.clicked.connect(self.media_stop)
        self.ui.calendarium.selectionChanged.connect(self.get_date)

    def get_date(self):
        self.media_stop()
        print(self.ui.calendarium.selectedDate())
        day = str(self.ui.calendarium.selectedDate().day())

        self.media.setMedia(QMediaContent(QUrl.fromLocalFile(f'Video\\{day}.avi')))
        if self.ui.autostart.isChecked():
            self.media_play()

    def media_play(self):
        self.media.play()

    def media_stop(self):
        self.media.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
