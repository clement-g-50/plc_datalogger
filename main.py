import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from gui.ui_interface import Ui_MainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MyWindow()
    fenetre.show()
    sys.exit(app.exec())