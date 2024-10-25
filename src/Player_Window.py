from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import QSoundEffect
import sys
from src.Timer_Window import UiTimerWindow
import mysql.connector



class UiPlayerWindow(QMainWindow):
    def __init__(self, time):
        super().__init__()
        self.time = time
        
        self.player = QSoundEffect()
        self.loadBaseUi()
        self.enterUsernames()
        self.showStartButton()
        
        
    def loadBaseUi(self):
        url = QUrl.fromLocalFile('Sound/level_up.wav')
        self.player.setSource(url)
        self.player.play()
        
        self.setWindowTitle("Entry Player Name")
        self.setFixedSize(315, 250)
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/chess-clock.svg"))
        self.setWindowIcon(icon)
        self.setStyleSheet("""
            background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));
			color: rgb(0, 34, 0);
		""")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.generalLayout = QVBoxLayout(self.centralwidget)


    def enterUsernames(self):
        self.player1Label = QLabel("Player 1 - White")
        self.player1Label.setContentsMargins(15, 5, 10, 0)
        font = QFont("Georgia Pro Black", 16)
        font.setBold(True)
        self.player1Label.setFont(font)
        self.generalLayout.addWidget(self.player1Label)

        self.player1Name = QLineEdit()
        self.player1Name.setContentsMargins(15, 0, 10, 10)
        self.player1Name.setFixedSize(290, 45)
        font = QFont("Georgia Pro", 12)
        font.setItalic(True)
        self.player1Name.setFont(font)
        self.player1Name.setStyleSheet("""
            background-color:rgb(162, 241, 120);
            border: 1px solid rgb(85, 255, 127);
            padding: 6px 8px;
            border-radius: 5px;
            color: rgb(25, 33, 19);
        """)
        self.generalLayout.addWidget(self.player1Name)

        self.player2Label = QLabel("Player 2 - Black")
        self.player2Label.setContentsMargins(15, 0, 10, 0)
        font = QFont("Georgia Pro Black", 16)
        font.setBold(True)
        self.player2Label.setFont(font)
        self.generalLayout.addWidget(self.player2Label)

        self.player2Name = QLineEdit()
        self.player2Name.setContentsMargins(15, 0, 10, 10)
        self.player2Name.setFixedSize(290, 45)
        font = QFont("Georgia Pro", 12)
        font.setItalic(True)
        self.player2Name.setFont(font)
        self.player2Name.setStyleSheet("""
            background-color:rgb(162, 241, 120);
            border: 1px solid rgb(85, 255, 127);
            padding: 6px 8px;
            border-radius: 5px;
            color: rgb(25, 33, 19);
        """)
        self.player1Name.returnPressed.connect(self.player2Name.setFocus)
        self.player2Name.returnPressed.connect(self.openTimerWindow)
        self.generalLayout.addWidget(self.player2Name)


    def showStartButton(self):
        self.startButton = QPushButton("START")
        self.startButton.setFixedSize(280, 45)
        font = QFont("Algerian", 18)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("""
			QPushButton {
				background-color:rgb(169, 255, 8);
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
		""")

        self.startButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.startButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.startButton.clicked.connect(self.openTimerWindow)
        self.generalLayout.addWidget(self.startButton)
        

    def loadDatabase(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "password",
            database = "chess_clock",
            auth_plugin="mysql_native_password"
        )
        self.c = self.mydb.cursor()
            
            
    def openTimerWindow(self):  # sourcery skip: extract-method
        if self.player1Name.text() == "":
            self.player1Name.setStyleSheet("""
                background-color:rgb(162, 241, 120);
                border: 1px solid red;
                padding: 6px 8px;
                border-radius: 5px;
                color: rgb(25, 33, 19);
            """)
            
        if self.player2Name.text() == "":
            self.player2Name.setStyleSheet("""
                background-color:rgb(162, 241, 120);
                border: 1px solid red;
                padding: 6px 8px;
                border-radius: 5px;
                color: rgb(25, 33, 19);
            """)
            
        if self.player1Name.text() != "" and self.player2Name.text() != "":
            self.loadDatabase()
            
            self.c.execute("SELECT Username FROM profile")
            profiles = [profile[0] for profile in self.c.fetchall()]
            
            self.name1 = self.player1Name.text().lower()
            self.name2 = self.player2Name.text().lower()
            
            if self.name1 not in profiles:
                self.player1Name.setStyleSheet("""
                    background-color:rgb(162, 241, 120);
                    border: 1px solid red;
                    padding: 6px 8px;
                    border-radius: 5px;
                    color: rgb(25, 33, 19);
                """)
                
                self.showWarningMessageBox("1")
            
            elif self.name2 not in profiles:
                self.player2Name.setStyleSheet("""
                    background-color:rgb(162, 241, 120);
                    border: 1px solid red;
                    padding: 6px 8px;
                    border-radius: 5px;
                    color: rgb(25, 33, 19);
                """)
                
                self.showWarningMessageBox("2")
                
            elif self.name2 == self.name1:
                self.player1Name.setStyleSheet("""
                    background-color:rgb(162, 241, 120);
                    border: 1px solid red;
                    padding: 6px 8px;
                    border-radius: 5px;
                    color: rgb(25, 33, 19);
                """)
                
                self.player2Name.setStyleSheet("""
                    background-color:rgb(162, 241, 120);
                    border: 1px solid red;
                    padding: 6px 8px;
                    border-radius: 5px;
                    color: rgb(25, 33, 19);
                """)
                
                self.showWarningMessageBox("3")
                
            else:
                self.mydb.close()
                self.timerWindow = UiTimerWindow(self.time, self.name1, self.name2)
                self.hide()
                self.timerWindow.show()
                
                
    def showWarningMessageBox(self, playerNo):
        msg = QMessageBox()
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/chess-clock.svg"))
        msg.setWindowIcon(icon)
        font = QFont("Sitka", 20)
        font.setBold(True)
        msg.setFont(font)

        if playerNo == "3":
            msg.setWindowTitle("Invalid!!!")
            msg.setText(f"You can't play with yourself, fool!!\nEnter different Usernames.")
        else:
            msg.setWindowTitle("Not Registered!!!")
            msg.setText(f"Player {playerNo} doesn't exist in the database!\nCreate a Profile first.")

        msg.exec()

