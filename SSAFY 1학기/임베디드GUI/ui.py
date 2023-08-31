# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(514, 434)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 130, 271, 71))
        self.progressBar.setValue(24)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(98, 220, 261, 71))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btngo = QPushButton(self.widget)
        self.btngo.setObjectName(u"btngo")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btngo.sizePolicy().hasHeightForWidth())
        self.btngo.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btngo)

        self.btnPause = QPushButton(self.widget)
        self.btnPause.setObjectName(u"btnPause")
        sizePolicy.setHeightForWidth(self.btnPause.sizePolicy().hasHeightForWidth())
        self.btnPause.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btnPause)

        self.btnReset = QPushButton(self.widget)
        self.btnReset.setObjectName(u"btnReset")
        sizePolicy.setHeightForWidth(self.btnReset.sizePolicy().hasHeightForWidth())
        self.btnReset.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btnReset)


        self.retranslateUi(Form)
        self.btngo.clicked.connect(Form.go)
        self.btnPause.clicked.connect(Form.pause)
        self.btnReset.clicked.connect(Form.reset)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btngo.setText(QCoreApplication.translate("Form", u"GO", None))
        self.btnPause.setText(QCoreApplication.translate("Form", u"Pause", None))
        self.btnReset.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

