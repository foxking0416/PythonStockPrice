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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(325, 174)
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

        self.qtOkButtonBox = QDialogButtonBox(Dialog)
        self.qtOkButtonBox.setObjectName(u"qtOkButtonBox")
        self.qtOkButtonBox.setOrientation(Qt.Horizontal)
        self.qtOkButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.qtOkButtonBox)


        self.retranslateUi(Dialog)
        self.qtOkButtonBox.accepted.connect(Dialog.accept)
        self.qtOkButtonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6709\u76f8\u540c\u7684\u500b\u80a1\u8cc7\u6599\uff0c\u8acb\u9078\u64c7\u5c0d\u61c9\u65b9\u5f0f", None))
        self.qtOverWriteRadioButton.setText(QCoreApplication.translate("Dialog", u"\u8986\u5beb", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u5408\u4f75", None))
    # retranslateUi

