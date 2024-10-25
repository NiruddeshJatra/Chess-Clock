from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import QSoundEffect
import sys
from src.Congratulation_Window import UiCongratulationWindow
import mysql.connector



class MyLabel(QLabel):
    def __init__(self, text="", hoverText="", parent=None):
        super().__init__(text, parent)
        self.hoverText = hoverText

    def enterEvent(self, event):
        QToolTip.showText(self.mapToGlobal(self.rect().center()), self.hoverText)
        event.accept()
        
    def leaveEvent(self, event):
        QToolTip.hideText()



class UiTimerWindow(QMainWindow):
    def __init__(self, time, name1, name2):
        super().__init__()
        self.count = 0
        self.time = time
        self.white = name1
        self.black = name2
        self.matchType = ""
        self.date = QDate.currentDate()
        self.timerInterval = 1000
        self.player1RemainingTime = self.time
        self.player2RemainingTime = self.time
        self.player = QSoundEffect()
        
        self.loadBaseUi()
        self.showTimerDisplay()
        self.buildToggleButton()
        self.showBottomButtons()
        
        
    def loadBaseUi(self):
        self.playSound('Sound/level_up.wav')
        self.setWindowTitle("Timer Window")
        self.setFixedSize(640, 480)
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/chess-clock.svg"))
        self.setWindowIcon(icon)
        self.setStyleSheet("""
            background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));
            color: rgb(0, 34, 0);
        """)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        
        
    def showTimerDisplay(self):
        self.player1Name = QLabel(self.white.upper(), parent=self.centralwidget)
        self.player1Name.setGeometry(QRect(100, 30, 200, 41))
        font = QFont("Castellar", 23)
        font.setBold(True)
        self.player1Name.setFont(font)
        self.player1Name.setStyleSheet("background-color: transparent;")
        
        self.player2Name = QLabel(self.black.upper(), parent=self.centralwidget)
        self.player2Name.setGeometry(QRect(400, 30, 200, 41))
        font = QFont("Castellar", 23)
        font.setBold(True)
        self.player2Name.setFont(font)
        self.player2Name.setStyleSheet("background-color: transparent;")
        
        minutes = self.time // 60
        seconds = self.time % 60
        timeStr = f"{minutes:02}:{seconds:02}"
        
        self.player1Time = QLCDNumber(parent=self.centralwidget)
        self.player1Time.setGeometry(QRect(40, 80, 261, 201))
        currentFont = self.player1Time.font()
        font = QFont(currentFont)
        font.setPointSize(20)
        self.player1Time.setFont(font)
        self.player1Time.setStyleSheet("""
            background-color: #00813e;
            color:  rgb(230, 234, 230);
            border-radius: 5px;
            padding: 10px 20px;
        """)
        
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.updateTimer1)
        self.player1Time.display(timeStr)
        
        self.player2Time = QLCDNumber(parent=self.centralwidget)
        self.player2Time.setGeometry(QRect(340, 80, 261, 201))
        currentFont = self.player1Time.font()
        font = QFont(currentFont)
        font.setPointSize(20)
        self.player2Time.setFont(font)
        self.player2Time.setStyleSheet("""
            background-color: #00813e;
            color:  rgb(230, 234, 230);
            border-radius: 5px;
            padding: 10px 20px;
        """)
        
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.updateTimer2)
        self.player2Time.display(timeStr)
        
        self.player1Move = QLabel("Moves: 0", parent=self.centralwidget)
        self.player1Move.setGeometry(QRect(50, 250, 81, 16))
        font = QFont("Segoe Pro Display SemiLight", 12)
        self.player1Move.setFont(font)
        self.player1Move.setStyleSheet("background-color: transparent; color: white;")
        self.player1Move.setObjectName("player1Move")
        
        self.player2Move = QLabel("Moves: 0", parent=self.centralwidget)
        self.player2Move.setGeometry(QRect(350, 250, 81, 16))
        self.player2Move.setFont(font)
        self.player2Move.setStyleSheet("background-color: transparent; color: white;")
        self.player2Move.setObjectName("player2Move")
        
        
    def buildToggleButton(self):
        self.pushButton = QPushButton("W H I T E' S  M O V E", parent=self.centralwidget)
        self.pushButton.setGeometry(QRect(120, 330, 401, 71))
        font = QFont("Sitka", 18)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QSize(30, 16))
        self.shortcut = QShortcut(Qt.Key.Key_Space, self)
        self.shortcut.activated.connect(self.pushButton.click)
        self.pushButton.setStyleSheet("""
			QPushButton {
				background-color: white;
                border: 1px solid rgb(10, 10, 10);
				border-radius: 10px;
				padding: 10px 20px;
				color: black;
			}
			"""
        )
        self.pushButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pushButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.pushButton.clicked.connect(self.toggleTimer)
        
        
    def showBottomButtons(self):
        self.resignButton = MyLabel(parent=self.centralwidget)
        self.resignButton.setGeometry(QRect(250, 430, 32, 32))
        self.resignButton.setStyleSheet("background-color: transparent;")
        self.resignButton.setPixmap(QPixmap("Icons/loser.png"))
        self.resignButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.resignButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.resignButton.setScaledContents(True)
        self.resignButton.mousePressEvent = lambda event: self.resign()
        self.resignButton.setToolTip("Resign") 
        
        self.drawButton = MyLabel(parent=self.centralwidget)
        self.drawButton.setGeometry(QRect(310, 430, 32, 32))
        self.drawButton.setStyleSheet("background-color: transparent;")
        self.drawButton.setPixmap(QPixmap("Icons/draw.png"))
        self.drawButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.drawButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.drawButton.setScaledContents(True)
        self.drawButton.mousePressEvent = lambda event: self.draw()
        self.drawButton.setToolTip("Draw")
        
        self.checkmateButton = MyLabel(parent=self.centralwidget)
        self.checkmateButton.setGeometry(QRect(370, 430, 31, 31))
        self.checkmateButton.setStyleSheet("background-color: transparent;")
        self.checkmateButton.setPixmap(QPixmap("Icons/chess.png"))
        self.checkmateButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.checkmateButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.checkmateButton.setScaledContents(True)
        self.checkmateButton.mousePressEvent = lambda event: self.checkmate()
        self.checkmateButton.setToolTip("Checkmate")
        
        
    def updateTimer1(self):
        self.updateBorder()
        self.player1RemainingTime -= 1
        minutes, seconds = divmod(self.player1RemainingTime, 60)
        timeStr = f"{minutes:02}:{seconds:02}"
        self.player1Time.display(timeStr)

        if (self.time >= 600 and self.player1RemainingTime == 120) or (self.time >= 180 and self.player1RemainingTime == 60) or (self.time >= 60 and self.player1RemainingTime == 20):
            self.playSound('Sound/low_on_time.wav')
        
        if (self.time >= 600 and self.player1RemainingTime == 20) or (self.time >= 180 and self.player1RemainingTime == 10) or (self.time >= 60 and self.player1RemainingTime == 5):
            self.playSound('Sound/last_warning.wav')
            
        if self.player1RemainingTime < 0:
            self.playSound('Sound/game_over.wav')
            self.timer1.stop()
            self.winner = self.black
            self.winningMethod = "Time"
            self.openCongratulationWindow()
        
        
    def updateTimer2(self):
        self.updateBorder()
        self.player2RemainingTime -= 1
        minutes, seconds = divmod(self.player2RemainingTime, 60)
        timeStr = f"{minutes:02}:{seconds:02}"
        self.player2Time.display(timeStr)

        if (self.time >= 600 and self.player2RemainingTime == 120) or (self.time >= 180 and self.player2RemainingTime == 60) or (self.time >= 60 and self.player2RemainingTime == 20):
            self.playSound('Sound/low_on_time.wav')
            
        if (self.time >= 600 and self.player2RemainingTime == 20) or (self.time >= 180 and self.player2RemainingTime == 10) or (self.time >= 60 and self.player2RemainingTime == 5):
            self.playSound('Sound/last_warning.wav')
            
        if self.player2RemainingTime < 0:
            self.playSound('Sound/game_over.wav')
            self.timer2.stop()
            self.winner = self.white
            self.winningMethod = "Time"
            self.openCongratulationWindow()
        
        
    def toggleTimer(self):
        if self.count % 2 == 0:
            if self.time == 120:
                self.player1RemainingTime += 1
            elif self.time == 180:
                self.player1RemainingTime += 2
            elif self.time == 900:
                self.player1RemainingTime += 10

            minutes, seconds = divmod(self.player1RemainingTime, 60)
            timeStr = f"{minutes:02}:{seconds:02}"
            self.player1Time.display(timeStr)

            self.timer2.start(self.timerInterval)
            self.timer1.stop()
            self.player1Move.setText(f"Moves: {1+self.count//2}")
            
            self.playSound('Sound/toggle.wav')

            self.pushButton.setText("B L A C K' S  M O V E")
            self.pushButton.setStyleSheet("""
                QPushButton {
                    background-color: black;
                    border: 2px solid white;
                    border-radius: 10px;
                    padding: 10px 20px;
                    color: white;
                    }
			""")

        else:
            if self.time == 120:
                self.player2RemainingTime += 1
            elif self.time == 180:
                self.player2RemainingTime += 2
            elif self.time == 900:
                self.player2RemainingTime += 10

            minutes, seconds = divmod(self.player2RemainingTime, 60)
            timeStr = f"{minutes:02}:{seconds:02}"
            self.player2Time.display(timeStr)

            self.timer1.start(self.timerInterval)
            self.timer2.stop()
            self.player2Move.setText(f"Moves: {1+self.count//2}")
            
            self.playSound('Sound/toggle.wav')

            self.pushButton.setText("W H I T E' S  M O V E")
            self.pushButton.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    border: 1px solid rgb(10, 10, 10);
                    border-radius: 10px;
                    padding: 10px 20px;
                    color: black;
                }
			""")

        self.count += 1
        self.updateBorder()


    def playSound(self, sound_file):
        url = QUrl.fromLocalFile(sound_file)
        self.player.setSource(url)
        self.player.play()
        
        
    def updateBorder(self):
        if self.count % 2 == 0:
            if (self.time >= 600 and self.player1RemainingTime <= 120) or (self.time >= 180 and self.player1RemainingTime <= 60) or (self.time <= 60 and self.player1RemainingTime <= 20):
                    self.player1Time.setStyleSheet("""
                    background-color: #00813e;
                    border: 1px solid red;
                    color:  #ffff00;
                """)
            else:
                self.player1Time.setStyleSheet("""
                    background-color: #00813e;
                    border: 2px solid rgb(85, 255, 127);
                    color:  #ffff00;
                """)

            self.player2Time.setStyleSheet("""
                background-color: #00813e;
                color:  #006800;
            """)
            
        else:
            if (self.time >= 600 and self.player2RemainingTime <= 120) or (self.time >= 180 and self.player2RemainingTime <= 60) or (self.time >= 60 and self.player2RemainingTime <= 20):
                self.player2Time.setStyleSheet("""
                background-color: #00813e;
                border: 1px solid red;
                color: #ffff00;
            """)
            else:
                self.player2Time.setStyleSheet("""
                    background-color: #00813e;
                    border: 2px solid rgb(85, 255, 127);
                    color: #ffff00;
                """)
            
            self.player1Time.setStyleSheet("""
                background-color: #00813e;
                color:  #006800;
            """
        )
                
                
    def loadDatabase(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "password",
            database = "chess_clock",
            auth_plugin="mysql_native_password"
        )
        self.c = self.mydb.cursor()
        
        
    def resign(self):
        self.winningMethod = "Resignation"
        self.winner = self.white if self.count % 2 == 0 else self.black
        self.timer1.stop()
        self.timer2.stop()
        self.openCongratulationWindow()
        
        
    def checkmate(self):
        self.winningMethod = "Checkmate"
        self.winner = self.white if self.count % 2 == 0 else self.black
        self.timer1.stop()
        self.timer2.stop()
        self.openCongratulationWindow()
        
        
    def draw(self):
        self.winningMethod = "Draw"
        self.winner = "Nobody"
        
        self.timer1.stop()    
        self.timer2.stop()
        self.openCongratulationWindow()
        
        
    def openCongratulationWindow(self):
        self.insertMatchHistory()    
        self.congratulationWindow = UiCongratulationWindow(self.winner, self.winningMethod)
        self.hide()
        self.congratulationWindow.show()
        
        
    def insertMatchHistory(self):
        self.loadDatabase()
        
        self.c.execute("SELECT Rating FROM profile WHERE Username = %s", (self.white,))
        result = self.c.fetchone()
        self.whiteRating = result[0]
        
        self.c.execute("SELECT Rating FROM profile WHERE Username = %s", (self.black,))
        result = self.c.fetchone()
        self.blackRating = result[0]
        
        self.updateRating()
        
        self.c.execute("""
            INSERT INTO match_history(White, White_rating, Black, Black_rating, Match_type, Won, Cause, Moves, Match_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (self.white.lower(), self.whiteRating, self.black.lower(), self.blackRating, self.matchType, self.winner, self.winningMethod, self.count//2, self.date.toString("yyyy-MM-dd"),))
        
        self.mydb.commit()
        self.mydb.close()
        
        
    def updateRating(self):
        self.calculateMatchPoint()
        ratingDiff = abs(self.whiteRating - self.blackRating)
        self.bonusPoint = ratingDiff // 30
        if self.winner == self.white:
            self.c.execute("UPDATE profile SET Match_played = Match_played + 1, Won = Won + 1 WHERE Username = %s", (self.white,))
            self.mydb.commit()
            self.c.execute("UPDATE profile SET Match_played = Match_played + 1, Lost = Lost + 1 WHERE Username = %s", (self.black,))
            self.mydb.commit()
        
            if self.whiteRating > self.blackRating:
                self.whiteRating += (self.matchPoint - self.bonusPoint)
                self.blackRating -= (self.matchPoint - self.bonusPoint)
            else:
                self.whiteRating += (self.matchPoint + self.bonusPoint)
                self.blackRating -= (self.matchPoint + self.bonusPoint)
                
        elif self.winner == self.black:
            self.c.execute("UPDATE profile SET Match_played = Match_played + 1, Won = Won + 1 WHERE Username = %s", (self.black,))
            self.mydb.commit()
            self.c.execute("UPDATE profile SET Match_played = Match_played + 1, Lost = Lost + 1 WHERE Username = %s", (self.white,))
            self.mydb.commit()
            
            if self.whiteRating > self.blackRating:
                self.whiteRating -= (self.matchPoint + self.bonusPoint)
                self.blackRating += (self.matchPoint + self.bonusPoint)
            else:
                self.whiteRating -= (self.matchPoint - self.bonusPoint)
                self.blackRating += (self.matchPoint - self.bonusPoint)
                
        else:
            self.c.execute("UPDATE profile SET Match_played = Match_played + 1, Draw = Draw + 1 WHERE Username = %s", (self.white,))
            self.mydb.commit()
            self.c.execute("UPDATE profile SET Match_played = Match_played + 1, Draw = Draw + 1 WHERE Username = %s", (self.black,))
            self.mydb.commit()
            
            if self.whiteRating > self.blackRating:
                self.whiteRating -= self.bonusPoint
                self.blackRating += self.bonusPoint
            else:
                self.whiteRating += self.bonusPoint
                self.blackRating -= self.bonusPoint
        
        self.c.execute("UPDATE profile SET Rating = %s WHERE Username = %s", (self.whiteRating, self.white,))
        self.mydb.commit()
        self.c.execute("UPDATE profile SET Rating = %s WHERE Username = %s", (self.blackRating, self.black,))
        self.mydb.commit()
        
        
    def calculateMatchPoint(self):
        if self.time <= 120:
            self.matchType = "Bullet"
            self.matchPoint = 20
        elif self.time <= 300:
            self.matchType = "Blitz"
            self.matchPoint = 15
        elif self.time <= 900:
            self.matchType = "Rapid"
            self.matchPoint = 10
        else:
            self.matchType = "Custom"
            self.matchPoint = 5
