from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """This fixes the window size to 400x500 pixels and takes in the gui class from the gui.py file.
        It also links the buttons to their respective functions and assigns vote totals as private
        variables for each of the candidates that were listed in the original Lab 1"""
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

    def vote_input(self) -> None:
        """This takes what index the dropdown box is set to assign a new total to the chosen candidate.
        It resets the dropdown box after every time the Vote button is clicked, and if a new candidate is not
        selected before trying to vote again, it will give you an error and do nothing else."""
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

    def results(self) -> None:
        """This just prints the vote totals in the output box using the class's private variables.
        The text box already aligns to the center for both height and width, so it is completely centered."""
        self.label_2.setText(f"Votes for Candidate Totals"
                             f"\nCameron: {self.__cameron_votes}"
                             f"\nAllison: {self.__allison_votes}"
                             f"\nDiego: {self.__diego_votes}")
        return

    def save(self) -> None:
        """This is a bit different from the original lab. When the save button is clicked, it will send the
        vote totals to a csv file labeled 'vote_totals.csv'. This way you can see the most recent use of the
        application saved in an easy-to-read format."""
        with open('vote_totals.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['Candidate', 'Votes'])
            writer.writerow(['Cameron', self.__cameron_votes])
            writer.writerow(['Allison', self.__allison_votes])
            writer.writerow(['Diego', self.__diego_votes])
        self.label_2.setText("Vote totals have been saved to a file")
        return

    def clear(self) -> None:
        """This just resets the output text box and the dropdown box."""
        self.label_2.setText("")
        self.dropdownBox.setCurrentIndex(0)
        return

