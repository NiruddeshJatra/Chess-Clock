from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import mysql.connector



class UiProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.loadBaseUi()
        self.enterUsername()
        self.showCreateButton()


    def loadBaseUi(self):
        self.setWindowTitle("Create Profile")
        self.setFixedSize(315, 150)
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
        
        
    def enterUsername(self):
        self.nameLabel = QLabel("Enter Your Name")
        self.nameLabel.setContentsMargins(15, 5, 10, 0)
        font = QFont("Georgia Pro Black", 16)
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("")
        self.generalLayout.addWidget(self.nameLabel)

        self.name = QLineEdit()
        self.name.setContentsMargins(15, 0, 10, 10)
        self.name.setFixedSize(290, 45)
        font = QFont("Georgia Pro", 12)
        font.setItalic(True)
        self.name.setFont(font)
        self.name.setStyleSheet("""
            background-color:rgb(162, 241, 120);
            border: 1px solid rgb(85, 255, 127);
            padding: 6px 8px;
            border-radius: 5px;
            color: rgb(25, 33, 19);
            """
        )
        self.name.returnPressed.connect(self.addProfile)
        self.generalLayout.addWidget(self.name)
        
        
    def showCreateButton(self):
        self.createButton = QPushButton("create")
        self.createButton.setFixedSize(280, 45)
        font = QFont("Algerian", 18)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("""
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
        
        self.createButton.enterEvent = lambda event: self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.createButton.leaveEvent = lambda event: self.setCursor(Qt.CursorShape.ArrowCursor)
        self.createButton.clicked.connect(self.addProfile)
        self.generalLayout.addWidget(self.createButton)
        
        
    def loadDatabase(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "password",
            database = "chess_clock",
        )
        self.c = self.mydb.cursor()    
        
        
    def addProfile(self):
        profileName = self.name.text().lower()
        
        if profileName == "":
            self.name.setStyleSheet("""
                background-color:rgb(162, 241, 120);
                border: 1px solid red;
                padding: 6px 8px;
                border-radius: 5px;
                color: rgb(25, 33, 19);
            """)
        
        else:
            self.loadDatabase()
            self.c.execute("SELECT Username FROM profile")
            profiles = [profile[0] for profile in self.c.fetchall()]
            
            if profileName in profiles:
                self.name.setStyleSheet("""
                    background-color:rgb(162, 241, 120);
                    border: 1px solid red;
                    padding: 6px 8px;
                    border-radius: 5px;
                    color: rgb(25, 33, 19);
                """)
                
                self.showWarningMessageBox()
                
            else:
                self.c.execute("""
                    INSERT INTO profile (Username, Match_played, Won, Draw, Lost, Rating)
                    VALUES (%s, 0, 0, 0, 0, 1000)", (profileName,)
                """)
                self.mydb.commit()
                self.mydb.close()
                self.hide()
        
        
    def showWarningMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Already Created!!!")
        msg.setText("This profile exists in the database!\nEnter another one.")
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/chess-clock.svg"))
        msg.setWindowIcon(icon)
        font = QFont("Sitka", 20)
        font.setBold(True)
        msg.setFont(font)
        msg.exec()
        
        