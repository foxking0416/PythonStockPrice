# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockRegularTradingEditDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QDoubleSpinBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(308, 358)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(308, 358))
        Dialog.setMaximumSize(QSize(308, 358))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.qtStockNumberLabel = QLabel(Dialog)
        self.qtStockNumberLabel.setObjectName(u"qtStockNumberLabel")

        self.horizontalLayout_12.addWidget(self.qtStockNumberLabel)

        self.qtStockNameLabel = QLabel(Dialog)
        self.qtStockNameLabel.setObjectName(u"qtStockNameLabel")

        self.horizontalLayout_12.addWidget(self.qtStockNameLabel)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.qtDateEdit = QDateEdit(Dialog)
        self.qtDateEdit.setObjectName(u"qtDateEdit")

        self.horizontalLayout.addWidget(self.qtDateEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.qtPriceDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtPriceDoubleSpinBox.setObjectName(u"qtPriceDoubleSpinBox")
        self.qtPriceDoubleSpinBox.setMinimumSize(QSize(75, 0))
        self.qtPriceDoubleSpinBox.setMaximum(9999.989999999999782)
        self.qtPriceDoubleSpinBox.setValue(10.000000000000000)

        self.horizontalLayout_3.addWidget(self.qtPriceDoubleSpinBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.qtOddTradeCountSpinBox = QSpinBox(Dialog)
        self.qtOddTradeCountSpinBox.setObjectName(u"qtOddTradeCountSpinBox")
        self.qtOddTradeCountSpinBox.setEnabled(True)
        self.qtOddTradeCountSpinBox.setMinimumSize(QSize(75, 0))
        self.qtOddTradeCountSpinBox.setMaximum(99999)

        self.horizontalLayout_6.addWidget(self.qtOddTradeCountSpinBox)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.qtVariableFeeRadioButton = QRadioButton(Dialog)
        self.qtVariableFeeRadioButton.setObjectName(u"qtVariableFeeRadioButton")
        self.qtVariableFeeRadioButton.setChecked(True)

        self.horizontalLayout_11.addWidget(self.qtVariableFeeRadioButton)

        self.qtDiscountCheckBox = QCheckBox(Dialog)
        self.qtDiscountCheckBox.setObjectName(u"qtDiscountCheckBox")

        self.horizontalLayout_11.addWidget(self.qtDiscountCheckBox)

        self.qtDiscountRateDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtDiscountRateDoubleSpinBox.setObjectName(u"qtDiscountRateDoubleSpinBox")
        self.qtDiscountRateDoubleSpinBox.setDecimals(1)
        self.qtDiscountRateDoubleSpinBox.setMaximum(10.000000000000000)
        self.qtDiscountRateDoubleSpinBox.setSingleStep(0.500000000000000)

        self.horizontalLayout_11.addWidget(self.qtDiscountRateDoubleSpinBox)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_12 = QSpacerItem(150, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.qtTradingFeeMinimumSpinBox = QSpinBox(Dialog)
        self.qtTradingFeeMinimumSpinBox.setObjectName(u"qtTradingFeeMinimumSpinBox")
        self.qtTradingFeeMinimumSpinBox.setMinimumSize(QSize(50, 0))
        self.qtTradingFeeMinimumSpinBox.setMaximum(20)
        self.qtTradingFeeMinimumSpinBox.setValue(20)

        self.horizontalLayout_5.addWidget(self.qtTradingFeeMinimumSpinBox)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.qtConstantFeeRadioButton = QRadioButton(Dialog)
        self.qtConstantFeeRadioButton.setObjectName(u"qtConstantFeeRadioButton")

        self.horizontalLayout_9.addWidget(self.qtConstantFeeRadioButton)

        self.qtTradingFeeConstantSpinBox = QSpinBox(Dialog)
        self.qtTradingFeeConstantSpinBox.setObjectName(u"qtTradingFeeConstantSpinBox")
        self.qtTradingFeeConstantSpinBox.setMinimumSize(QSize(50, 0))
        self.qtTradingFeeConstantSpinBox.setMaximum(20)
        self.qtTradingFeeConstantSpinBox.setValue(1)

        self.horizontalLayout_9.addWidget(self.qtTradingFeeConstantSpinBox)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.qtTradingValueLineEdit = QLineEdit(Dialog)
        self.qtTradingValueLineEdit.setObjectName(u"qtTradingValueLineEdit")
        self.qtTradingValueLineEdit.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.qtTradingValueLineEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_7.addWidget(self.label_6)

        self.qtFeeLineEdit = QLineEdit(Dialog)
        self.qtFeeLineEdit.setObjectName(u"qtFeeLineEdit")
        self.qtFeeLineEdit.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.qtFeeLineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_10.addWidget(self.label_9)

        self.qtTotalCostLineEdit = QLineEdit(Dialog)
        self.qtTotalCostLineEdit.setObjectName(u"qtTotalCostLineEdit")
        self.qtTotalCostLineEdit.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.qtTotalCostLineEdit)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout_2.addWidget(self.qtOkPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout_2.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5b9a\u671f\u5b9a\u984d\u4ea4\u6613", None))
        self.qtStockNumberLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtStockNameLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4ea4\u6613\u50f9\u683c", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u8cfc\u8cb7\u80a1\u6578", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u80a1", None))
        self.qtVariableFeeRadioButton.setText(QCoreApplication.translate("Dialog", u"\u8b8a\u52d5\u624b\u7e8c\u8cbb", None))
        self.qtDiscountCheckBox.setText(QCoreApplication.translate("Dialog", u"\u624b\u7e8c\u8cbb\u6298\u6263", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u6298", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u624b\u7e8c\u8cbb\u6700\u4f4e", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u5143", None))
        self.qtConstantFeeRadioButton.setText(QCoreApplication.translate("Dialog", u"\u56fa\u5b9a\u624b\u7e8c\u8cbb", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5143", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u91d1\u984d", None))
        self.qtTradingValueLineEdit.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u624b\u7e8c\u8cbb", None))
        self.qtFeeLineEdit.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u7e3d\u984d", None))
        self.qtTotalCostLineEdit.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

