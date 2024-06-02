from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
import mysql.connector



class UiMatchHistoryWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
        self.loadBaseUi()
        self.loadDatabase()
        self.loadHistory()
        self.showRecent()
        self.showOlder()
        
    def loadBaseUi(self):
        self.setWindowTitle("Match History")
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
        self.generalLayout = QVBoxLayout(self.centralwidget)
        self.generalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setLayout(self.generalLayout)
        
        
    def loadDatabase(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "password",
            database = "chess_clock",
        )
        self.c = self.mydb.cursor()
        
        
    def loadHistory(self):
        self.c.execute("SELECT Match_date, White, White_rating, Black, Black_rating, Match_type, Won, Cause, Moves FROM match_history WHERE White = %s OR Black = %s ORDER BY Match_date DESC LIMIT 10", (self.name, self.name,))
        self.result = self.c.fetchall()
        
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        
        self.headerCol = ["Date", "White", "Rating", "Black", "Rating", "Type", "Won", "Cause", "Moves"]
        
        for row in range(len(self.result)+1):
            for col in range(9):
                self.label = QLabel()
                self.label.setStyleSheet("""
                    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));
                    color: rgb(0, 34, 0);
                    """)
                self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                if col in [2,4,5,7,8]:
                    self.label.setFixedSize(80, 35)
                else:
                    self.label.setFixedSize(120, 35)
                    
                if row == 0:
                    self.label.setText(self.headerCol[col])
                    font = QFont("Castellar", 12)
                    font.setBold(True)
                    self.label.setFont(font)
                else:
                    font = QFont("Gill Sans Nova Light", 12)
                    font.setBold(True)
                    self.label.setFont(font)
                    self.label.setText(str(self.result[row-1][col]))
                    
                self.gridLayout.addWidget(self.label, row, col)
                self.generalLayout.addLayout(self.gridLayout)
        
        self.c.close()
        self.mydb.close()
                
        self.setFixedSize(880, 35*(len(self.result) + 1) + 100)
        
        
    def showRecent(self):
        self.recentButton = QPushButton("Recent")
        self.recentButton.setGeometry(QRect(215, 35*(len(self.result) + 1) + 50, 220, 40))
        font = QFont("Algerian", 12)
        self.recentButton.setFont(font)
        self.recentButton.setStyleSheet("""
			QPushButton {
				background-color:rgb(169, 255, 8);
				border: 1px solid rgb(85, 255, 127);
				border-radius: 10px;
                margin-left: 220px;
                margin-right: 220px;
                margin-bottom: 25px;
				padding: 10px 20px;
				color: rgb(25, 33, 19);
			}
			QPushButton:hover {
				background-color: #ffff00;
				color: rgb(0, 0, 0);
			}
        """)
        
        self.recentButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.recentButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.recentButton.clicked.connect(self.loadHistory)
        self.generalLayout.addWidget(self.recentButton)
        
        
    def showOlder(self):
        self.olderButton = QPushButton("Recent")
        self.olderButton.setGeometry(QRect(655, 35*(len(self.result) + 1) + 50, 220, 40))
        font = QFont("Algerian", 12)
        self.olderButton.setFont(font)
        self.olderButton.setStyleSheet("""
			QPushButton {
				background-color:rgb(169, 255, 8);
				border: 1px solid rgb(85, 255, 127);
				border-radius: 10px;
                margin-left: 220px;
                margin-right: 220px;
                margin-bottom: 25px;
				padding: 10px 20px;
				color: rgb(25, 33, 19);
			}
			QPushButton:hover {
				background-color: #ffff00;
				color: rgb(0, 0, 0);
			}
        """)
        
        self.olderButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.olderButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.olderButton.clicked.connect(self.loadHistory)
        self.generalLayout.addWidget(self.olderButton)
