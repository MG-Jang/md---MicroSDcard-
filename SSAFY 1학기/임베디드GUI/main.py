from PySide6.QtWidgets import *
from PySide6.QtCore import *
from prog_ui import Ui_Form

class MyApp(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.val = 0
        self.flag = 0
        self.progressBar.setValue(0)
        self.main()


    def main(self):
        self.tm = QTimer()
        self.tm.setInterval(50)
        self.tm.timeout.connect(self.go)

    def go(self):
        if (self.flag == 0):
            self.tm.start()
            self.flag = 1
        self.progressBar.setValue(self.val)
        if (self.val == 100):
            self.tm.stop()
            print(self.tm.isActive())
        else:
            self.val += 1

    def pause(self):
        self.tm.stop()
        self.flag = 0

    def reset(self):
        self.val = 0
        self.progressBar.setValue(self.val)


    def run(self):
        print("#", end='')


app = QApplication()
win = MyApp()
win.show()
app.exec()