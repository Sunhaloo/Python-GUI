from PySide6 import QtCore, QtWidgets, QtGui
from random import randint
import os
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
                "background-color: white;"
            )

        self.label = QtWidgets.QLabel(
                text = "Hello World",
                alignment = QtCore.Qt.AlignCenter
            )

        # create the button
        self.dark_light_button = QtWidgets.QToolButton(self)
        # explicitly add the text back ==> as you can see not passing args in `QToolButton`
        self.dark_light_button.setText("Dark Mode")

        # get the path of the icon
        dark_mode_icon = QtGui.QIcon(os.path.expanduser("~/GitHub/Python-GUI/assets/icons/dark_mode_icon.png"))
        # set button icon
        self.dark_light_button.setIcon(dark_mode_icon)

        # place the text for the button next to the icon ( of the button )
        self.dark_light_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        # place the text for the button below to the icon ( of the button )
        # self.dark_light_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # text button only
        # self.dark_light_button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        # icon button only
        # self.dark_light_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)

        self.label.setStyleSheet(
                "color: black;"
            )

        # styling for our dark mode button
        self.dark_light_button.setStyleSheet(
                "text-align: left;"
                "background-color: red;"
                "color: white;"
            )

        # add functionality to our dark mode button
        self.dark_light_button.clicked.connect(self.click_dark_mode_button)

        self.layout = QtWidgets.QHBoxLayout(self)
        # self.layout.addWidget(self.label)
        self.layout.addWidget(self.dark_light_button)

    # create a simple click functionality
    def click_dark_mode_button(self):
        # output in terminal
        random_number = randint(0, 100)
        print("Dark Mode Button has been Pressed!!!")
        print(f"Random Number: {random_number}\n")

def main():
    app = QtWidgets.QApplication([])

    window = Main_Window()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
