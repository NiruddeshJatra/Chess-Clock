# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Congratulation_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QStatusBar, QWidget)

class Ui_Congratulation_Window(object):
    def setupUi(self, Congratulation_Window):
        if not Congratulation_Window.objectName():
            Congratulation_Window.setObjectName(u"Congratulation_Window")
        Congratulation_Window.resize(330, 330)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Congratulation_Window.sizePolicy().hasHeightForWidth())
        Congratulation_Window.setSizePolicy(sizePolicy)
        Congratulation_Window.setMinimumSize(QSize(330, 330))
        Congratulation_Window.setMaximumSize(QSize(330, 330))
        font = QFont()
        font.setFamilies([u"Lucida Handwriting"])
        font.setPointSize(22)
        Congratulation_Window.setFont(font)
        icon = QIcon()
        icon.addFile(u"Icons/chess-clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        Congratulation_Window.setWindowIcon(icon)
        Congratulation_Window.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));\n"
"color: rgb(253, 255, 210);\n"
"text-shadow:0 0 5px rgba(255, 255, 255, 0.5);")
        self.centralwidget = QWidget(Congratulation_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 311, 51))
        font1 = QFont()
        font1.setFamilies([u"Lucida Calligraphy"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 90, 261, 91))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 180, 171, 61))
        font2 = QFont()
        font2.setFamilies([u"Lucida Calligraphy"])
        font2.setPointSize(25)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: transparent;")
        Congratulation_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Congratulation_Window)
        self.statusbar.setObjectName(u"statusbar")
        Congratulation_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Congratulation_Window)

        QMetaObject.connectSlotsByName(Congratulation_Window)
    # setupUi

    def retranslateUi(self, Congratulation_Window):
        Congratulation_Window.setWindowTitle(QCoreApplication.translate("Congratulation_Window", u"Congratulations!", None))
        self.label.setText(QCoreApplication.translate("Congratulation_Window", u"Congratulations!", None))
        self.label_2.setText(QCoreApplication.translate("Congratulation_Window", u"PLayer 1 Won", None))
        self.label_3.setText(QCoreApplication.translate("Congratulation_Window", u" on Time", None))
    # retranslateUi

