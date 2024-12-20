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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(938, 893)
        self.qtActionImport = QAction(MainWindow)
        self.qtActionImport.setObjectName(u"qtActionImport")
        self.qtActionExportAllAccount = QAction(MainWindow)
        self.qtActionExportAllAccount.setObjectName(u"qtActionExportAllAccount")
        self.qtActionExportCurrentAccount = QAction(MainWindow)
        self.qtActionExportCurrentAccount.setObjectName(u"qtActionExportCurrentAccount")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.qtTabWidget = QTabWidget(self.centralwidget)
        self.qtTabWidget.setObjectName(u"qtTabWidget")
        self.qtTabWidget.setIconSize(QSize(10, 10))
        self.qtTabWidget.setTabsClosable(True)
        self.qtTabWidget.setMovable(True)
        self.tab_add = QWidget()
        self.tab_add.setObjectName(u"tab_add")
        self.qtTabWidget.addTab(self.tab_add, "")

        self.verticalLayout.addWidget(self.qtTabWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.qtFromNewToOldRadioButton = QRadioButton(self.centralwidget)
        self.qtFromNewToOldRadioButton.setObjectName(u"qtFromNewToOldRadioButton")
        self.qtFromNewToOldRadioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.qtFromNewToOldRadioButton)

        self.qtFromOldToNewRadioButton = QRadioButton(self.centralwidget)
        self.qtFromOldToNewRadioButton.setObjectName(u"qtFromOldToNewRadioButton")

        self.verticalLayout_4.addWidget(self.qtFromOldToNewRadioButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.qtShowAllRadioButton = QRadioButton(self.centralwidget)
        self.qtShowAllRadioButton.setObjectName(u"qtShowAllRadioButton")
        self.qtShowAllRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.qtShowAllRadioButton)

        self.qtShow10RadioButton = QRadioButton(self.centralwidget)
        self.qtShow10RadioButton.setObjectName(u"qtShow10RadioButton")

        self.verticalLayout_3.addWidget(self.qtShow10RadioButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_7 = QSpacerItem(50, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.qtShow1StockRadioButton = QRadioButton(self.centralwidget)
        self.qtShow1StockRadioButton.setObjectName(u"qtShow1StockRadioButton")
        self.qtShow1StockRadioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.qtShow1StockRadioButton)

        self.qtShow1000StockRadioButton = QRadioButton(self.centralwidget)
        self.qtShow1000StockRadioButton.setObjectName(u"qtShow1000StockRadioButton")

        self.verticalLayout_2.addWidget(self.qtShow1000StockRadioButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_8 = QSpacerItem(50, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.qtADYearRadioButton = QRadioButton(self.centralwidget)
        self.qtADYearRadioButton.setObjectName(u"qtADYearRadioButton")
        self.qtADYearRadioButton.setChecked(True)

        self.verticalLayout_5.addWidget(self.qtADYearRadioButton)

        self.qtROCYearRadioButton = QRadioButton(self.centralwidget)
        self.qtROCYearRadioButton.setObjectName(u"qtROCYearRadioButton")

        self.verticalLayout_5.addWidget(self.qtROCYearRadioButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.qtTradingDataTableView = QTableView(self.centralwidget)
        self.qtTradingDataTableView.setObjectName(u"qtTradingDataTableView")
        self.qtTradingDataTableView.setMinimumSize(QSize(0, 470))
        self.qtTradingDataTableView.verticalHeader().setMinimumSectionSize(15)

        self.verticalLayout.addWidget(self.qtTradingDataTableView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtAddTradingDataPushButton = QPushButton(self.centralwidget)
        self.qtAddTradingDataPushButton.setObjectName(u"qtAddTradingDataPushButton")
        self.qtAddTradingDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddTradingDataPushButton)

        self.qtAddDividendDataPushButton = QPushButton(self.centralwidget)
        self.qtAddDividendDataPushButton.setObjectName(u"qtAddDividendDataPushButton")
        self.qtAddDividendDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddDividendDataPushButton)

        self.qtAddLimitBuyingDataPushButton = QPushButton(self.centralwidget)
        self.qtAddLimitBuyingDataPushButton.setObjectName(u"qtAddLimitBuyingDataPushButton")

        self.horizontalLayout_3.addWidget(self.qtAddLimitBuyingDataPushButton)

        self.qtAddCapitalReductionDataPushButton = QPushButton(self.centralwidget)
        self.qtAddCapitalReductionDataPushButton.setObjectName(u"qtAddCapitalReductionDataPushButton")
        self.qtAddCapitalReductionDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddCapitalReductionDataPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.qtExportAllStockTradingDataPushButton = QPushButton(self.centralwidget)
        self.qtExportAllStockTradingDataPushButton.setObjectName(u"qtExportAllStockTradingDataPushButton")
        self.qtExportAllStockTradingDataPushButton.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.qtExportAllStockTradingDataPushButton)

        self.qtExportSelectedStockTradingDataPushButton = QPushButton(self.centralwidget)
        self.qtExportSelectedStockTradingDataPushButton.setObjectName(u"qtExportSelectedStockTradingDataPushButton")
        self.qtExportSelectedStockTradingDataPushButton.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.qtExportSelectedStockTradingDataPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 938, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.qtActionImport)
        self.menu.addAction(self.qtActionExportAllAccount)
        self.menu.addAction(self.qtActionExportCurrentAccount)

        self.retranslateUi(MainWindow)

        self.qtTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.qtActionImport.setText(QCoreApplication.translate("MainWindow", u"\u532f\u5165", None))
        self.qtActionExportAllAccount.setText(QCoreApplication.translate("MainWindow", u"\u532f\u51fa\u6240\u6709\u5e33\u865f\u8cc7\u6599", None))
        self.qtActionExportCurrentAccount.setText(QCoreApplication.translate("MainWindow", u"\u532f\u51fa\u76ee\u524d\u5e33\u865f\u8cc7\u6599", None))
        self.qtTabWidget.setTabText(self.qtTabWidget.indexOf(self.tab_add), QCoreApplication.translate("MainWindow", u"+", None))
        self.qtFromNewToOldRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u7531\u65b0\u5230\u820a", None))
        self.qtFromOldToNewRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u7531\u820a\u5230\u65b0", None))
        self.qtShowAllRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u5168\u90e8\u4ea4\u6613\u7d00\u9304", None))
        self.qtShow10RadioButton.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a10\u7b46\u4ea4\u6613\u7d00\u9304", None))
        self.qtShow1StockRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u4e00\u80a1\u70ba\u55ae\u4f4d", None))
        self.qtShow1000StockRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u4e00\u5f35\u70ba\u55ae\u4f4d", None))
        self.qtADYearRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u897f\u5143\u986f\u793a", None))
        self.qtROCYearRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u6c11\u570b\u986f\u793a", None))
        self.qtAddTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u4ea4\u6613\u7d00\u9304", None))
        self.qtAddDividendDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u914d\u80a1\u914d\u606f\u7d00\u9304", None))
        self.qtAddLimitBuyingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u589e\u8cc7\u8a8d\u8cfc\u8cc7\u6599", None))
        self.qtAddCapitalReductionDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u73fe\u91d1\u6e1b\u8cc7\u7d00\u9304", None))
        self.qtExportAllStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u6240\u6709\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.qtExportSelectedStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u55ae\u652f\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6a94\u6848", None))
    # retranslateUi

