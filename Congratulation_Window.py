from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys



class UiCongratulationWindow(QMainWindow):
    def __init__(self, winner, winningMethod):
        super().__init__()
        
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        self.winner = winner
        
        if winningMethod == "Time":
            self.winningMethod = "on Time"
        elif winningMethod == "Checkmate":
            self.winningMethod = "by Checkmate"
        elif winningMethod == "Resignation":
            self.winningMethod = "by Resignation"
        else:
            self.winningMethod = "It's a Draw!"

        self.loadBaseUi()
        self.showCongrats()
        
        
    def loadBaseUi(self):
        url = QUrl.fromLocalFile('Sound\winner.wav')
        self.player.setSource(url)
        self.player.play()
        
        self.setWindowTitle("Congratulations!")
        self.setFixedSize(350, 230)
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/chess-clock.svg"))
        self.setWindowIcon(icon)
        self.setStyleSheet("""
            background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));
            color: rgb(253, 255, 210);
            """
        )
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        
        
    def showCongrats(self):
        self.label = QLabel(parent=self.centralwidget)
        font = QFont("Sitka", 30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText(f"Congratulations!\n{self.winner} Won\n{self.winningMethod}")
        self.label.setStyleSheet("background-color: transparent; text-align: center; padding: 45px 25px;")
