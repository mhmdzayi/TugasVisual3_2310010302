# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kota.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(370, 340)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 351, 51))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelKdKota = QLabel(self.formLayoutWidget)
        self.labelKdKota.setObjectName(u"labelKdKota")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelKdKota)

        self.editKdKota = QLineEdit(self.formLayoutWidget)
        self.editKdKota.setObjectName(u"editKdKota")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editKdKota)

        self.labelNamaKota = QLabel(self.formLayoutWidget)
        self.labelNamaKota.setObjectName(u"labelNamaKota")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelNamaKota)

        self.editNamaKota = QLineEdit(self.formLayoutWidget)
        self.editNamaKota.setObjectName(u"editNamaKota")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNamaKota)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 70, 111, 25))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(130, 70, 111, 25))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(250, 70, 111, 25))
        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(130, 100, 111, 25))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 130, 351, 25))
        self.tabelKota = QTableWidget(Form)
        if (self.tabelKota.columnCount() < 2):
            self.tabelKota.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelKota.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelKota.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabelKota.setObjectName(u"tabelKota")
        self.tabelKota.setGeometry(QRect(10, 160, 351, 151))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Kota", None))
        self.labelKdKota.setText(QCoreApplication.translate("Form", u"Kode Kota", None))
        self.labelNamaKota.setText(QCoreApplication.translate("Form", u"Nama Kota", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("Form", u"Ketik untuk mencari...", None))
        ___qtablewidgetitem = self.tabelKota.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode Kota", None));
        ___qtablewidgetitem1 = self.tabelKota.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Kota", None));
    # retranslateUi

