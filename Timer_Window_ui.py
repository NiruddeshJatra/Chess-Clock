# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Timer_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import Photos_rc

class Ui_Timer_Window(object):
    def setupUi(self, Timer_Window):
        if not Timer_Window.objectName():
            Timer_Window.setObjectName(u"Timer_Window")
        Timer_Window.resize(640, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Timer_Window.sizePolicy().hasHeightForWidth())
        Timer_Window.setSizePolicy(sizePolicy)
        Timer_Window.setMinimumSize(QSize(640, 480))
        Timer_Window.setMaximumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u"Icons/chess-clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        Timer_Window.setWindowIcon(icon)
        Timer_Window.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));\n"
"color: rgb(0, 34, 0);")
        self.centralwidget = QWidget(Timer_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Player_1_name = QLabel(self.centralwidget)
        self.Player_1_name.setObjectName(u"Player_1_name")
        self.Player_1_name.setGeometry(QRect(80, 30, 171, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.Player_1_name.setFont(font)
        self.Player_1_name.setStyleSheet(u"background-color: transparent;")
        self.Player_1_time = QLCDNumber(self.centralwidget)
        self.Player_1_time.setObjectName(u"Player_1_time")
        self.Player_1_time.setGeometry(QRect(40, 80, 251, 201))
        self.Player_1_time.setStyleSheet(u"background-color: rgb(33, 33, 33)")
        self.Player_2_time = QLCDNumber(self.centralwidget)
        self.Player_2_time.setObjectName(u"Player_2_time")
        self.Player_2_time.setGeometry(QRect(340, 80, 251, 201))
        self.Player_2_time.setStyleSheet(u"background-color: rgb(33, 33, 33)")
        self.Player_2_name = QLabel(self.centralwidget)
        self.Player_2_name.setObjectName(u"Player_2_name")
        self.Player_2_name.setGeometry(QRect(390, 30, 171, 41))
        self.Player_2_name.setFont(font)
        self.Player_2_name.setStyleSheet(u"background-color: transparent;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 320, 461, 101))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(True)
        self.pushButton.setFont(font1)
        self.pushButton.setIconSize(QSize(30, 16))
        self.EndButton = QLabel(self.centralwidget)
        self.EndButton.setObjectName(u"EndButton")
        self.EndButton.setGeometry(QRect(310, 430, 31, 31))
        self.EndButton.setStyleSheet(u"background-color: transparent;")
        self.EndButton.setPixmap(QPixmap(u"Icons/palm.png"))
        self.Player_1_move = QLabel(self.centralwidget)
        self.Player_1_move.setObjectName(u"Player_1_move")
        self.Player_1_move.setGeometry(QRect(50, 250, 81, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe Pro Display SemiLight"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.Player_1_move.setFont(font2)
        self.Player_1_move.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.Player_2_move = QLabel(self.centralwidget)
        self.Player_2_move.setObjectName(u"Player_2_move")
        self.Player_2_move.setGeometry(QRect(350, 250, 81, 16))
        self.Player_2_move.setFont(font2)
        self.Player_2_move.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        Timer_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Timer_Window)
        self.statusbar.setObjectName(u"statusbar")
        Timer_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Timer_Window)

        QMetaObject.connectSlotsByName(Timer_Window)
    # setupUi

    def retranslateUi(self, Timer_Window):
        Timer_Window.setWindowTitle(QCoreApplication.translate("Timer_Window", u"Clock Winodw", None))
        self.Player_1_name.setText(QCoreApplication.translate("Timer_Window", u"Player 1", None))
        self.Player_2_name.setText(QCoreApplication.translate("Timer_Window", u"Player 2", None))
        self.pushButton.setText(QCoreApplication.translate("Timer_Window", u"Player 1's Move", None))
        self.EndButton.setText("")
        self.Player_1_move.setText(QCoreApplication.translate("Timer_Window", u"Moves: ", None))
        self.Player_2_move.setText(QCoreApplication.translate("Timer_Window", u"Moves: ", None))
    # retranslateUi

