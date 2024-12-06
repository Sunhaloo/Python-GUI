from PySide6 import QtCore, QtWidgets, QtGui
import sys

# create the main window
class Main_Window(QtWidgets.QWidget):
    # create the constructor
    def __init__(self):
        super().__init__()

        # set the "size" application
        self.setGeometry(100, 100, 800, 600)
        self.resize(800, 600)
        self.setWindowTitle("Background Colour")

        self.setStyleSheet(
                "background-color: black;"
            )

        self.label = QtWidgets.QLabel(
                text = "Hello World",
                alignment = QtCore.Qt.AlignCenter
            )

        self.label.setStyleSheet(
                "color: white;"
            )

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)

def main():
    app = QtWidgets.QApplication([])

    window = Main_Window()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
