import itertools
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import QSoundEffect
import sys
import mysql.connector



class UiRankingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.player = QSoundEffect()
        self.loadBaseUi()
        self.loadDatabase()
        self.loadRanking()
        
    
    def loadBaseUi(self):
        url = QUrl.fromLocalFile('Sound\click.wav')
        self.player.setSource(url)
        self.player.play()
        
        self.setWindowTitle("Rankings")
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/chess-clock.svg"))
        self.setWindowIcon(icon)
        self.setStyleSheet("""
			background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));
			color: rgb(0, 34, 0);
			"""
        )
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        
        
    def loadDatabase(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "password",
            database = "chess_clock",
        )
        self.c = self.mydb.cursor()
        
        
    def loadRanking(self):
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.c.execute("SELECT Username, Rating, Won, Draw, Lost FROM profile ORDER BY Rating DESC LIMIT 10")
        self.result = self.c.fetchall()

        self.rankingCol = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.headerCol = ["Ranking", "Name", "Rating", "Won", "Draw", "Lost"]

        i = 0
        for row, col in itertools.product(range(len(self.result)+1), range(6)):
            self.label = QLabel()
            self.label.setStyleSheet("""
                    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));
                    color: rgb(0, 34, 0);
                    """)
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            if col == 1:
                self.label.setFixedSize(150, 35)
            else:
                self.label.setFixedSize(100, 35)

            if row == 0:
                self.label.setText(self.headerCol[col])
                font = QFont("Castellar", 12)
                font.setBold(True)
                self.label.setFont(font)
            else:
                font = QFont("Gill Sans Nova Light", 12)
                font.setBold(True)
                self.label.setFont(font)
                if col == 0:
                    self.label.setText(self.rankingCol[i])
                    i += 1
                else:
                    self.label.setText(str(self.result[row-1][col-1]))

            self.gridLayout.addWidget(self.label, row, col)

        self.c.close()
        self.mydb.close()

        self.setFixedSize(650, 35*(len(self.result) + 1))
        
        
