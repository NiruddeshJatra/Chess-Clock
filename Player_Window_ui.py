# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Player_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_Player_Window(object):
    def setupUi(self, Player_Window):
        if not Player_Window.objectName():
            Player_Window.setObjectName(u"Player_Window")
        Player_Window.resize(316, 184)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Player_Window.sizePolicy().hasHeightForWidth())
        Player_Window.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"Icons/chess-clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        Player_Window.setWindowIcon(icon)
        Player_Window.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));\n"
"color: rgb(0, 34, 0);")
        self.centralwidget = QWidget(Player_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 261, 151))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Player_1 = QLabel(self.widget)
        self.Player_1.setObjectName(u"Player_1")
        font = QFont()
        font.setFamilies([u"Georgia Pro Cond Black"])
        font.setPointSize(16)
        font.setBold(True)
        self.Player_1.setFont(font)
        self.Player_1.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.Player_1)

        self.Player_1_lineEdit = QLineEdit(self.widget)
        self.Player_1_lineEdit.setObjectName(u"Player_1_lineEdit")
        font1 = QFont()
        font1.setFamilies([u"Georgia Pro"])
        font1.setPointSize(14)
        font1.setItalic(True)
        self.Player_1_lineEdit.setFont(font1)
        self.Player_1_lineEdit.setStyleSheet(u"background-color:rgb(162, 241, 120);\n"
"border: 1px solid rgb(85, 255, 127);\n"
"padding: 6px 8px;\n"
"        border-radius: 5px;\n"
"color: rgb(25, 33, 19)\n"
"")

        self.verticalLayout.addWidget(self.Player_1_lineEdit)

        self.Player_2 = QLabel(self.widget)
        self.Player_2.setObjectName(u"Player_2")
        font2 = QFont()
        font2.setFamilies([u"Georgia Pro Black"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.Player_2.setFont(font2)

        self.verticalLayout.addWidget(self.Player_2)

        self.Player_2_lineEdit = QLineEdit(self.widget)
        self.Player_2_lineEdit.setObjectName(u"Player_2_lineEdit")
        self.Player_2_lineEdit.setFont(font1)
        self.Player_2_lineEdit.setStyleSheet(u"background-color:rgb(162, 241, 120);\n"
"border: 1px solid rgb(85, 255, 127);\n"
"padding: 6px 8px;\n"
"        border-radius: 5px;\n"
"color: rgb(25, 33, 19)\n"
"")

        self.verticalLayout.addWidget(self.Player_2_lineEdit)

        Player_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Player_Window)
        self.statusbar.setObjectName(u"statusbar")
        Player_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Player_Window)

        QMetaObject.connectSlotsByName(Player_Window)
    # setupUi

    def retranslateUi(self, Player_Window):
        Player_Window.setWindowTitle(QCoreApplication.translate("Player_Window", u"Entry Player's Name", None))
        self.Player_1.setText(QCoreApplication.translate("Player_Window", u"Player 1 - White", None))
        self.Player_2.setText(QCoreApplication.translate("Player_Window", u"Player 2 - Black", None))
    # retranslateUi

