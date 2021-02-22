import sys
from console import Ui_Console
from PyQt5 import QtWidgets
import pygame

import draw
from generation import processes

def main():
    app = QtWidgets.QApplication(sys.argv)
    Console = QtWidgets.QMainWindow()
    ui = Ui_Console()
    ui.setupUi(Console)
    Console.show()
    sys.exit(app.exec_())
    pygame.quit() # quit pygame

    # only one process but I want to bypass error when there are 0 processes
    for proc in generation.processes:
        proc.join()

if __name__ == "__main__":
    pygame.init() # initialize pygame
    main()