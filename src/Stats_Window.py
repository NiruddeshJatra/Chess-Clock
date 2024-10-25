import itertools
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import QSoundEffect
from src.Match_History_Window import UiMatchHistoryWindow
import mysql.connector
import sys



class ChessStatisticsBar(QWidget):
    def __init__(self, xPos, yPos, percentage1, percentage2, percentage3, causes):
        super().__init__()
        self.xPos = xPos
        self.yPos = yPos
        self.percentage1 = percentage1
        self.percentage2 = percentage2
        self.percentage3 = percentage3
        self.causes = causes
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        totalWidth = 400
        totalHeight = 10
        
        width1 = int(totalWidth * self.percentage1 / 100)
        width2 = int(totalWidth * self.percentage2 / 100)
        width3 = int(totalWidth * self.percentage3 / 100)
        
        # Draw win portion
        painter.fillRect(self.xPos + 100, self.yPos + 20, width1, totalHeight, Qt.GlobalColor.green)
        
        # Draw draw portion
        painter.fillRect(self.xPos + 100 + width1, self.yPos + 20, width2, totalHeight, Qt.GlobalColor.gray)
        
        # Draw lose portion
        painter.fillRect(self.xPos + 100 + width1 + width2, self.yPos + 20, width3, totalHeight, Qt.GlobalColor.red)
        
        # Draw text labels
        font = QFont("Gill Sans Nova Light", 8)
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(Qt.GlobalColor.black)
        if width1:
            painter.drawText(self.xPos + 105, self.yPos + 45, f"{self.causes[0]} {self.percentage1:.2f}%")
        if width2:
            if width1 and width1 < 110:
                painter.drawText(self.xPos + width1 + 200, self.yPos + 45, f"{self.causes[1]} {self.percentage2:.2f}%")
            elif width1 and width1 > 190:
                painter.drawText(self.xPos + width1 + 50, self.yPos + 45, f"{self.causes[1]} {self.percentage2:.2f}%")
            else:
                painter.drawText(self.xPos + width1 + 110, self.yPos + 45, f"{self.causes[1]} {self.percentage2:.2f}%")
        if width3:
            painter.drawText(self.xPos + 460, self.yPos + 45, f"{self.causes[2]} {self.percentage3:.2f}%")
        
        
        
class UiStatsWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
        self.player = QSoundEffect()
        self.loadBaseUi()
        self.loadDatabase()
        self.showProfileStats()        
        self.showAsWhiteStats()
        self.showAsBlackStats()
        self.showWinStats()
        self.showLoseStats()
        self.showMatchHistory()
        
        
    def loadBaseUi(self):
        url = QUrl.fromLocalFile('Sound/click.wav')
        self.player.setSource(url)
        self.player.play()
        
        self.setWindowTitle("Statistics")
        self.setFixedSize(650, 700)
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
        self.generalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setLayout(self.generalLayout)
        
        
    def loadDatabase(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "password",
            database = "chess_clock",
            auth_plugin="mysql_native_password"
        )
        self.c = self.mydb.cursor()
        
        
    def showProfileStats(self):
        self.c.execute("SELECT Username, Rating, Match_played, Won, Draw, Lost FROM profile WHERE Username = %s", (self.name,))
        self.result = self.c.fetchall()

        self.profileLabel = QLabel("Profile")
        self.profileLabel.setContentsMargins(35, 5, 10, 0)
        font = QFont("Georgia Pro Black", 24)
        font.setBold(True)
        self.profileLabel.setFont(font)
        self.profileLabel.setStyleSheet("")
        self.generalLayout.addWidget(self.profileLabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.headerCol = ["Name", "Rating", "Played", "Won", "Draw", "Lost"]

        for row, col in itertools.product(range(2), range(6)):
            self.label = QLabel()
            self.label.setStyleSheet("""
                    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));
                    color: rgb(0, 34, 0);
                    """)
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            if col == 0:
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
                self.label.setText(str(self.result[0][col]))

            self.gridLayout.addWidget(self.label, row, col)

        self.generalLayout.addLayout(self.gridLayout)
        
        
    def createBar(self, xPos, yPos, cause1, cause2, cause3, causes):
        total = cause1 + cause2 + cause3
        percentage1 = (cause1 / total) * 100
        percentage3 = (cause2 / total) * 100
        percentage2 = 100 - (percentage1 + percentage3)
        
        self.statisticsBar = ChessStatisticsBar(xPos, yPos, percentage1, percentage2, percentage3, causes)
        self.generalLayout.addWidget(self.statisticsBar)
        
        
    def showAsWhiteStats(self):
        self.whiteLabel = QLabel("Played As White")
        self.whiteLabel.setContentsMargins(35, 5, 5, 0)
        font = QFont("Georgia Pro Black", 20)
        font.setBold(True)
        self.whiteLabel.setFont(font)
        self.whiteLabel.setStyleSheet("")
        self.xPos = self.whiteLabel.pos().x()
        self.yPos = self.whiteLabel.pos().y()
        self.generalLayout.addWidget(self.whiteLabel)
        
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE White = %s AND White = Won", (self.name,))
        won = self.c.fetchall()[0][0]
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE White = %s AND Black = Won", (self.name,))
        lost = self.c.fetchall()[0][0]
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE White = %s AND Won = 'Nobody'", (self.name,))
        draw = self.c.fetchall()[0][0]

        if (won + lost + draw) > 0:
            self.createBar(self.xPos, self.yPos, won, lost, draw, ["won", "draw", "lost"])

        
    def showAsBlackStats(self):
        self.blackLabel = QLabel("Played As Black")
        self.blackLabel.setContentsMargins(35, 5, 5, 0)
        font = QFont("Georgia Pro Black", 20)
        font.setBold(True)
        self.blackLabel.setFont(font)
        self.blackLabel.setStyleSheet("")
        self.xPos = self.blackLabel.pos().x()
        self.yPos = self.blackLabel.pos().y()
        self.generalLayout.addWidget(self.blackLabel)
        
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE Black = %s AND Black = Won", (self.name,))
        won = self.c.fetchall()[0][0]
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE Black = %s AND White = Won", (self.name,))
        lost = self.c.fetchall()[0][0]
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE Black = %s AND Won = 'Nobody'", (self.name,))
        draw = self.c.fetchall()[0][0]
        
        if (won + lost + draw) > 0:
            self.createBar(self.xPos, self.yPos, won, lost, draw, ["won", "draw", "lost"])
        
        
    def showWinStats(self):
        self.winLabel = QLabel("Winning Methods")
        self.winLabel.setContentsMargins(35, 5, 5, 0)
        font = QFont("Georgia Pro Black", 20)
        font.setBold(True)
        self.winLabel.setFont(font)
        self.winLabel.setStyleSheet("")
        self.xPos = self.winLabel.pos().x()
        self.yPos = self.winLabel.pos().y()
        self.generalLayout.addWidget(self.winLabel)
        
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE Won = %s AND Cause = 'Resignation'", (self.name,))
        resignation = self.c.fetchall()[0][0]
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE Won = %s AND Cause = 'Checkmate'", (self.name,))
        checkmate = self.c.fetchall()[0][0]
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE Won = %s AND Cause = 'Time'", (self.name,))
        timeout = self.c.fetchall()[0][0]
        
        if (resignation + checkmate + timeout) > 0:
            self.createBar(self.xPos, self.yPos, resignation, timeout, checkmate, ["resignation", "checkmate", "timeout"])
        
        
    def showLoseStats(self):
        self.loseLabel = QLabel("Losing Methods")
        self.loseLabel.setContentsMargins(35, 5, 5, 0)
        font = QFont("Georgia Pro Black", 20)
        font.setBold(True)
        self.loseLabel.setFont(font)
        self.loseLabel.setStyleSheet("")
        self.xPos = self.loseLabel.pos().x()
        self.yPos = self.loseLabel.pos().y()
        self.generalLayout.addWidget(self.loseLabel)
        
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE (White = %s OR Black = %s) AND Won != %s AND Cause = 'Resignation'", (self.name,self.name,self.name,))
        resignation = self.c.fetchall()[0][0]
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE (White = %s OR Black = %s) AND Won != %s AND Cause = 'Checkmate'", (self.name,self.name,self.name,))
        checkmate = self.c.fetchall()[0][0]
        self.c.execute("SELECT COUNT(Match_type) FROM match_history WHERE (White = %s OR Black = %s) AND Won != %s AND Cause = 'Time'", (self.name,self.name,self.name,))
        timeout = self.c.fetchall()[0][0]
        
        if (resignation + checkmate + timeout) > 0:
            self.createBar(self.xPos, self.yPos, resignation, timeout, checkmate, ["resignation", "checkmate", "timeout"])


    def openMatchHistoryWindow(self):
        self.matchHistoryWindow = UiMatchHistoryWindow(self.name)
        self.matchHistoryWindow.show()
        
        
    def showMatchHistory(self):
        self.matchHistoryButton = QPushButton("match history")
        self.matchHistoryButton.setGeometry(QRect(215, 420, 220, 40))
        font = QFont("Algerian", 12)
        self.matchHistoryButton.setFont(font)
        self.matchHistoryButton.setStyleSheet("""
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
        
        self.matchHistoryButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.matchHistoryButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.matchHistoryButton.clicked.connect(self.openMatchHistoryWindow)
        self.generalLayout.addWidget(self.matchHistoryButton)
        
        