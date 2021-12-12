from random import randint
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QPainter, QColor


class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('UI.ui', self)
        self.color = 'Yellow'
        self.show()
        self.pushButton.clicked.connect(self.draw)
        self.run = True

    def draw(self):
        self.run = True

    def paintEvent(self, event):
        if self.run:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def drawing(self, qp):
        for i in range(randint(1, 10)):
            qp.setBrush(QColor(self.color))
            a = randint(1, 100)
            qp.drawEllipse(10, 10, a, a)

        self.update()
        self.run = False


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()