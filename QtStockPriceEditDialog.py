# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockPriceEditDialog.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QLineEdit, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.qtDateEdit = QDateEdit(Dialog)
        self.qtDateEdit.setObjectName(u"qtDateEdit")
        self.qtDateEdit.setGeometry(QRect(20, 20, 110, 22))
        self.qtBuyRadioButton = QRadioButton(Dialog)
        self.qtBuyRadioButton.setObjectName(u"qtBuyRadioButton")
        self.qtBuyRadioButton.setGeometry(QRect(30, 60, 83, 16))
        self.qtSellRadioButton = QRadioButton(Dialog)
        self.qtSellRadioButton.setObjectName(u"qtSellRadioButton")
        self.qtSellRadioButton.setGeometry(QRect(30, 80, 83, 16))
        self.qtPriceDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtPriceDoubleSpinBox.setObjectName(u"qtPriceDoubleSpinBox")
        self.qtPriceDoubleSpinBox.setGeometry(QRect(30, 110, 91, 22))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 190, 113, 20))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 240, 113, 20))
        self.doubleSpinBox = QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(30, 140, 101, 22))
        self.doubleSpinBox.setDecimals(3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.qtBuyRadioButton.setText(QCoreApplication.translate("Dialog", u"\u8cb7", None))
        self.qtSellRadioButton.setText(QCoreApplication.translate("Dialog", u"\u8ce3", None))
    # retranslateUi

