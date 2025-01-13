# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtDuplicateOptionDialog.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(210, 135)
        Dialog.setMinimumSize(QSize(210, 135))
        Dialog.setMaximumSize(QSize(210, 135))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.qtOverWriteRadioButton = QRadioButton(Dialog)
        self.qtOverWriteRadioButton.setObjectName(u"qtOverWriteRadioButton")
        self.qtOverWriteRadioButton.setChecked(True)

        self.verticalLayout.addWidget(self.qtOverWriteRadioButton)

        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u91cd\u8907\u8cc7\u6599\u8655\u7406\u65b9\u5f0f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6709\u76f8\u540c\u7684\u500b\u80a1\u8cc7\u6599\uff0c\u8acb\u9078\u64c7\u8655\u7406\u65b9\u5f0f\n"
"\u6216\u662f\u653e\u68c4\u532f\u5165", None))
        self.qtOverWriteRadioButton.setText(QCoreApplication.translate("Dialog", u"\u8986\u5beb", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u5408\u4f75", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u653e\u68c4\u532f\u5165", None))
    # retranslateUi

