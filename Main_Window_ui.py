# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(514, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"Icons/chess-clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));\n"
"color: rgb(0, 34, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 10, 291, 91))
        self.logo.setLayoutDirection(Qt.RightToLeft)
        self.logo.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Sunken)
        self.logo.setPixmap(QPixmap(u"Icons/vector/default.svg"))
        self.history = QLabel(self.centralwidget)
        self.history.setObjectName(u"history")
        self.history.setGeometry(QRect(390, 40, 41, 41))
        self.history.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.history.setPixmap(QPixmap(u"Icons/vehicle_10883158.png"))
        self.ranking = QLabel(self.centralwidget)
        self.ranking.setObjectName(u"ranking")
        self.ranking.setGeometry(QRect(440, 40, 41, 41))
        self.ranking.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.ranking.setPixmap(QPixmap(u"C:/Users/Mr/Downloads/chart-bars_7268541.png"))
        self.profile = QLabel(self.centralwidget)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(340, 40, 41, 41))
        self.profile.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.profile.setFrameShape(QFrame.NoFrame)
        self.profile.setPixmap(QPixmap(u"Icons/user_11144968.png"))
        self.match_type = QComboBox(self.centralwidget)
        icon1 = QIcon()
        icon1.addFile(u"Icons/bullet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.match_type.addItem(icon1, "")
        self.match_type.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u"Icons/lightning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.match_type.addItem(icon2, "")
        self.match_type.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u"Icons/rapid.png", QSize(), QIcon.Normal, QIcon.Off)
        self.match_type.addItem(icon3, "")
        self.match_type.addItem(icon3, "")
        self.match_type.setObjectName(u"match_type")
        self.match_type.setGeometry(QRect(90, 120, 350, 50))
        self.match_type.setMinimumSize(QSize(350, 50))
        self.match_type.setMaximumSize(QSize(350, 50))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.match_type.setFont(font)
        self.match_type.setCursor(QCursor(Qt.UpArrowCursor))
        self.match_type.setStyleSheet(u"background-color: rgb(112, 229, 22);\n"
"border: 1px solid rgb(0, 255, 127);\n"
"border-radius: 10px;\n"
"color: rgb(26, 35, 30)")
        self.match_type.setFrame(False)
        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setGeometry(QRect(90, 180, 350, 50))
        self.playButton.setMinimumSize(QSize(350, 50))
        self.playButton.setMaximumSize(QSize(350, 50))
        font1 = QFont()
        font1.setFamilies([u"Algerian"])
        font1.setPointSize(20)
        self.playButton.setFont(font1)
        self.playButton.setStyleSheet(u"background-color:rgb(169, 255, 8);\n"
"border: 1px solid rgb(85, 255, 127);\n"
"        border-radius: 10px;\n"
"        padding: 10px 20px;\n"
"color: rgb(25, 33, 19)\n"
"")
        self.playButton.setAutoDefault(False)
        self.playButton.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.playButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chess Clock", None))
        self.logo.setText("")
        self.history.setText("")
        self.ranking.setText("")
        self.profile.setText("")
        self.match_type.setItemText(0, QCoreApplication.translate("MainWindow", u"  Bullet: 1 Min", None))
        self.match_type.setItemText(1, QCoreApplication.translate("MainWindow", u"  Bullet: 2 Min", None))
        self.match_type.setItemText(2, QCoreApplication.translate("MainWindow", u"  Blitz: 3 Min", None))
        self.match_type.setItemText(3, QCoreApplication.translate("MainWindow", u"  Blitz: 5 Min", None))
        self.match_type.setItemText(4, QCoreApplication.translate("MainWindow", u"  Rapid: 10 Min", None))
        self.match_type.setItemText(5, QCoreApplication.translate("MainWindow", u"  Rapid: 15 Min", None))

        self.match_type.setPlaceholderText("")
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
    # retranslateUi

