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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QHBoxLayout,
    QHeaderView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 557)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.qtDiscountRateDoubleSpinBox.setSingleStep(0.100000000000000)
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

        self.qtStockPositionTableView = QTableView(self.centralwidget)
        self.qtStockPositionTableView.setObjectName(u"qtStockPositionTableView")
        self.qtStockPositionTableView.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.qtStockPositionTableView)

        self.qtTradingDataTableView = QTableView(self.centralwidget)
        self.qtTradingDataTableView.setObjectName(u"qtTradingDataTableView")
        self.qtTradingDataTableView.setMinimumSize(QSize(0, 300))

        self.verticalLayout.addWidget(self.qtTradingDataTableView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtAddTradingDataPushButton = QPushButton(self.centralwidget)
        self.qtAddTradingDataPushButton.setObjectName(u"qtAddTradingDataPushButton")

        self.horizontalLayout_3.addWidget(self.qtAddTradingDataPushButton)

        self.qtAddDividendDataPushButton = QPushButton(self.centralwidget)
        self.qtAddDividendDataPushButton.setObjectName(u"qtAddDividendDataPushButton")

        self.horizontalLayout_3.addWidget(self.qtAddDividendDataPushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.qtEditDataPushButton = QPushButton(self.centralwidget)
        self.qtEditDataPushButton.setObjectName(u"qtEditDataPushButton")

        self.verticalLayout.addWidget(self.qtEditDataPushButton)

        self.qtDeleteDataPushButton = QPushButton(self.centralwidget)
        self.qtDeleteDataPushButton.setObjectName(u"qtDeleteDataPushButton")

        self.verticalLayout.addWidget(self.qtDeleteDataPushButton)

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
        self.qtAddTradingDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u4ea4\u6613\u7d00\u9304", None))
        self.qtAddDividendDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u914d\u80a1\u914d\u606f\u7d00\u9304", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u6e1b\u8cc7\u7d00\u9304", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u589e\u8cc7\u7d00\u9304", None))
        self.qtEditDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u7de8\u8f2f", None))
        self.qtDeleteDataPushButton.setText(QCoreApplication.translate("MainWindow", u"\u522a\u9664", None))
    # retranslateUi

