from Main_Window import UiMainWindow
from PyQt6.QtWidgets import *
import sys



app = QApplication(sys.argv)
mainWindow = UiMainWindow()
mainWindow.show()
sys.exit(app.exec())