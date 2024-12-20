import sys
import random

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn.setText('Создать')
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        for i in range(random.randint(30, 100)):
            diameter = random.randrange(300)
            a_side = random.randrange(300)
            b_side = random.randrange(300)
            randx = random.randrange(750)
            randy = random.randrange(750)
            r, g, b = random.randrange(256), random.randrange(256), random.randrange(256)
            qp.setBrush(QColor(r, g, b))
            qp.drawRect(randx, randy, a_side, b_side)
            qp.drawEllipse(randx, randy, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())