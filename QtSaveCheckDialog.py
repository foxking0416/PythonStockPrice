# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtSaveCheckDialog.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(319, 103)
        Dialog.setMinimumSize(QSize(319, 103))
        Dialog.setMaximumSize(QSize(319, 103))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtSavePushButton = QPushButton(Dialog)
        self.qtSavePushButton.setObjectName(u"qtSavePushButton")

        self.horizontalLayout.addWidget(self.qtSavePushButton)

        self.qtNoSavePushButton = QPushButton(Dialog)
        self.qtNoSavePushButton.setObjectName(u"qtNoSavePushButton")

        self.horizontalLayout.addWidget(self.qtNoSavePushButton)

        self.qtAbortPushButton = QPushButton(Dialog)
        self.qtAbortPushButton.setObjectName(u"qtAbortPushButton")

        self.horizontalLayout.addWidget(self.qtAbortPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u662f\u5426\u8981\u5132\u5b58\u5c1a\u672a\u5b8c\u6210\u7684\u5de5\u4f5c", None))
        self.qtSavePushButton.setText(QCoreApplication.translate("Dialog", u"\u5132\u5b58", None))
        self.qtNoSavePushButton.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8981\u5132\u5b58", None))
        self.qtAbortPushButton.setText(QCoreApplication.translate("Dialog", u"\u653e\u68c4", None))
    # retranslateUi

