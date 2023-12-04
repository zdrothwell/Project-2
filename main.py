from logic import *


def main():
    application = QApplication([])
    window = Logic()
    window.setWindowTitle('FinalProjectPart2')
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
