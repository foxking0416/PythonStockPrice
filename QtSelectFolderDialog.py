# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtSelectFolderDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(412, 74)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qtFolderPathLineEdit = QLineEdit(Dialog)
        self.qtFolderPathLineEdit.setObjectName(u"qtFolderPathLineEdit")
        self.qtFolderPathLineEdit.setEnabled(False)
        self.qtFolderPathLineEdit.setMinimumSize(QSize(220, 0))

        self.horizontalLayout.addWidget(self.qtFolderPathLineEdit)

        self.qtSelectPushButton = QPushButton(Dialog)
        self.qtSelectPushButton.setObjectName(u"qtSelectPushButton")
        self.qtSelectPushButton.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.qtSelectPushButton)

        self.qtReturnToDefaultPushButton = QPushButton(Dialog)
        self.qtReturnToDefaultPushButton.setObjectName(u"qtReturnToDefaultPushButton")
        self.qtReturnToDefaultPushButton.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.qtReturnToDefaultPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qtOkPushButton = QPushButton(Dialog)
        self.qtOkPushButton.setObjectName(u"qtOkPushButton")

        self.horizontalLayout_2.addWidget(self.qtOkPushButton)

        self.qtCancelPushButton = QPushButton(Dialog)
        self.qtCancelPushButton.setObjectName(u"qtCancelPushButton")

        self.horizontalLayout_2.addWidget(self.qtCancelPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u9078\u53d6\u66ab\u5b58\u6a94\u4f4d\u7f6e", None))
        self.qtSelectPushButton.setText(QCoreApplication.translate("Dialog", u"\u9078\u64c7\u8cc7\u6599\u593e", None))
        self.qtReturnToDefaultPushButton.setText(QCoreApplication.translate("Dialog", u"\u56de\u5230\u9810\u8a2d\u503c", None))
        self.qtOkPushButton.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
        self.qtCancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

