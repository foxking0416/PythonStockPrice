# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtStockCapitalIncreaseEditDialog.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(255, 201)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.qtStockNumberLabel = QLabel(Dialog)
        self.qtStockNumberLabel.setObjectName(u"qtStockNumberLabel")

        self.horizontalLayout_12.addWidget(self.qtStockNumberLabel)

        self.qtStockNameLabel = QLabel(Dialog)
        self.qtStockNameLabel.setObjectName(u"qtStockNameLabel")

        self.horizontalLayout_12.addWidget(self.qtStockNameLabel)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.qtDateEdit = QDateEdit(Dialog)
        self.qtDateEdit.setObjectName(u"qtDateEdit")

        self.horizontalLayout.addWidget(self.qtDateEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.qtPriceDoubleSpinBox = QDoubleSpinBox(Dialog)
        self.qtPriceDoubleSpinBox.setObjectName(u"qtPriceDoubleSpinBox")
        self.qtPriceDoubleSpinBox.setMinimumSize(QSize(75, 0))
        self.qtPriceDoubleSpinBox.setMaximum(9999.989999999999782)
        self.qtPriceDoubleSpinBox.setValue(10.000000000000000)

        self.horizontalLayout_3.addWidget(self.qtPriceDoubleSpinBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.qtOddTradeCountSpinBox = QSpinBox(self.groupBox)
        self.qtOddTradeCountSpinBox.setObjectName(u"qtOddTradeCountSpinBox")
        self.qtOddTradeCountSpinBox.setEnabled(True)
        self.qtOddTradeCountSpinBox.setMinimumSize(QSize(75, 0))
        self.qtOddTradeCountSpinBox.setMaximum(99999)

        self.horizontalLayout_6.addWidget(self.qtOddTradeCountSpinBox)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_10.addWidget(self.label_9)

        self.qtTotalCostLineEdit = QLineEdit(Dialog)
        self.qtTotalCostLineEdit.setObjectName(u"qtTotalCostLineEdit")
        self.qtTotalCostLineEdit.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.qtTotalCostLineEdit)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u80a1\u7968\u8a8d\u8cfc", None))
        self.qtStockNumberLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.qtStockNameLabel.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4ea4\u6613\u50f9\u683c", None))
        self.groupBox.setTitle("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"   \u80a1", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u7e3d\u984d", None))
        self.qtTotalCostLineEdit.setText(QCoreApplication.translate("Dialog", u"0", None))
    # retranslateUi

