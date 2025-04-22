# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtAccountSettingEditDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(337, 483)
        Dialog.setMinimumSize(QSize(300, 0))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qtGroupNameLabel = QLabel(Dialog)
        self.qtGroupNameLabel.setObjectName(u"qtGroupNameLabel")

        self.verticalLayout.addWidget(self.qtGroupNameLabel)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.qtExtraInsuranceCheckBox = QCheckBox(Dialog)
        self.qtExtraInsuranceCheckBox.setObjectName(u"qtExtraInsuranceCheckBox")

        self.horizontalLayout_6.addWidget(self.qtExtraInsuranceCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.qtMinCommonTradingFeeSpinBox = QSpinBox(Dialog)
        self.qtMinCommonTradingFeeSpinBox.setObjectName(u"qtMinCommonTradingFeeSpinBox")
        self.qtMinCommonTradingFeeSpinBox.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_5.addWidget(self.qtMinCommonTradingFeeSpinBox)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.qtMinOddTradingFeeSpinBox = QSpinBox(Dialog)
        self.qtMinOddTradingFeeSpinBox.setObjectName(u"qtMinOddTradingFeeSpinBox")
        self.qtMinOddTradingFeeSpinBox.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_4.addWidget(self.qtMinOddTradingFeeSpinBox)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.qtDiscountImmediateRadioButton = QRadioButton(self.groupBox_3)
        self.qtDiscountImmediateRadioButton.setObjectName(u"qtDiscountImmediateRadioButton")
        self.qtDiscountImmediateRadioButton.setChecked(True)

        self.horizontalLayout_8.addWidget(self.qtDiscountImmediateRadioButton)

        self.qtDiscountPostRadioButton = QRadioButton(self.groupBox_3)
        self.qtDiscountPostRadioButton.setObjectName(u"qtDiscountPostRadioButton")

        self.horizontalLayout_8.addWidget(self.qtDiscountPostRadioButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.qtRoundDownRadioButton = QRadioButton(self.groupBox)
        self.qtRoundDownRadioButton.setObjectName(u"qtRoundDownRadioButton")
        self.qtRoundDownRadioButton.setChecked(True)

        self.horizontalLayout_7.addWidget(self.qtRoundDownRadioButton)

        self.qtRoundOffRadioButton = QRadioButton(self.groupBox)
        self.qtRoundOffRadioButton.setObjectName(u"qtRoundOffRadioButton")

        self.horizontalLayout_7.addWidget(self.qtRoundOffRadioButton)

        self.qtRoundUpRadioButton = QRadioButton(self.groupBox)
        self.qtRoundUpRadioButton.setObjectName(u"qtRoundUpRadioButton")

        self.horizontalLayout_7.addWidget(self.qtRoundUpRadioButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtStockInputLineEdit = QLineEdit(self.groupBox_2)
        self.qtStockInputLineEdit.setObjectName(u"qtStockInputLineEdit")
        self.qtStockInputLineEdit.setMinimumSize(QSize(200, 0))
        self.qtStockInputLineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.qtStockInputLineEdit)

        self.qtAddStockPushButton = QPushButton(self.groupBox_2)
        self.qtAddStockPushButton.setObjectName(u"qtAddStockPushButton")

        self.horizontalLayout.addWidget(self.qtAddStockPushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtStockSelectComboBox = QComboBox(self.groupBox_2)
        self.qtStockSelectComboBox.setObjectName(u"qtStockSelectComboBox")
        self.qtStockSelectComboBox.setMinimumSize(QSize(200, 0))
        self.qtStockSelectComboBox.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.qtStockSelectComboBox)

        self.horizontalSpacer = QSpacerItem(40, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.qtDividendTransferFeeTableView = QTableView(self.groupBox_2)
        self.qtDividendTransferFeeTableView.setObjectName(u"qtDividendTransferFeeTableView")

        self.verticalLayout_2.addWidget(self.qtDividendTransferFeeTableView)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout_2.addWidget(self.qtOkPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.qtGroupNameLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtExtraInsuranceCheckBox.setText(QCoreApplication.translate("Dialog", u"\u88dc\u5145\u4fdd\u8cbb", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6574\u80a1\u4ea4\u6613\u6700\u4f4e\u624b\u7e8c\u8cbb", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5143", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u96f6\u80a1\u4ea4\u6613\u6700\u4f4e\u624b\u7e8c\u8cbb", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5143", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u624b\u7e8c\u8cbb\u6298\u6263\u65b9\u5f0f", None))
        self.qtDiscountImmediateRadioButton.setText(QCoreApplication.translate("Dialog", u"\u5373\u6642\u6298\u6263", None))
        self.qtDiscountPostRadioButton.setText(QCoreApplication.translate("Dialog", u"\u4e8b\u5f8c\u9000\u4f63", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u624b\u7e8c\u8cbb\u5c0f\u6578\u8a08\u7b97", None))
        self.qtRoundDownRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7121\u689d\u4ef6\u6368\u53bb", None))
        self.qtRoundOffRadioButton.setText(QCoreApplication.translate("Dialog", u"\u56db\u6368\u4e94\u5165", None))
        self.qtRoundUpRadioButton.setText(QCoreApplication.translate("Dialog", u"\u7121\u689d\u4ef6\u9032\u5165", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u80a1\u5229\u532f\u8cbb\u8a2d\u5b9a", None))
        self.qtAddStockPushButton.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u80a1\u7968", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6c92\u6709\u7279\u5225\u8a2d\u5b9a\u7684\u516c\u53f8\u7684\u80a1\u5229\u532f\u8cbb\uff0c\u9810\u8a2d\u5c31\u662f10\u5143", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u5132\u5b58", None))
    # retranslateUi

