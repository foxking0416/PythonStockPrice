# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtCashTransferEditDialog.ui'
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
    QDialogButtonBox, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

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
        self.qtAccountNameLabel = QLabel(Dialog)
        self.qtAccountNameLabel.setObjectName(u"qtAccountNameLabel")

        self.horizontalLayout.addWidget(self.qtAccountNameLabel)

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
        self.qtTransferInRadioButton = QRadioButton(Dialog)
        self.qtTransferInRadioButton.setObjectName(u"qtTransferInRadioButton")
        self.qtTransferInRadioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.qtTransferInRadioButton)

        self.qtTransferOutRadioButton = QRadioButton(Dialog)
        self.qtTransferOutRadioButton.setObjectName(u"qtTransferOutRadioButton")

        self.horizontalLayout_3.addWidget(self.qtTransferOutRadioButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.qtCashDividendSpinBox = QSpinBox(Dialog)
        self.qtCashDividendSpinBox.setObjectName(u"qtCashDividendSpinBox")
        self.qtCashDividendSpinBox.setMinimumSize(QSize(100, 0))
        self.qtCashDividendSpinBox.setMaximum(999999999)

        self.horizontalLayout_4.addWidget(self.qtCashDividendSpinBox)


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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5165\u91d1/\u51fa\u91d1", None))
        self.qtAccountNameLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u65e5\u671f", None))
        self.qtTransferInRadioButton.setText(QCoreApplication.translate("Dialog", u"\u5165\u91d1", None))
        self.qtTransferOutRadioButton.setText(QCoreApplication.translate("Dialog", u"\u51fa\u91d1", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u91d1\u984d", None))
    # retranslateUi

