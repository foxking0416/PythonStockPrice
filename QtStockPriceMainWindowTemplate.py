# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockPriceMainWindowTemplate.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
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
        self.qtActionExport = QAction(MainWindow)
        self.qtActionExport.setObjectName(u"qtActionExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.qtTabWidget = QTabWidget(self.centralwidget)
        self.qtTabWidget.setObjectName(u"qtTabWidget")
        self.qtTabWidget.setIconSize(QSize(10, 10))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.tabWidget = QTabWidget(self.tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtStockInputLineEdit = QLineEdit(self.tab_3)
        self.qtStockInputLineEdit.setObjectName(u"qtStockInputLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtStockInputLineEdit.sizePolicy().hasHeightForWidth())
        self.qtStockInputLineEdit.setSizePolicy(sizePolicy)
        self.qtStockInputLineEdit.setMinimumSize(QSize(200, 0))
        self.qtStockInputLineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.qtStockInputLineEdit)

        self.qtAddStockPushButton = QPushButton(self.tab_3)
        self.qtAddStockPushButton.setObjectName(u"qtAddStockPushButton")
        self.qtAddStockPushButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.qtAddStockPushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.qtExtraInsuranceFeeCheckBox = QCheckBox(self.tab_3)
        self.qtExtraInsuranceFeeCheckBox.setObjectName(u"qtExtraInsuranceFeeCheckBox")

        self.horizontalLayout.addWidget(self.qtExtraInsuranceFeeCheckBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.qtStockSelectComboBox = QComboBox(self.tab_3)
        self.qtStockSelectComboBox.setObjectName(u"qtStockSelectComboBox")
        self.qtStockSelectComboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.qtStockSelectComboBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qtStockListTableView = QTableView(self.tab_3)
        self.qtStockListTableView.setObjectName(u"qtStockListTableView")
        self.qtStockListTableView.setMinimumSize(QSize(0, 100))

        self.horizontalLayout_2.addWidget(self.qtStockListTableView)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.qtTabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.qtTabWidget.addTab(self.tab_2, "")

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
        self.menu.addAction(self.qtActionExport)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.qtActionImport.setText(QCoreApplication.translate("MainWindow", u"\u532f\u5165", None))
        self.qtActionExport.setText(QCoreApplication.translate("MainWindow", u"\u532f\u51fa", None))
        self.qtAddStockPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u80a1\u7968", None))
        self.qtExtraInsuranceFeeCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u88dc\u5145\u4fdd\u8cbb", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.qtTabWidget.setTabText(self.qtTabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.qtTabWidget.setTabText(self.qtTabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
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
        self.qtAddCapitalReductionDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u73fe\u91d1\u6e1b\u8cc7\u7d00\u9304", None))
        self.qtExportAllStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u6240\u6709\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.qtExportSelectedStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u55ae\u652f\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6a94\u6848", None))
    # retranslateUi

