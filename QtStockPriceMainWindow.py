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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTabWidget,
    QTableView, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1167, 893)
        self.qtNewFileAction = QAction(MainWindow)
        self.qtNewFileAction.setObjectName(u"qtNewFileAction")
        self.qtSaveAsAction = QAction(MainWindow)
        self.qtSaveAsAction.setObjectName(u"qtSaveAsAction")
        self.qtSaveAction = QAction(MainWindow)
        self.qtSaveAction.setObjectName(u"qtSaveAction")
        self.qtOpenFileAction = QAction(MainWindow)
        self.qtOpenFileAction.setObjectName(u"qtOpenFileAction")
        self.qtExportCurrentGroupAction = QAction(MainWindow)
        self.qtExportCurrentGroupAction.setObjectName(u"qtExportCurrentGroupAction")
        self.qtImportFullAction = QAction(MainWindow)
        self.qtImportFullAction.setObjectName(u"qtImportFullAction")
        self.qtImportSingleStockAction = QAction(MainWindow)
        self.qtImportSingleStockAction.setObjectName(u"qtImportSingleStockAction")
        self.qtFromNewToOldAction = QAction(MainWindow)
        self.qtFromNewToOldAction.setObjectName(u"qtFromNewToOldAction")
        self.qtFromNewToOldAction.setCheckable(True)
        self.qtFromOldToNewAction = QAction(MainWindow)
        self.qtFromOldToNewAction.setObjectName(u"qtFromOldToNewAction")
        self.qtFromOldToNewAction.setCheckable(True)
        self.qtShowAllAction = QAction(MainWindow)
        self.qtShowAllAction.setObjectName(u"qtShowAllAction")
        self.qtShowAllAction.setCheckable(True)
        self.qtShow10Action = QAction(MainWindow)
        self.qtShow10Action.setObjectName(u"qtShow10Action")
        self.qtShow10Action.setCheckable(True)
        self.qtUse1ShareUnitAction = QAction(MainWindow)
        self.qtUse1ShareUnitAction.setObjectName(u"qtUse1ShareUnitAction")
        self.qtUse1ShareUnitAction.setCheckable(True)
        self.qtUse1000ShareUnitAction = QAction(MainWindow)
        self.qtUse1000ShareUnitAction.setObjectName(u"qtUse1000ShareUnitAction")
        self.qtUse1000ShareUnitAction.setCheckable(True)
        self.qtADYearAction = QAction(MainWindow)
        self.qtADYearAction.setObjectName(u"qtADYearAction")
        self.qtADYearAction.setCheckable(True)
        self.qtROCYearAction = QAction(MainWindow)
        self.qtROCYearAction.setObjectName(u"qtROCYearAction")
        self.qtROCYearAction.setCheckable(True)
        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1165, 850))
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
        self.tab_add.setMinimumSize(QSize(25, 25))
        self.qtTabWidget.addTab(self.tab_add, "")

        self.verticalLayout.addWidget(self.qtTabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtCurrentSelectCompanyLabel = QLabel(self.scrollAreaWidgetContents)
        self.qtCurrentSelectCompanyLabel.setObjectName(u"qtCurrentSelectCompanyLabel")

        self.horizontalLayout.addWidget(self.qtCurrentSelectCompanyLabel)

        self.qtHideTradingDataTableToolButton = QToolButton(self.scrollAreaWidgetContents)
        self.qtHideTradingDataTableToolButton.setObjectName(u"qtHideTradingDataTableToolButton")

        self.horizontalLayout.addWidget(self.qtHideTradingDataTableToolButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.qtTradingDataTableView = QTableView(self.scrollAreaWidgetContents)
        self.qtTradingDataTableView.setObjectName(u"qtTradingDataTableView")
        self.qtTradingDataTableView.setMinimumSize(QSize(0, 471))
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
        self.menubar.setGeometry(QRect(0, 0, 1167, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.qtNewFileAction)
        self.menu.addAction(self.qtOpenFileAction)
        self.menu.addSeparator()
        self.menu.addAction(self.qtSaveAsAction)
        self.menu.addAction(self.qtSaveAction)
        self.menu.addSeparator()
        self.menu.addAction(self.qtExportCurrentGroupAction)
        self.menu.addAction(self.qtImportFullAction)
        self.menu.addAction(self.qtImportSingleStockAction)
        self.menu_2.addAction(self.qtFromNewToOldAction)
        self.menu_2.addAction(self.qtFromOldToNewAction)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.qtShowAllAction)
        self.menu_2.addAction(self.qtShow10Action)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.qtUse1ShareUnitAction)
        self.menu_2.addAction(self.qtUse1000ShareUnitAction)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.qtADYearAction)
        self.menu_2.addAction(self.qtROCYearAction)

        self.retranslateUi(MainWindow)

        self.qtTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.qtNewFileAction.setText(QCoreApplication.translate("MainWindow", u"\u958b\u65b0\u6a94\u6848", None))
        self.qtSaveAsAction.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u65b0\u6a94", None))
        self.qtSaveAction.setText(QCoreApplication.translate("MainWindow", u"\u5132\u5b58", None))
        self.qtOpenFileAction.setText(QCoreApplication.translate("MainWindow", u"\u958b\u555f\u820a\u6a94", None))
        self.qtExportCurrentGroupAction.setText(QCoreApplication.translate("MainWindow", u"\u532f\u51fa\u76ee\u524d\u7fa4\u7d44", None))
        self.qtImportFullAction.setText(QCoreApplication.translate("MainWindow", u"\u532f\u5165\u6240\u6709\u7fa4\u7d44\u8cc7\u6599", None))
        self.qtImportSingleStockAction.setText(QCoreApplication.translate("MainWindow", u"\u532f\u5165\u55ae\u652f\u80a1\u7968\u5230\u7576\u524d\u7fa4\u7d44", None))
        self.qtFromNewToOldAction.setText(QCoreApplication.translate("MainWindow", u"\u7531\u65b0\u5230\u820a", None))
        self.qtFromOldToNewAction.setText(QCoreApplication.translate("MainWindow", u"\u7531\u820a\u5230\u65b0", None))
        self.qtShowAllAction.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u5168\u90e8\u4ea4\u6613\u7d00\u9304", None))
        self.qtShow10Action.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a10\u7b46\u4ea4\u6613\u7d00\u9304", None))
        self.qtUse1ShareUnitAction.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u4e00\u80a1\u70ba\u55ae\u4f4d", None))
        self.qtUse1000ShareUnitAction.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u4e00\u5f35\u70ba\u55ae\u4f4d", None))
        self.qtADYearAction.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u897f\u5143\u986f\u793a", None))
        self.qtROCYearAction.setText(QCoreApplication.translate("MainWindow", u"\u4ee5\u6c11\u570b\u986f\u793a", None))
