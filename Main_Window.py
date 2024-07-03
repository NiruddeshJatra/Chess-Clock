from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import QSoundEffect
import sys
from Player_Window import UiPlayerWindow
from Profile_Window import UiProfileWindow
from Stats_Prompt_Window import UiStatsPromptWindow
from Ranking_Window import UiRankingWindow
from Custom_Prompt_Window import UiCustomPromptWindow



class MyLabel(QLabel):
    def __init__(self, text="", hoverText="", parent=None):
        super().__init__(text, parent)
        self.hoverText = hoverText


    def enterEvent(self, event):
        QToolTip.showText(self.mapToGlobal(self.rect().center()), self.hoverText)
        event.accept()
        
        
    def leaveEvent(self, event):
        QToolTip.hideText()



class UiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.time = 0
        
        self.player = QSoundEffect()
        self.loadBaseUi()
        self.showLogo()
        self.showTopButtons()
        self.buildMatchSelectionBox()
        self.showPlayButton()
        
        
    def loadBaseUi(self):
        url = QUrl.fromLocalFile("Sound\welcome.wav")
        self.player.setSource(url)
        self.player.play()
        
        self.setWindowTitle("Chess Clock")
        self.setFixedSize(515, 260)
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/chess-clock.svg"))
        self.setWindowIcon(icon)
        self.setStyleSheet("""
			background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));
			color: rgb(0, 34, 0);
		""")

        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet("")
        self.setCentralWidget(self.centralwidget)
        
        
    def showLogo(self):
        self.logo = MyLabel(parent=self.centralwidget)
        self.logo.setGeometry(QRect(10, 10, 291, 91))
        self.logo.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.logo.setStyleSheet("background-color: transparent;")
        self.logo.setFrameShape(QFrame.Shape.NoFrame)
        self.logo.setPixmap(QPixmap("Icons/vector/default.svg"))
        
        
    def showTopButtons(self):
        self.profile = MyLabel(parent=self.centralwidget)
        self.profile.setGeometry(QRect(340, 40, 32, 32))
        self.profile.setStyleSheet("background-color: transparent;")
        self.profile.setFrameShape(QFrame.Shape.NoFrame)
        self.profile.setPixmap(QPixmap("Icons/user_11144968.png"))
        self.profile.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.profile.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.profile.setScaledContents(True)
        self.profile.mousePressEvent = lambda event: self.openProfileWindow()
        self.profile.setToolTip("Create Profile")

        self.stats = MyLabel(parent=self.centralwidget)
        self.stats.setGeometry(QRect(390, 40, 32, 32))
        self.stats.setStyleSheet("background-color: transparent;")
        self.stats.setPixmap(QPixmap("Icons/vehicle_10883158.png"))
        self.stats.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.stats.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.stats.setScaledContents(True)
        self.stats.mousePressEvent = lambda event: self.openstatsWindow()
        self.stats.setToolTip("Show Statistics")

        self.ranking = MyLabel(parent=self.centralwidget)
        self.ranking.setGeometry(QRect(440, 40, 32, 32))
        self.ranking.setStyleSheet("background-color: transparent;")
        self.ranking.setPixmap(QPixmap("Icons/chart-bars_7268541.png"))
        self.ranking.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ranking.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.ranking.setScaledContents(True)
        self.ranking.mousePressEvent = lambda event: self.openRankingWindow()
        self.ranking.setToolTip("Ranking")


    def buildMatchSelectionBox(self):
        self.matchType = QComboBox(parent=self.centralwidget)
        self.matchType.setGeometry(QRect(90, 120, 350, 50))
        self.matchType.setFixedSize(350, 50)
        font = QFont("Consolas", 18)
        self.matchType.setFont(font)
        self.matchType.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.matchType.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.matchType.setStyleSheet("""
			border: 1px solid #98e820;
			border-radius: 10px;
			color: rgb(26, 35, 30)
		""")
        
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("Icons/bullet.png"))
        self.matchType.addItem(icon1, " Bullet: 1 Min")
        self.matchType.addItem(icon1, " Bullet: 2|1 Min")
        
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("Icons/lightning.png"))
        self.matchType.addItem(icon2, " Blitz: 3|2 Min")
        self.matchType.addItem(icon2, " Blitz: 5 Min")
        
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("Icons/rapid.png"))
        self.matchType.addItem(icon3, " Rapid: 10 Min")
        self.matchType.addItem(icon3, " Rapid: 15|10 Min")
        self.matchType.addItem(icon3, " Custom")
        
        self.matchType.activated.connect(self.openPlayerWindow)
        
        
    def showPlayButton(self):
        self.playButton = QPushButton("PLAY", parent=self.centralwidget)
        self.playButton.setGeometry(QRect(90, 180, 350, 50))
        self.playButton.setFixedSize(350, 50)
        font = QFont("Algerian", 20)
        self.playButton.setFont(font)
        self.playButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.playButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.playButton.setStyleSheet("""
			QPushButton {
				background-color:rgb(169, 255, 8);
				border-radius: 10px;
				padding: 10px 20px;
				color: rgb(25, 33, 19);
			}
			QPushButton:hover {
				background-color: #ffff00;
				color: rgb(0, 0, 0);
			}
		""")

        self.shortcut = QShortcut(Qt.Key.Key_Return, self)
        self.shortcut.activated.connect(self.playButton.click)
        self.playButton.clicked.connect(self.openPlayerWindow)


    def updateTime(self, timeEntered):
        if self.matchType.currentIndex() == 1:
            self.time = 120
        elif self.matchType.currentIndex() == 2:
            self.time = 180
        elif self.matchType.currentIndex() == 3:
            self.time = 300
        elif self.matchType.currentIndex() == 4:
            self.time = 600
        elif self.matchType.currentIndex() == 5:
            self.time = 900
        elif self.matchType.currentIndex() == 6:
            self.time = timeEntered * 60
        else:
            self.time = 60
        

    def openProfileWindow(self):
        self.profileWindow = UiProfileWindow()
        self.profileWindow.show()
        
        
    def openstatsWindow(self):
        self.statsWindow = UiStatsPromptWindow()
        self.statsWindow.show()
        
        
    def openRankingWindow(self):
        self.rankingWindow = UiRankingWindow()
        self.rankingWindow.show()
        
        
    def openCustomWindow(self):
        self.customTimeWindow = UiCustomPromptWindow()
        self.customTimeWindow.timeEntered.connect(self.updateTime)
        self.customTimeWindow.show()


    def openPlayerWindow(self):
        if self.matchType.currentIndex() == 6:
            self.openCustomWindow()
        else:
            self.updateTime(0)

        if self.time:
            if self.matchType.currentIndex() == 6:
                self.customTimeWindow.hide()
            self.playerWindow = UiPlayerWindow(self.time)
            self.playerWindow.show()            