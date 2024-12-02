# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockPriceMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 325)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.qtEditPushButton = QPushButton(self.centralwidget)
        self.qtEditPushButton.setObjectName(u"qtEditPushButton")
        self.qtEditPushButton.setGeometry(QRect(110, 250, 131, 23))
        self.qtPriceTableView = QTableView(self.centralwidget)
        self.qtPriceTableView.setObjectName(u"qtPriceTableView")
        self.qtPriceTableView.setGeometry(QRect(10, 50, 761, 191))
        self.qtDeletePushButton = QPushButton(self.centralwidget)
        self.qtDeletePushButton.setObjectName(u"qtDeletePushButton")
        self.qtDeletePushButton.setGeometry(QRect(260, 250, 111, 23))
        self.qtAddPushButton = QPushButton(self.centralwidget)
        self.qtAddPushButton.setObjectName(u"qtAddPushButton")
        self.qtAddPushButton.setGeometry(QRect(400, 250, 101, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.qtEditPushButton.setText(QCoreApplication.translate("MainWindow", u"\u7de8\u8f2f", None))
        self.qtDeletePushButton.setText(QCoreApplication.translate("MainWindow", u"\u522a\u9664", None))
        self.qtAddPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e", None))
    # retranslateUi

