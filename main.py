from random import randint
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QPainter, QColor


class Main(QtWidgets.QDialog):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.run = False
        self.show()

    def draw(self):
        self.run = True
        self.update()

    def paintEvent(self, event):
        if self.run:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('Yellow'))
            for i in range(10):
                r = randint(10, 90)
                qp.drawEllipse(randint(5, 300), randint(5, 300), r, r)
            qp.end()


app = QtWidgets.QApplication(sys.argv)
window = Main()
app.exec_()
