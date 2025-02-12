# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockDividendTransferFeeEditSpinboxDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(176, 69)
        Dialog.setMinimumSize(QSize(176, 69))
        Dialog.setMaximumSize(QSize(176, 71))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.qtDividendTransferFeeSpinBox = QSpinBox(Dialog)
        self.qtDividendTransferFeeSpinBox.setObjectName(u"qtDividendTransferFeeSpinBox")
        self.qtDividendTransferFeeSpinBox.setMinimumSize(QSize(60, 0))
        self.qtDividendTransferFeeSpinBox.setMaximumSize(QSize(60, 16777215))
        self.qtDividendTransferFeeSpinBox.setValue(10)

        self.horizontalLayout_2.addWidget(self.qtDividendTransferFeeSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout.addWidget(self.qtOkPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7de8\u8f2f\u532f\u8cbb", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u73fe\u91d1\u80a1\u5229\u532f\u8cbb", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

