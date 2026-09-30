from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QApplication)
from instr import *
from testscreen import TestWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_UI()
        self.connects()

    def set_appear(self):
        self.setWindowTitle(txt_hello)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def init_UI(self):
        self.lbl_hello = QLabel(txt_hello)
        self.lbl_intro = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.lbl_hello, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addWidget(self.lbl_intro, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addWidget(self.btn_next, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.main_layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next)

    def next(self):
        self.next_window = TestWin()
        self.next_window.show()
        self.hide()

app = QApplication([])
window = MainWin()
window.show()
app.exec_()