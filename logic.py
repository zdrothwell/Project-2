from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(400, 500)
        self.voteButton.clicked.connect(self.vote_input)
        self.resultsButton.clicked.connect(self.results)
        self.saveButton.clicked.connect(self.save)
        self.clearButton.clicked.connect(self.clear)
        self.__cameron_votes = 0
        self.__allison_votes = 0
        self.__diego_votes = 0

    def vote_input(self):
        vote_choice = self.dropdownBox.currentIndex()
        if vote_choice == 1:
            self.__cameron_votes += 1
            self.label_2.setText("Voted!")
        elif vote_choice == 2:
            self.__allison_votes += 1
            self.label_2.setText("Voted!")
        elif vote_choice == 3:
            self.__diego_votes += 1
            self.label_2.setText("Voted!")
        else:
            self.label_2.setText("You need to select a candidate first.")
        self.dropdownBox.setCurrentIndex(0)
        return

    def results(self):
        self.label_2.setText(f"Votes for Candidate Totals"
                             f"\nCameron: {self.__cameron_votes}"
                             f"\nAllison: {self.__allison_votes}"
                             f"\nDiego: {self.__diego_votes}")
        return

    def save(self):
        with open('vote_totals.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['Candidate', 'Votes'])
            writer.writerow(['Cameron', self.__cameron_votes])
            writer.writerow(['Allison', self.__allison_votes])
            writer.writerow(['Diego', self.__diego_votes])
        self.label_2.setText("Vote totals have been saved to a file")
        return

    def clear(self):
        self.label_2.setText("")
        self.dropdownBox.setCurrentIndex(0)
        return

