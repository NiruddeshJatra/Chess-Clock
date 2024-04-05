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
        
        self.c.close()
        self.mydb.close()
                
        self.setFixedSize(880, 35*(len(self.result) + 1))
