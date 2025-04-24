# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockSplitEditDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(192, 175)
        Dialog.setMinimumSize(QSize(192, 175))
        Dialog.setMaximumSize(QSize(192, 175))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qtStockNumberLabel = QLabel(Dialog)
        self.qtStockNumberLabel.setObjectName(u"qtStockNumberLabel")

        self.horizontalLayout_2.addWidget(self.qtStockNumberLabel)

        self.qtStockNameLabel = QLabel(Dialog)
        self.qtStockNameLabel.setObjectName(u"qtStockNameLabel")

        self.horizontalLayout_2.addWidget(self.qtStockNameLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.qtDateEdit = QDateEdit(Dialog)
        self.qtDateEdit.setObjectName(u"qtDateEdit")

        self.horizontalLayout_3.addWidget(self.qtDateEdit)

        self.qtWeekdayLabel = QLabel(Dialog)
        self.qtWeekdayLabel.setObjectName(u"qtWeekdayLabel")

        self.horizontalLayout_3.addWidget(self.qtWeekdayLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.qtStockSplitSpinBox = QSpinBox(Dialog)
        self.qtStockSplitSpinBox.setObjectName(u"qtStockSplitSpinBox")
        self.qtStockSplitSpinBox.setMinimum(2)
        self.qtStockSplitSpinBox.setMaximum(20)

        self.horizontalLayout.addWidget(self.qtStockSplitSpinBox)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout_4.addWidget(self.qtOkPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout_4.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u80a1\u7968\u5206\u62c6", None))
        self.qtStockNumberLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtStockNameLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u65e5\u671f", None))
        self.qtWeekdayLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6bcf\u80a1\u5206\u62c6\u6210", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u80a1", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

