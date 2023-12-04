from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(400, 500)
        self.voteButton.clicked.connect(self.vote_input)
        self.resultsButton.clicked.connect(self.results)
        self.saveButton.clicked.connect(self.save)

    def vote_input(self):
        return

    def results(self):
        self.label_2.setText("Bruh")
        return

    def save(self):
        return

