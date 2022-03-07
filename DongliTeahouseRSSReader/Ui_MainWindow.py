# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import DTPySide.DT_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 658)
        self.actionCreate_New_Section = QAction(MainWindow)
        self.actionCreate_New_Section.setObjectName(u"actionCreate_New_Section")
        icon = QIcon()
        icon.addFile(u":/icon/white/white_plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCreate_New_Section.setIcon(icon)
        self.horizontalLayout_5 = QHBoxLayout(MainWindow)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(72, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")

        self.horizontalLayout_3.addLayout(self.buttonLayout)


        self.horizontalLayout_5.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(MainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.horizontalLayout_4 = QHBoxLayout(self.page_home)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(39)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_home)
        self.page_rss = QWidget()
        self.page_rss.setObjectName(u"page_rss")
        self.horizontalLayout_2 = QHBoxLayout(self.page_rss)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.page_rss)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_all = QPushButton(self.widget)
        self.pushButton_all.setObjectName(u"pushButton_all")

        self.verticalLayout_2.addWidget(self.pushButton_all)

        self.topfeedTable = QTableWidget(self.widget)
        self.topfeedTable.setObjectName(u"topfeedTable")
        self.topfeedTable.setMinimumSize(QSize(200, 0))

        self.verticalLayout_2.addWidget(self.topfeedTable)

        self.feedTable = QTableWidget(self.widget)
        self.feedTable.setObjectName(u"feedTable")
        self.feedTable.setMinimumSize(QSize(200, 0))

        self.verticalLayout_2.addWidget(self.feedTable)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 5)
        self.splitter.addWidget(self.widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.articleTable = QTableWidget(self.layoutWidget)
        self.articleTable.setObjectName(u"articleTable")
        self.articleTable.setMinimumSize(QSize(200, 0))

        self.verticalLayout.addWidget(self.articleTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_left = QPushButton(self.layoutWidget)
        self.pushButton_left.setObjectName(u"pushButton_left")
        icon1 = QIcon()
        icon1.addFile(u":/icon/white/white_chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_left.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton_left)

        self.pushButton_right = QPushButton(self.layoutWidget)
        self.pushButton_right.setObjectName(u"pushButton_right")
        icon2 = QIcon()
        icon2.addFile(u":/icon/white/white_chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_right.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_right)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget)

        self.horizontalLayout_2.addWidget(self.splitter)

        self.stackedWidget.addWidget(self.page_rss)

        self.horizontalLayout_5.addWidget(self.stackedWidget)


        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.actionCreate_New_Section.setText(QCoreApplication.translate("MainWindow", u"Create New Section", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_all.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.pushButton_left.setText("")
        self.pushButton_right.setText("")
    # retranslateUi

