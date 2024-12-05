from PySide6 import QtCore, QtWidgets, QtGui
import sys

# create the main window for our program
class Main_Window(QtWidgets.QWidget):
    # initialise our constructor
    def __init__(self):
        super().__init__()

        # resize the application
        self.resize(1280, 720)
        self.setWindowTitle("PyYu")


# our main function
def main():
    # initialise the whole application / python program
    app = QtWidgets.QApplication([])


    # create an instance of the window / GUI Window
    window = Main_Window()
    # apply them method `show` to make the "program" show
    window.show()

    # execute the application with `sys`
    sys.exit(app.exec())



if __name__ == '__main__':
    main()
