# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockDividendEditDialog.ui'
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
    QDoubleSpinBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(380, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(380, 260))
        Dialog.setMaximumSize(QSize(380, 260))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtStockNumberLabel = QLabel(Dialog)
        self.qtStockNumberLabel.setObjectName(u"qtStockNumberLabel")

        self.horizontalLayout.addWidget(self.qtStockNumberLabel)

        self.qtStockNameLabel = QLabel(Dialog)
        self.qtStockNameLabel.setObjectName(u"qtStockNameLabel")

        self.horizontalLayout.addWidget(self.qtStockNameLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.qtDateEdit = QDateEdit(Dialog)
        self.qtDateEdit.setObjectName(u"qtDateEdit")

        self.horizontalLayout_2.addWidget(self.qtDateEdit)

        self.qtWeekdayLabel = QLabel(Dialog)
        self.qtWeekdayLabel.setObjectName(u"qtWeekdayLabel")

        self.horizontalLayout_2.addWidget(self.qtWeekdayLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.qtPerShareDividendRadioButton = QRadioButton(Dialog)
        self.qtPerShareDividendRadioButton.setObjectName(u"qtPerShareDividendRadioButton")
        self.qtPerShareDividendRadioButton.setChecked(True)

        self.verticalLayout.addWidget(self.qtPerShareDividendRadioButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.qtPerShareStockDividendDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtPerShareStockDividendDoubleSpinBox.setObjectName(u"qtPerShareStockDividendDoubleSpinBox")
        self.qtPerShareStockDividendDoubleSpinBox.setMinimumSize(QSize(95, 0))
        self.qtPerShareStockDividendDoubleSpinBox.setDecimals(9)
        self.qtPerShareStockDividendDoubleSpinBox.setMaximum(999.990000000000009)

        self.horizontalLayout_3.addWidget(self.qtPerShareStockDividendDoubleSpinBox)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.qtPerShareCashDividendDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtPerShareCashDividendDoubleSpinBox.setObjectName(u"qtPerShareCashDividendDoubleSpinBox")
        self.qtPerShareCashDividendDoubleSpinBox.setMinimumSize(QSize(95, 0))
        self.qtPerShareCashDividendDoubleSpinBox.setDecimals(9)
        self.qtPerShareCashDividendDoubleSpinBox.setMaximum(999.990000000000009)

        self.horizontalLayout_3.addWidget(self.qtPerShareCashDividendDoubleSpinBox)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.qtTotalDividendRadioButton = QRadioButton(Dialog)
        self.qtTotalDividendRadioButton.setObjectName(u"qtTotalDividendRadioButton")

        self.verticalLayout.addWidget(self.qtTotalDividendRadioButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(48, 0))

        self.horizontalLayout_4.addWidget(self.label_7)

        self.qtTotalStockDividendDoubleSpinBox = QSpinBox(Dialog)
        self.qtTotalStockDividendDoubleSpinBox.setObjectName(u"qtTotalStockDividendDoubleSpinBox")
        self.qtTotalStockDividendDoubleSpinBox.setMinimumSize(QSize(95, 0))
        self.qtTotalStockDividendDoubleSpinBox.setMaximum(999999999)

        self.horizontalLayout_4.addWidget(self.qtTotalStockDividendDoubleSpinBox)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(48, 0))

        self.horizontalLayout_4.addWidget(self.label_6)

        self.qtTotalCashDividendDoubleSpinBox = QSpinBox(Dialog)
        self.qtTotalCashDividendDoubleSpinBox.setObjectName(u"qtTotalCashDividendDoubleSpinBox")
        self.qtTotalCashDividendDoubleSpinBox.setMinimumSize(QSize(95, 0))
        self.qtTotalCashDividendDoubleSpinBox.setMaximum(999999999)

        self.horizontalLayout_4.addWidget(self.qtTotalCashDividendDoubleSpinBox)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.qtCustomExtraInsuranceCheckBox = QCheckBox(Dialog)
        self.qtCustomExtraInsuranceCheckBox.setObjectName(u"qtCustomExtraInsuranceCheckBox")

        self.horizontalLayout_6.addWidget(self.qtCustomExtraInsuranceCheckBox)

        self.qtExtraInsuranceSpinBox = QSpinBox(Dialog)
        self.qtExtraInsuranceSpinBox.setObjectName(u"qtExtraInsuranceSpinBox")
        self.qtExtraInsuranceSpinBox.setMaximum(999999999)

        self.horizontalLayout_6.addWidget(self.qtExtraInsuranceSpinBox)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout_5.addWidget(self.qtOkPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout_5.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u80a1\u5229\u5206\u914d", None))
        self.qtStockNumberLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtStockNameLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u65e5\u671f", None))
        self.qtWeekdayLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtPerShareDividendRadioButton.setText(QCoreApplication.translate("Dialog", u"\u8a2d\u5b9a\u6bcf\u80a1\u80a1\u5229", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6bcf\u80a1\u914d\u80a1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5143", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u6bcf\u80a1\u914d\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5143", None))
        self.qtTotalDividendRadioButton.setText(QCoreApplication.translate("Dialog", u"\u8a2d\u5b9a\u7e3d\u80a1\u5229", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u7e3d\u914d\u80a1", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u80a1", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u7e3d\u914d\u606f", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u5143", None))
        self.qtCustomExtraInsuranceCheckBox.setText(QCoreApplication.translate("Dialog", u"\u624b\u52d5\u8a2d\u5b9a\u88dc\u5145\u4fdd\u8cbb", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u5143", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

