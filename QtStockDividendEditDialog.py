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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(185, 157)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(185, 185))
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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.qtStockDividendDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtStockDividendDoubleSpinBox.setObjectName(u"qtStockDividendDoubleSpinBox")
        self.qtStockDividendDoubleSpinBox.setMinimumSize(QSize(75, 0))
        self.qtStockDividendDoubleSpinBox.setDecimals(9)
        self.qtStockDividendDoubleSpinBox.setMaximum(999.990000000000009)

        self.horizontalLayout_3.addWidget(self.qtStockDividendDoubleSpinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.qtCashDividendDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtCashDividendDoubleSpinBox.setObjectName(u"qtCashDividendDoubleSpinBox")
        self.qtCashDividendDoubleSpinBox.setMinimumSize(QSize(75, 0))
        self.qtCashDividendDoubleSpinBox.setDecimals(9)
        self.qtCashDividendDoubleSpinBox.setMaximum(999.990000000000009)

        self.horizontalLayout_4.addWidget(self.qtCashDividendDoubleSpinBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.qtOkButtonBox = QDialogButtonBox(Dialog)
        self.qtOkButtonBox.setObjectName(u"qtOkButtonBox")
        self.qtOkButtonBox.setLayoutDirection(Qt.LeftToRight)
        self.qtOkButtonBox.setOrientation(Qt.Horizontal)
        self.qtOkButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.qtOkButtonBox)


        self.retranslateUi(Dialog)
        self.qtOkButtonBox.accepted.connect(Dialog.accept)
        self.qtOkButtonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u80a1\u5229\u5206\u914d", None))
        self.qtStockNumberLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtStockNameLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u65e5\u671f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u914d\u80a1", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u914d\u606f", None))
    # retranslateUi

