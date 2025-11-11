# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iklan.ui'
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
        Form.resize(420, 450)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 401, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelKdIklan = QLabel(self.formLayoutWidget)
        self.labelKdIklan.setObjectName(u"labelKdIklan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelKdIklan)

        self.editKdIklan = QLineEdit(self.formLayoutWidget)
        self.editKdIklan.setObjectName(u"editKdIklan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editKdIklan)

        self.labelJudul = QLabel(self.formLayoutWidget)
        self.labelJudul.setObjectName(u"labelJudul")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelJudul)

        self.editJudul = QLineEdit(self.formLayoutWidget)
        self.editJudul.setObjectName(u"editJudul")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editJudul)

        self.labelHarga = QLabel(self.formLayoutWidget)
        self.labelHarga.setObjectName(u"labelHarga")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelHarga)

        self.editHarga = QLineEdit(self.formLayoutWidget)
        self.editHarga.setObjectName(u"editHarga")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editHarga)

        self.labelKdKategori = QLabel(self.formLayoutWidget)
        self.labelKdKategori.setObjectName(u"labelKdKategori")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelKdKategori)

        self.editKdKategori = QLineEdit(self.formLayoutWidget)
        self.editKdKategori.setObjectName(u"editKdKategori")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editKdKategori)

        self.labelKdMember = QLabel(self.formLayoutWidget)
        self.labelKdMember.setObjectName(u"labelKdMember")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.labelKdMember)

        self.editKdMember = QLineEdit(self.formLayoutWidget)
        self.editKdMember.setObjectName(u"editKdMember")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editKdMember)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 140, 131, 25))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(145, 140, 131, 25))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 140, 131, 25))
        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(145, 170, 131, 25))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 200, 401, 25))
        self.tabelIklan = QTableWidget(Form)
        if (self.tabelIklan.columnCount() < 5):
            self.tabelIklan.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelIklan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelIklan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelIklan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelIklan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelIklan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelIklan.setObjectName(u"tabelIklan")
        self.tabelIklan.setGeometry(QRect(10, 230, 401, 171))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Iklan", None))
        self.labelKdIklan.setText(QCoreApplication.translate("Form", u"Kode Iklan", None))
        self.labelJudul.setText(QCoreApplication.translate("Form", u"Judul Iklan", None))
        self.labelHarga.setText(QCoreApplication.translate("Form", u"Harga", None))
        self.labelKdKategori.setText(QCoreApplication.translate("Form", u"Kode Kategori", None))
        self.labelKdMember.setText(QCoreApplication.translate("Form", u"Kode Member", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("Form", u"Ketik untuk mencari...", None))
        ___qtablewidgetitem = self.tabelIklan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Iklan", None));
        ___qtablewidgetitem1 = self.tabelIklan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Judul", None));
        ___qtablewidgetitem2 = self.tabelIklan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Harga", None));
        ___qtablewidgetitem3 = self.tabelIklan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Kategori", None));
        ___qtablewidgetitem4 = self.tabelIklan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Member", None));
    # retranslateUi

