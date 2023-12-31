# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.voteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.voteButton.setGeometry(QtCore.QRect(35, 420, 85, 25))
        self.voteButton.setObjectName("voteButton")
        self.resultsButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resultsButton.setGeometry(QtCore.QRect(155, 420, 85, 25))
        self.resultsButton.setObjectName("resultsButton")
        self.saveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(270, 420, 85, 25))
        self.saveButton.setObjectName("saveButton")
        self.clearButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(155, 450, 85, 25))
        self.clearButton.setObjectName("clearButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.dropdownBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.dropdownBox.setGeometry(QtCore.QRect(100, 120, 200, 30))
        self.dropdownBox.setObjectName("dropdownBox")
        self.dropdownBox.addItem("")
        self.dropdownBox.addItem("")
        self.dropdownBox.addItem("")
        self.dropdownBox.addItem("")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 200, 200, 150))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.voteButton.setText(_translate("MainWindow", "Vote"))
        self.resultsButton.setText(_translate("MainWindow", "Results"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "Choose your candidate from the dropdown and click \"Vote\" to enter your vote!"))
        self.dropdownBox.setItemText(0, _translate("MainWindow", "Choose your candidate!"))
        self.dropdownBox.setItemText(1, _translate("MainWindow", "Cameron"))
        self.dropdownBox.setItemText(2, _translate("MainWindow", "Allison"))
        self.dropdownBox.setItemText(3, _translate("MainWindow", "Diego"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
