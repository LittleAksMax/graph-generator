import sys
from console import Ui_Console
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Console = QtWidgets.QMainWindow()
    ui = Ui_Console()
    ui.setupUi(Console)
    Console.show()
    sys.exit(app.exec_())