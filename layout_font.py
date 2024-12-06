from PySide6 import QtCore, QtWidgets, QtGui
import os
import sys

# create a function for our system-wide font
def system_wide_font(font_name: str, font_size: int) -> QtGui.QFont:
    return QtGui.QFont(font_name, font_size)

# create a function for GitHub Monaspace Font
def monaspice_radon(font_size: int = 12) -> QtGui.QFont:
    # find the custom font in our system
    font_path: str = "/usr/share/fonts/OTF/MonaspiceRnNerdFontMono-Regular.otf"
    # get the font name
    font_name = os.path.basename(font_path)

    # get the ID of our custom font
    font_id = QtGui.QFontDatabase.addApplicationFont(font_path)

    # check if our custom font is loaded properly
    if font_id != -1:
        # NOTE: this one will be printed in the terminal
        print(f"Successfully Loaded Custom Font '{font_name}'")
        # add the font
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        # allow our program to use the font
        return QtGui.QFont(font_family, font_size)

    else:
        # if our font has not been loaded
        print(f"\nError: {font_id} ==> Font '{font_name}' Has NOT Been Loaded")
        print("Using Default Font\n")
        return QtGui.QFont(system_wide_font("DejaVu Serif", 12))


# create a function for ProggyClean Font
def proggy_clean(font_size: int = 12) -> QtGui.QFont:
    # find the custom font in our system
    font_path: str = "/usr/share/fonts/TTF/ProggyCleanNerdFont-Regular.ttf"
    # get the font name
    font_name = os.path.basename(font_path)

    # get the ID of our custom font
    font_id = QtGui.QFontDatabase.addApplicationFont(font_path)

    # check if our custom font is loaded properly
    if font_id != -1:
        # NOTE: this one will be printed in the terminal
        print(f"Successfully Loaded Custom Font '{font_name}'")
        # add the font
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        # allow our program to use the font
        return QtGui.QFont(font_family, font_size)

    else:
        # if our font has not been loaded
        print(f"\nError: {font_id} ==> Font '{font_name}' Has NOT Been Loaded")
        print("Using Default Font\n")
        return QtGui.QFont(system_wide_font("DejaVu Serif", 12))


# create a function for JetBrainsMono Font
def program_font(font_size: int = 12):
    # find the custom font in our system
    font_path: str = "/usr/share/fonts/TTF/JetBrainsMonoNerdFontMono-Regular.ttf"
    # get the font name
    font_name = os.path.basename(font_path)

    # get the ID of our custom font
    font_id = QtGui.QFontDatabase.addApplicationFont(font_path)

    # check if our custom font is loaded properly
    if font_id != -1:
        # NOTE: this one will be printed in the terminal
        print(f"Successfully Loaded Custom Font '{font_name}'")
        # add the font
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        # allow our program to use the font
        return QtGui.QFont(font_family, font_size)

    else:
        # if our font has not been loaded
        print(f"\nError: {font_id} ==> Font '{font_name}' Has NOT Been Loaded")
        print("Using Default Font\n")
        return QtGui.QFont(system_wide_font("DejaVu Serif", 12))

# create the main window for our program
class Main_Window(QtWidgets.QWidget):
    # initialise our constructor
    def __init__(self):
        super().__init__()

        # set the "size" application
        self.setGeometry(100, 100, 800, 600)
        self.resize(800, 600)
        self.setWindowTitle("Layout and Fonts")

        # INFO: Testing --> create a label for testing
        self.test_label = QtWidgets.QLabel(
                text = "Hello World",
                alignment = QtCore.Qt.AlignCenter
            )

        self.randon_font_added = QtWidgets.QLabel(
                text = "With GitHub Monaspace Radon Font",
                alignment = QtCore.Qt.AlignTop
            )

        self.proggy_font_added = QtWidgets.QLabel(
                text = "With Proggy Clean Font",
                alignment = QtCore.Qt.AlignBottom
            )

        self.default_program_font = QtWidgets.QLabel(
                text = "With Default Font",
                alignment = QtCore.Qt.AlignRight
            )


        # INFO: Testing --> system wide fonts
        # apply the system wide font to `test_label`
        self.test_label.setFont(system_wide_font("DejaVu Serif", 20))
        # self.test_label.setFont(system_wide_font("Noto Serif CJK SC", 20))

        # INFO: Testing --> custom - downloaded fonts
        # call the function and apply the font with default font size
        self.randon_font_added.setFont(monaspice_radon())
        self.proggy_font_added.setFont(proggy_clean())

        # INFO: Testing --> create the box layout
        self.box_layout = QtWidgets.QHBoxLayout(self)
        # place the label acksually
        self.box_layout.addWidget(self.test_label)
        self.box_layout.addWidget(self.randon_font_added)
        self.box_layout.addWidget(self.proggy_font_added)
        self.box_layout.addWidget(self.default_program_font)


# our main function
def main():
    # initialise the whole application / python program
    app = QtWidgets.QApplication([])


    # INFO: Testing --> setting a main font for everything in the app
    # call the function to set our "default" font for our program
    app.setFont(program_font())


    # create an instance of the window / GUI Window
    window = Main_Window()
    # apply them method `show` to make the "program" show
    window.show()


    # execute the application with `sys`
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

