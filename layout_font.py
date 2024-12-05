from PySide6 import QtCore, QtWidgets, QtGui
import sys

# create the main window for our program
class Main_Window(QtWidgets.QWidget):
    # initialise our constructor
    def __init__(self):
        super().__init__()

        # set the "size" application
        self.setGeometry(100, 100, 800, 600)
        self.resize(800, 600)
        self.setWindowTitle("PyYu")

        # INFO: Testing --> create a label for testing
        self.test_label = QtWidgets.QLabel(
                text = "Hello World",
                alignment = QtCore.Qt.AlignCenter
            )

        self.randon_font_added = QtWidgets.QLabel(
                text = "With GitHub Monaspace Radon Font",
                alignment = QtCore.Qt.AlignTop
            )

        self.app_font_added = QtWidgets.QLabel(
                text = "With Proggy Clean Font",
                alignment = QtCore.Qt.AlignBottom
            )


        # INFO: Testing --> system wide fonts
        sys_wide_font = QtGui.QFont(
                "DejaVu Serif",
                10
            )
        # apply the devu system wide font to `test_label`
        self.test_label.setFont(sys_wide_font)

        # INFO: Testing --> custom - downloaded fonts
        # find the id of the font
        monaspice_radon_id = QtGui.QFontDatabase.addApplicationFont("/usr/share/fonts/OTF/MonaspiceRnNerdFontMono-Regular.otf")
        # check if the font is loaded
        if monaspice_radon_id != -1:
            print("Successfully Loaded Font")
            # add the font to the program
            monaspice_radon_font_family = QtGui.QFontDatabase.applicationFontFamilies(monaspice_radon_id)[0]

            # allow python program to use custom font
            monaspice_radon_font = QtGui.QFont(monaspice_radon_font_family, 12)
            # NOTE: apply to `no_font_added`
            self.randon_font_added.setFont(monaspice_radon_font)

        else:
            print(f"\nError: Could not Load Font {monaspice_radon_id}\n")

        # INFO: Testing --> create the box layout
        self.box_layout = QtWidgets.QHBoxLayout(self)
        # place the label acksually
        self.box_layout.addWidget(self.test_label)
        self.box_layout.addWidget(self.randon_font_added)
        self.box_layout.addWidget(self.app_font_added)


# our main function
def main():
    # initialise the whole application / python program
    app = QtWidgets.QApplication([])


    # INFO: Testing --> setting a main font for everything in the app
    proggy_clean_id = QtGui.QFontDatabase.addApplicationFont("/usr/share/fonts/TTF/ProggyCleanNerdFont-Regular.ttf")
    # check if the font has been loaded in your mother 
    if proggy_clean_id != -1:
        print("Successfully Loaded Font")
        proggy_clean_font_family = QtGui.QFontDatabase.applicationFontFamilies(proggy_clean_id)[0]

        # allow python program to use custom font
        proggy_clean_font = QtGui.QFont(proggy_clean_font_family, 16)

        # set the font for the whole application
        app.setFont(proggy_clean_font)
    else:
        print(f"\nError: Could not Load Font {proggy_clean_id}\n")


    # create an instance of the window / GUI Window
    window = Main_Window()
    # apply them method `show` to make the "program" show
    window.show()


    # execute the application with `sys`
    sys.exit(app.exec())



if __name__ == '__main__':
    main()
