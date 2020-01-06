from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
import sys
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 700, 600)
        self.setWindowTitle('Git и случайные окружности')
        self.pushButton = QPushButton('СОЗДАТЬ ОКРУЖНОСТИ', self)
        self.pushButton.adjustSize()
        self.pushButton.move(10, 10)
        self.pushButton.clicked.connect(self.create_circles)
        self.pressed = False

    def create_circles(self):
        self.pressed = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        if not self.pressed:
            return True
        for i in range(random.randint(10, 25)):
            size = random.randint(30, 90)
            x, y = random.randint(50, 600), random.randint(50, 500)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            qp.drawEllipse(x, y, size, size)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
