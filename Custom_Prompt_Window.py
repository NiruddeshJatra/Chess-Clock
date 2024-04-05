from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from Stats_Window import UiStatsWindow
import sys


class UiCustomPromptWindow(QMainWindow):
    timeEntered = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setObjectName("statsWindow")
        self.setWindowTitle("Custom Game")
        self.setFixedSize(315, 150)
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/chess-clock.svg"))
        self.setWindowIcon(icon)
        self.setStyleSheet("""
            background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));
			color: rgb(0, 34, 0);
			"""
        )

        self.centralwidget = QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.timeLabel = QLabel("Enter Time in Minutes", parent=self.widget)
        self.timeLabel.setContentsMargins(15, 5, 10, 0)
        font = QFont("Georgia Pro Black", 16)
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("")
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout.addWidget(self.timeLabel)

        self.time = QLineEdit(parent=self.widget)
        self.time.setContentsMargins(15, 0, 10, 10)
        self.time.setFixedSize(290, 45)
        font = QFont("Georgia Pro", 12)
        self.time.setFont(font)
        self.time.setStyleSheet("""
            background-color:rgb(162, 241, 120);
            border: 1px solid rgb(85, 255, 127);
            padding: 6px 8px;
            border-radius: 5px;
            color: rgb(25, 33, 19);
            """
        )
        self.time.setObjectName("time")
        self.time.returnPressed.connect(self.submitTime)
        self.verticalLayout.addWidget(self.time)
        
        self.submitButton = QPushButton("submit", parent=self.centralwidget)
        self.submitButton.setFixedSize(280, 45)
        font = QFont("Algerian", 18)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("""
			QPushButton {
				background-color: rgb(169, 255, 8);
				border: 1px solid rgb(85, 255, 127);
				border-radius: 10px;
				padding: 10px 20px;
                margin-left: 15px;
				color: rgb(25, 33, 19);
			}
			QPushButton:hover {
				background-color: #ffff00;
				color: rgb(0, 0, 0);
			}
			"""
        )
        self.submitButton.setObjectName("submitButton")
        self.submitButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.submitButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.submitButton.clicked.connect(self.submitTime)
        self.verticalLayout.addWidget(self.submitButton)

        
    def submitTime(self):
        timeEntered = int(self.time.text())
        self.timeEntered.emit(timeEntered)
        self.hide()