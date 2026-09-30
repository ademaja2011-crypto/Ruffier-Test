from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QApplication)
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_UI()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def init_UI(self):
        self.lbl_index = QLabel(txt_index)
        self.lbl_performance = QLabel(txt_workheart)
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.lbl_index, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.lbl_performance, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.main_layout)