#if QT_CONFIG(tooltip)
        self.tab_add.setToolTip(QCoreApplication.translate("MainWindow", u"\u96d9\u64ca\u65b0\u589e", None))
#endif // QT_CONFIG(tooltip)
        self.qtTabWidget.setTabText(self.qtTabWidget.indexOf(self.tab_add), QCoreApplication.translate("MainWindow", u"+", None))
        self.qtCurrentSelectCompanyLabel.setText("")
        self.qtHideTradingDataTableToolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.qtAddTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u73fe\u80a1\u4ea4\u6613\u7d00\u9304(T)", None))
        self.qtAddRegularTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u5b9a\u671f\u5b9a\u984d\u4ea4\u6613\u7d00\u9304(E)", None))
        self.qtAddDividendDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u914d\u80a1\u914d\u606f\u7d00\u9304(D)", None))
        self.qtAddLimitBuyingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u589e\u8cc7\u8a8d\u8cfc\u7d00\u9304(A)", None))
        self.qtAddCapitalReductionDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u73fe\u91d1\u6e1b\u8cc7\u7d00\u9304(R)", None))
        self.qtExportAllStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u6240\u6709\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.qtExportSelectedStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u55ae\u652f\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6a94\u6848", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u986f\u793a", None))
    # retranslateUi

