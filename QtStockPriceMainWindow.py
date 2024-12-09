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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QHeaderView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 794)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtDiscountCheckBox = QCheckBox(self.centralwidget)
        self.qtDiscountCheckBox.setObjectName(u"qtDiscountCheckBox")
        self.qtDiscountCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.qtDiscountCheckBox)

        self.qtDiscountRateDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.qtDiscountRateDoubleSpinBox.setObjectName(u"qtDiscountRateDoubleSpinBox")
        self.qtDiscountRateDoubleSpinBox.setEnabled(True)
        self.qtDiscountRateDoubleSpinBox.setDecimals(1)
        self.qtDiscountRateDoubleSpinBox.setMaximum(10.000000000000000)
        self.qtDiscountRateDoubleSpinBox.setSingleStep(0.500000000000000)
        self.qtDiscountRateDoubleSpinBox.setValue(6.000000000000000)

        self.horizontalLayout.addWidget(self.qtDiscountRateDoubleSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.qtExtraInsuranceFeeCheckBox = QCheckBox(self.centralwidget)
        self.qtExtraInsuranceFeeCheckBox.setObjectName(u"qtExtraInsuranceFeeCheckBox")

        self.horizontalLayout.addWidget(self.qtExtraInsuranceFeeCheckBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.qtStockInputLineEdit = QLineEdit(self.centralwidget)
        self.qtStockInputLineEdit.setObjectName(u"qtStockInputLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtStockInputLineEdit.sizePolicy().hasHeightForWidth())
        self.qtStockInputLineEdit.setSizePolicy(sizePolicy)
        self.qtStockInputLineEdit.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_2.addWidget(self.qtStockInputLineEdit)

        self.qtStockSelectComboBox = QComboBox(self.centralwidget)
        self.qtStockSelectComboBox.setObjectName(u"qtStockSelectComboBox")

        self.verticalLayout_2.addWidget(self.qtStockSelectComboBox)

        self.qtAddStockPushButton = QPushButton(self.centralwidget)
        self.qtAddStockPushButton.setObjectName(u"qtAddStockPushButton")
        self.qtAddStockPushButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_2.addWidget(self.qtAddStockPushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.qtStockListTableView = QTableView(self.centralwidget)
        self.qtStockListTableView.setObjectName(u"qtStockListTableView")
        self.qtStockListTableView.setMinimumSize(QSize(0, 100))

        self.horizontalLayout_2.addWidget(self.qtStockListTableView)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.qtTradingDataTableView = QTableView(self.centralwidget)
        self.qtTradingDataTableView.setObjectName(u"qtTradingDataTableView")
        self.qtTradingDataTableView.setMinimumSize(QSize(0, 450))
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

        self.qtAddCapitalIncreaseDataPushButton = QPushButton(self.centralwidget)
        self.qtAddCapitalIncreaseDataPushButton.setObjectName(u"qtAddCapitalIncreaseDataPushButton")
        self.qtAddCapitalIncreaseDataPushButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.qtAddCapitalIncreaseDataPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.qtExportAllStockTradingDataPushButton = QPushButton(self.centralwidget)
        self.qtExportAllStockTradingDataPushButton.setObjectName(u"qtExportAllStockTradingDataPushButton")
        self.qtExportAllStockTradingDataPushButton.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.qtExportAllStockTradingDataPushButton)

        self.qtExportSelectedStockTradingDataPushButton = QPushButton(self.centralwidget)
        self.qtExportSelectedStockTradingDataPushButton.setObjectName(u"qtExportSelectedStockTradingDataPushButton")
        self.qtExportSelectedStockTradingDataPushButton.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.qtExportSelectedStockTradingDataPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

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
        self.qtDiscountCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u624b\u7e8c\u8cbb\u6298\u6263", None))
        self.qtExtraInsuranceFeeCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u88dc\u5145\u4fdd\u8cbb", None))
        self.qtAddStockPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u80a1\u7968", None))
        self.qtFromNewToOldRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u7531\u65b0\u5230\u820a", None))
        self.qtFromOldToNewRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u7531\u820a\u5230\u65b0", None))
        self.qtShowAllRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a\u5168\u90e8\u4ea4\u6613\u7d00\u9304", None))
        self.qtShow10RadioButton.setText(QCoreApplication.translate("MainWindow", u"\u986f\u793a10\u7b46\u4ea4\u6613\u7d00\u9304", None))
        self.qtAddTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u4ea4\u6613\u7d00\u9304", None))
        self.qtAddDividendDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u914d\u80a1\u914d\u606f\u7d00\u9304", None))
        self.qtAddCapitalReductionDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u6e1b\u8cc7\u7d00\u9304", None))
        self.qtAddCapitalIncreaseDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u589e\u8cc7\u7d00\u9304", None))
        self.qtExportAllStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u6240\u6709\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
        self.qtExportSelectedStockTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u55ae\u652f\u80a1\u7968\u4ea4\u6613\u7d00\u9304", None))
    # retranslateUi

