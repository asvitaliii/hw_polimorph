from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from new_fraction import *


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('gui.ui')

    def set_slots(self):
        self.__win.ButtonSum.clicked.connect(self.sum)
        self.__win.ButtonSub.clicked.connect(self.sub)
        self.__win.ButtonMul.clicked.connect(self.mul)
        self.__win.ButtonDiv.clicked.connect(self.div)

    def show(self):
        self.set_slots()
        self.__win.show()

    def sum(self):
        a = NewFraction(self.__win.lineEdit.text())
        b = NewFraction(self.__win.lineEdit_2.text())
        QMessageBox.information(self, 'Результат:', f'{a} + {b} = {a + b}')

    def sub(self):
        a = NewFraction(self.__win.lineEdit.text())
        b = NewFraction(self.__win.lineEdit_2.text())
        QMessageBox.information(self, 'Результат:', f'{a} - {b} = {a - b}')

    def mul(self):
        a = NewFraction(self.__win.lineEdit.text())
        b = NewFraction(self.__win.lineEdit_2.text())
        QMessageBox.information(self, 'Результат:', f'{a} * {b} = {a * b}')

    def div(self):
        a = NewFraction(self.__win.lineEdit.text())
        b = NewFraction(self.__win.lineEdit_2.text())
        QMessageBox.information(self, 'Результат:', f'{a} / {b} = {a / b}')
