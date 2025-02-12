# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockDividendTransferFeeEditDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 420)
        Dialog.setMinimumSize(QSize(300, 0))
        Dialog.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qtGroupNameLabel = QLabel(Dialog)
        self.qtGroupNameLabel.setObjectName(u"qtGroupNameLabel")

        self.verticalLayout.addWidget(self.qtGroupNameLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtStockInputLineEdit = QLineEdit(Dialog)
        self.qtStockInputLineEdit.setObjectName(u"qtStockInputLineEdit")
        self.qtStockInputLineEdit.setMinimumSize(QSize(200, 0))
        self.qtStockInputLineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.qtStockInputLineEdit)

        self.qtAddStockPushButton = QPushButton(Dialog)
        self.qtAddStockPushButton.setObjectName(u"qtAddStockPushButton")

        self.horizontalLayout.addWidget(self.qtAddStockPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtStockSelectComboBox = QComboBox(Dialog)
        self.qtStockSelectComboBox.setObjectName(u"qtStockSelectComboBox")
        self.qtStockSelectComboBox.setMinimumSize(QSize(200, 0))
        self.qtStockSelectComboBox.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.qtStockSelectComboBox)

        self.horizontalSpacer = QSpacerItem(40, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.qtDividendTransferFeeTableView = QTableView(Dialog)
        self.qtDividendTransferFeeTableView.setObjectName(u"qtDividendTransferFeeTableView")

        self.verticalLayout.addWidget(self.qtDividendTransferFeeTableView)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u80a1\u5229\u532f\u8cbb\u8a2d\u5b9a", None))
        self.qtGroupNameLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtAddStockPushButton.setText(QCoreApplication.translate("Dialog", u"\u65b0\u589e\u80a1\u7968", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
    # retranslateUi

