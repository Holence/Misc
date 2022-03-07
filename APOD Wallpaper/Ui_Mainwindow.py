# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        if not Mainwindow.objectName():
            Mainwindow.setObjectName(u"Mainwindow")
        Mainwindow.resize(672, 544)
        self.horizontalLayout = QHBoxLayout(Mainwindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(Mainwindow)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setAutoScroll(False)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setIconSize(QSize(512, 512))
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(10)
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setWordWrap(True)
        self.listWidget.setItemAlignment(Qt.AlignHCenter)

        self.horizontalLayout.addWidget(self.listWidget)


        self.retranslateUi(Mainwindow)

        QMetaObject.connectSlotsByName(Mainwindow)
    # setupUi

    def retranslateUi(self, Mainwindow):
        Mainwindow.setWindowTitle(QCoreApplication.translate("Mainwindow", u"Mainwindow", None))
    # retranslateUi

