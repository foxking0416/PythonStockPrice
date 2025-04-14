# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtShowItemEditDialog.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(453, 439)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.qtShowListWidget = QListWidget(Dialog)
        self.qtShowListWidget.setObjectName(u"qtShowListWidget")

        self.verticalLayout_3.addWidget(self.qtShowListWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.qtHideSelectToolButton = QToolButton(Dialog)
        self.qtHideSelectToolButton.setObjectName(u"qtHideSelectToolButton")

        self.horizontalLayout_3.addWidget(self.qtHideSelectToolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.qtShowSelectToolButton = QToolButton(Dialog)
        self.qtShowSelectToolButton.setObjectName(u"qtShowSelectToolButton")

        self.horizontalLayout_4.addWidget(self.qtShowSelectToolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.qtHideAllToolButton = QToolButton(Dialog)
        self.qtHideAllToolButton.setObjectName(u"qtHideAllToolButton")

        self.verticalLayout_2.addWidget(self.qtHideAllToolButton)

        self.qtShowAllToolButton = QToolButton(Dialog)
        self.qtShowAllToolButton.setObjectName(u"qtShowAllToolButton")

        self.verticalLayout_2.addWidget(self.qtShowAllToolButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.qtHideListWidget = QListWidget(Dialog)
        self.qtHideListWidget.setObjectName(u"qtHideListWidget")

        self.verticalLayout_4.addWidget(self.qtHideListWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 0);")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.qtResetToDefaultPushButton = QPushButton(Dialog)
        self.qtResetToDefaultPushButton.setObjectName(u"qtResetToDefaultPushButton")

        self.horizontalLayout_5.addWidget(self.qtResetToDefaultPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7de8\u8f2f\u986f\u793a\u9805\u76ee", None))
#if QT_CONFIG(tooltip)
        Dialog.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Dialog", u"\u986f\u793a\u9805\u76ee", None))
#if QT_CONFIG(tooltip)
        self.qtHideSelectToolButton.setToolTip(QCoreApplication.translate("Dialog", u"\u96b1\u85cf\u6240\u9078\u9805\u76ee", None))
#endif // QT_CONFIG(tooltip)
        self.qtHideSelectToolButton.setText(QCoreApplication.translate("Dialog", u">", None))
#if QT_CONFIG(tooltip)
        self.qtShowSelectToolButton.setToolTip(QCoreApplication.translate("Dialog", u"\u986f\u793a\u6240\u9078\u9805\u76ee", None))
#endif // QT_CONFIG(tooltip)
        self.qtShowSelectToolButton.setText(QCoreApplication.translate("Dialog", u"<", None))
#if QT_CONFIG(tooltip)
        self.qtHideAllToolButton.setToolTip(QCoreApplication.translate("Dialog", u"\u96b1\u85cf\u6240\u6709\u9805\u76ee", None))
#endif // QT_CONFIG(tooltip)
        self.qtHideAllToolButton.setText(QCoreApplication.translate("Dialog", u">>", None))
#if QT_CONFIG(tooltip)
        self.qtShowAllToolButton.setToolTip(QCoreApplication.translate("Dialog", u"\u986f\u793a\u6240\u6709\u9805\u76ee", None))
#endif // QT_CONFIG(tooltip)
        self.qtShowAllToolButton.setText(QCoreApplication.translate("Dialog", u"<<", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u96b1\u85cf\u9805\u76ee", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u4e0b\u62d6\u79fb\u986f\u793a\u9805\u76ee\u7269\u4ef6\u6539\u8b8a\u986f\u793a\u9806\u5e8f", None))
        self.qtResetToDefaultPushButton.setText(QCoreApplication.translate("Dialog", u"  \u56de\u5230\u9810\u8a2d\u503c  ", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

