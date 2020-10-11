from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from new_fraction import NewFraction


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('gui.ui')

    def __set_slots(self):
        self.__win.ButtonSum.clicked.connect(self.__sum)
        self.__win.ButtonSub.clicked.connect(self.__sub)
        self.__win.ButtonMul.clicked.connect(self.__mul)
        self.__win.ButtonDiv.clicked.connect(self.__div)

    def show(self):
        self.__set_slots()
        self.__win.show()

    def __sum(self):
        a = NewFraction(self.__win.lineEdit.text())
        b = NewFraction(self.__win.lineEdit_2.text())
        QMessageBox.information(self, 'Результат:', f'{a} + {b} = {a + b}')

    def __sub(self):
        a = NewFraction(self.__win.lineEdit.text())
        b = NewFraction(self.__win.lineEdit_2.text())
        QMessageBox.information(self, 'Результат:', f'{a} - {b} = {a - b}')

    def __mul(self):
        a = NewFraction(self.__win.lineEdit.text())
        b = NewFraction(self.__win.lineEdit_2.text())
        QMessageBox.information(self, 'Результат:', f'{a} * {b} = {a * b}')

    def __div(self):
        a = NewFraction(self.__win.lineEdit.text())
        b = NewFraction(self.__win.lineEdit_2.text())
        QMessageBox.information(self, 'Результат:', f'{a} / {b} = {a / b}')
