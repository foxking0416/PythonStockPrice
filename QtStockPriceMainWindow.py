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
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1131, 893)
        self.qtActionNew = QAction(MainWindow)
        self.qtActionNew.setObjectName(u"qtActionNew")
        self.qtActionSaveAs = QAction(MainWindow)
        self.qtActionSaveAs.setObjectName(u"qtActionSaveAs")
        self.qtActionSave = QAction(MainWindow)
        self.qtActionSave.setObjectName(u"qtActionSave")
        self.qtActionOpen = QAction(MainWindow)
        self.qtActionOpen.setObjectName(u"qtActionOpen")
        self.qtActionExportCurrentGroup = QAction(MainWindow)
        self.qtActionExportCurrentGroup.setObjectName(u"qtActionExportCurrentGroup")
        self.qtActionImportFull = QAction(MainWindow)
        self.qtActionImportFull.setObjectName(u"qtActionImportFull")
        self.qtActionImportSingleStock = QAction(MainWindow)
        self.qtActionImportSingleStock.setObjectName(u"qtActionImportSingleStock")
        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1129, 850))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.qtTabWidget = QTabWidget(self.scrollAreaWidgetContents)
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
        self.qtFromNewToOldRadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.qtFromNewToOldRadioButton.setObjectName(u"qtFromNewToOldRadioButton")
        self.qtFromNewToOldRadioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.qtFromNewToOldRadioButton)

        self.qtFromOldToNewRadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.qtFromOldToNewRadioButton.setObjectName(u"qtFromOldToNewRadioButton")

        self.verticalLayout_4.addWidget(self.qtFromOldToNewRadioButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.qtShowAllRadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.qtShowAllRadioButton.setObjectName(u"qtShowAllRadioButton")
        self.qtShowAllRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.qtShowAllRadioButton)

        self.qtShow10RadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.qtShow10RadioButton.setObjectName(u"qtShow10RadioButton")

        self.verticalLayout_3.addWidget(self.qtShow10RadioButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_7 = QSpacerItem(50, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.qtShow1StockRadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.qtShow1StockRadioButton.setObjectName(u"qtShow1StockRadioButton")
        self.qtShow1StockRadioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.qtShow1StockRadioButton)

        self.qtShow1000StockRadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.qtShow1000StockRadioButton.setObjectName(u"qtShow1000StockRadioButton")
        self.qtShow1000StockRadioButton.setEnabled(True)

        self.verticalLayout_2.addWidget(self.qtShow1000StockRadioButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_8 = QSpacerItem(50, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.qtADYearRadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.qtADYearRadioButton.setObjectName(u"qtADYearRadioButton")
        self.qtADYearRadioButton.setChecked(True)

        self.verticalLayout_5.addWidget(self.qtADYearRadioButton)

        self.qtROCYearRadioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.qtROCYearRadioButton.setObjectName(u"qtROCYearRadioButton")

        self.verticalLayout_5.addWidget(self.qtROCYearRadioButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.qtTradingDataTableView = QTableView(self.scrollAreaWidgetContents)
        self.qtTradingDataTableView.setObjectName(u"qtTradingDataTableView")
        self.qtTradingDataTableView.setMinimumSize(QSize(0, 470))
        self.qtTradingDataTableView.verticalHeader().setMinimumSectionSize(15)

        self.verticalLayout.addWidget(self.qtTradingDataTableView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtAddTradingDataPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.qtAddTradingDataPushButton.setObjectName(u"qtAddTradingDataPushButton")
        self.qtAddTradingDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddTradingDataPushButton)

        self.qtAddRegularTradingDataPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.qtAddRegularTradingDataPushButton.setObjectName(u"qtAddRegularTradingDataPushButton")
        self.qtAddRegularTradingDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddRegularTradingDataPushButton)

        self.qtAddDividendDataPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.qtAddDividendDataPushButton.setObjectName(u"qtAddDividendDataPushButton")
        self.qtAddDividendDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddDividendDataPushButton)

        self.qtAddLimitBuyingDataPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.qtAddLimitBuyingDataPushButton.setObjectName(u"qtAddLimitBuyingDataPushButton")
        self.qtAddLimitBuyingDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddLimitBuyingDataPushButton)

        self.qtAddCapitalReductionDataPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.qtAddCapitalReductionDataPushButton.setObjectName(u"qtAddCapitalReductionDataPushButton")
        self.qtAddCapitalReductionDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddCapitalReductionDataPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.qtExportAllStockTradingDataPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.qtExportAllStockTradingDataPushButton.setObjectName(u"qtExportAllStockTradingDataPushButton")
        self.qtExportAllStockTradingDataPushButton.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.qtExportAllStockTradingDataPushButton)

        self.qtExportSelectedStockTradingDataPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.qtExportSelectedStockTradingDataPushButton.setObjectName(u"qtExportSelectedStockTradingDataPushButton")
        self.qtExportSelectedStockTradingDataPushButton.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.qtExportSelectedStockTradingDataPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.scrollArea)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1131, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.qtActionNew)
        self.menu.addAction(self.qtActionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.qtActionSaveAs)
        self.menu.addAction(self.qtActionSave)
        self.menu.addSeparator()
        self.menu.addAction(self.qtActionExportCurrentGroup)
        self.menu.addAction(self.qtActionImportFull)
        self.menu.addAction(self.qtActionImportSingleStock)

        self.retranslateUi(MainWindow)

        self.qtTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.qtActionNew.setText(QCoreApplication.translate("MainWindow", u"\u958b\u65b0\u6a94\u6848", None))
        self.qtActionSaveAs.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u65b0\u6a94", None))
        self.qtActionSave.setText(QCoreApplication.translate("MainWindow", u"\u5132\u5b58", None))
        self.qtActionOpen.setText(QCoreApplication.translate("MainWindow", u"\u958b\u555f\u820a\u6a94", None))
        self.qtActionExportCurrentGroup.setText(QCoreApplication.translate("MainWindow", u"\u532f\u51fa\u76ee\u524d\u7fa4\u7d44", None))
        self.qtActionImportFull.setText(QCoreApplication.translate("MainWindow", u"\u532f\u5165\u6240\u6709\u7fa4\u7d44\u8cc7\u6599", None))
        self.qtActionImportSingleStock.setText(QCoreApplication.translate("MainWindow", u"\u532f\u5165\u55ae\u652f\u80a1\u7968\u5230\u7576\u524d\u7fa4\u7d44", None))
        self.qtTabWidget.setTabText(self.qtTabWidget.indexOf(self.tab_add), QCoreApplication.translate("MainWindow", u"+", None))
        self.qtFromNewToOldRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u7531\u65b0\u5230\u820a", None))
        self.qtFromOldToNewRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u7531\u820a\u5230\u65b0", None))
        self.qtShowAllRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u5168\u90e8\u4ea4\u6613\u7d00\u9304", None))
        self.qtShow10RadioButton.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a10\u7b46\u4ea4\u6613\u7d00\u9304", None))
        self.qtShow1StockRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u4e00\u80a1\u70ba\u55ae\u4f4d", None))
        self.qtShow1000StockRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u4e00\u5f35\u70ba\u55ae\u4f4d", None))
        self.qtADYearRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u897f\u5143\u986f\u793a", None))
        self.qtROCYearRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u6c11\u570b\u986f\u793a", None))
        self.qtAddTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u73fe\u80a1\u4ea4\u6613\u7d00\u9304(T)", None))
        self.qtAddRegularTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u5b9a\u671f\u5b9a\u984d\u4ea4\u6613\u7d00\u9304(E)", None))
        self.qtAddDividendDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u914d\u80a1\u914d\u606f\u7d00\u9304(D)", None))
        self.qtAddLimitBuyingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u589e\u8cc7\u8a8d\u8cfc\u8cc7\u6599(A)", None))
        self.qtAddCapitalReductionDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u73fe\u91d1\u6e1b\u8cc7\u7d00\u9304(R)", None))
        self.qtExportAllStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u6240\u6709\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.qtExportSelectedStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u55ae\u652f\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6a94\u6848", None))
    # retranslateUi

