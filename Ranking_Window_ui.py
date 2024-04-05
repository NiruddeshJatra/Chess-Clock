# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ranking_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QMainWindow, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 380)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 380))
        MainWindow.setMaximumSize(QSize(1000, 380))
        font = QFont()
        font.setFamilies([u"Castellar"])
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(8, 109, 55, 255), stop:1 rgba(63, 206, 112, 255));\n"
"            color: rgb(0, 34, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 801, 381))
        font1 = QFont()
        font1.setFamilies([u"Castellar"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.widget.setFont(font1)
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"Gill Sans Nova Light"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 2, 4, 1, 1)

        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)
        self.label_32.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_32, 6, 1, 1, 1)

        self.label_40 = QLabel(self.widget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_40, 7, 4, 1, 1)

        self.label_56 = QLabel(self.widget)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font2)
        self.label_56.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_56, 10, 1, 1, 1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 3, 4, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 0, 127);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_19, 4, 2, 1, 1)

        self.label_52 = QLabel(self.widget)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font2)
        self.label_52.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_52, 9, 4, 1, 1)

        self.label_45 = QLabel(self.widget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font2)
        self.label_45.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_45, 8, 3, 1, 1)

        self.label_35 = QLabel(self.widget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_35, 6, 0, 1, 1)

        self.label_54 = QLabel(self.widget)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font2)
        self.label_54.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_54, 9, 5, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.label_39 = QLabel(self.widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)
        self.label_39.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_39, 7, 3, 1, 1)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(64, 0, 255)")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_31, 6, 2, 1, 1)

        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 4, 4, 1, 1)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_26, 5, 1, 1, 1)

        self.label_43 = QLabel(self.widget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font2)
        self.label_43.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_43, 8, 2, 1, 1)

        self.label_46 = QLabel(self.widget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font2)
        self.label_46.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_46, 8, 4, 1, 1)

        self.label_62 = QLabel(self.widget)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font2)
        self.label_62.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_62, 11, 1, 1, 1)

        self.label_34 = QLabel(self.widget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)
        self.label_34.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_34, 6, 4, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_30, 5, 5, 1, 1)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_21, 4, 3, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color:rgb(0, 47, 255)")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
        self.label_28.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_28, 5, 4, 1, 1)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 0, 127);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_20, 4, 1, 1, 1)

        self.label_48 = QLabel(self.widget)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font2)
        self.label_48.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_48, 8, 5, 1, 1)

        self.label_61 = QLabel(self.widget)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font2)
        self.label_61.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_61, 11, 2, 1, 1)

        self.label_41 = QLabel(self.widget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font2)
        self.label_41.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_41, 7, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 3, 3, 1, 1)

        self.label_63 = QLabel(self.widget)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font2)
        self.label_63.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_63, 11, 3, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color:rgb(0, 47, 255)")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(64, 0, 255)")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 3, 1, 1, 1)

        self.label_53 = QLabel(self.widget)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font2)
        self.label_53.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_53, 9, 0, 1, 1)

        self.label_42 = QLabel(self.widget)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font2)
        self.label_42.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_42, 7, 5, 1, 1)

        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_33, 6, 3, 1, 1)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_25, 5, 2, 1, 1)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_27, 5, 3, 1, 1)

        self.label_47 = QLabel(self.widget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font2)
        self.label_47.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_47, 8, 0, 1, 1)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 0, 127);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_23, 4, 0, 1, 1)

        self.label_65 = QLabel(self.widget)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font2)
        self.label_65.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_65, 11, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_51 = QLabel(self.widget)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font2)
        self.label_51.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_51, 9, 3, 1, 1)

        self.label_58 = QLabel(self.widget)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font2)
        self.label_58.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_58, 10, 4, 1, 1)

        self.label_44 = QLabel(self.widget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font2)
        self.label_44.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_44, 8, 1, 1, 1)

        self.label_64 = QLabel(self.widget)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font2)
        self.label_64.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(85, 85, 85);")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_64, 11, 4, 1, 1)

        self.label_57 = QLabel(self.widget)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font2)
        self.label_57.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(0, 85, 0);")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_57, 10, 3, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(64, 0, 255)")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)

        self.label_55 = QLabel(self.widget)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)
        self.label_55.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_55, 10, 2, 1, 1)

        self.label_59 = QLabel(self.widget)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font2)
        self.label_59.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_59, 10, 0, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 2, 5, 1, 1)

        self.label_36 = QLabel(self.widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_36, 6, 5, 1, 1)

        self.label_49 = QLabel(self.widget)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font2)
        self.label_49.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_49, 9, 2, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)

        self.label_50 = QLabel(self.widget)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font2)
        self.label_50.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_50, 9, 1, 1, 1)

        self.label_37 = QLabel(self.widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_37, 7, 2, 1, 1)

        self.label_60 = QLabel(self.widget)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font2)
        self.label_60.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_60, 10, 5, 1, 1)

        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 4, 5, 1, 1)

        self.label_38 = QLabel(self.widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)
        self.label_38.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_38, 7, 1, 1, 1)

        self.label_66 = QLabel(self.widget)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font2)
        self.label_66.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_66, 11, 5, 1, 1)

        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_29, 5, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color: rgb(170, 0, 0);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 3, 5, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 99, 0, 255), stop:0.517045 rgba(213, 255, 148, 255), stop:0.994318 rgba(27, 125, 0, 255));\n"
"color:rgb(0, 47, 255)")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText("")
        self.label_32.setText("")
        self.label_40.setText("")
        self.label_56.setText("")
        self.label_16.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Lost", None))
        self.label_19.setText("")
        self.label_52.setText("")
        self.label_45.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_54.setText("")
        self.label_9.setText("")
        self.label_39.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_31.setText("")
        self.label_22.setText("")
        self.label_26.setText("")
        self.label_43.setText("")
        self.label_46.setText("")
        self.label_62.setText("")
        self.label_34.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_30.setText("")
        self.label_21.setText("")
        self.label_7.setText("")
        self.label_28.setText("")
        self.label_20.setText("")
        self.label_48.setText("")
        self.label_61.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rating", None))
        self.label_15.setText("")
        self.label_63.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_14.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_42.setText("")
        self.label_33.setText("")
        self.label_25.setText("")
        self.label_27.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Won", None))
        self.label_51.setText("")
        self.label_58.setText("")
        self.label_44.setText("")
        self.label_64.setText("")
        self.label_57.setText("")
        self.label_13.setText("")
        self.label_55.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_12.setText("")
        self.label_36.setText("")
        self.label_49.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Draw", None))
        self.label_50.setText("")
        self.label_37.setText("")
        self.label_60.setText("")
        self.label_24.setText("")
        self.label_38.setText("")
        self.label_66.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ranking", None))
        self.label_18.setText("")
        self.label_8.setText("")
    # retranslateUi

