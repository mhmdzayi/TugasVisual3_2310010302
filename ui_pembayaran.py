# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pembayaran.ui'
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
        Form.resize(420, 480)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 401, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelIdBayar = QLabel(self.formLayoutWidget)
        self.labelIdBayar.setObjectName(u"labelIdBayar")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelIdBayar)

        self.editIdBayar = QLineEdit(self.formLayoutWidget)
        self.editIdBayar.setObjectName(u"editIdBayar")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editIdBayar)

        self.labelBiaya = QLabel(self.formLayoutWidget)
        self.labelBiaya.setObjectName(u"labelBiaya")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelBiaya)

        self.editBiaya = QLineEdit(self.formLayoutWidget)
        self.editBiaya.setObjectName(u"editBiaya")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editBiaya)

        self.labelRekTujuan = QLabel(self.formLayoutWidget)
        self.labelRekTujuan.setObjectName(u"labelRekTujuan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelRekTujuan)

        self.editRekTujuan = QLineEdit(self.formLayoutWidget)
        self.editRekTujuan.setObjectName(u"editRekTujuan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editRekTujuan)

        self.labelNamaRek = QLabel(self.formLayoutWidget)
        self.labelNamaRek.setObjectName(u"labelNamaRek")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelNamaRek)

        self.editNamaRek = QLineEdit(self.formLayoutWidget)
        self.editNamaRek.setObjectName(u"editNamaRek")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editNamaRek)

        self.labelNominal = QLabel(self.formLayoutWidget)
        self.labelNominal.setObjectName(u"labelNominal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.labelNominal)

        self.editNominal = QLineEdit(self.formLayoutWidget)
        self.editNominal.setObjectName(u"editNominal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editNominal)

        self.labelKdIklan = QLabel(self.formLayoutWidget)
        self.labelKdIklan.setObjectName(u"labelKdIklan")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.labelKdIklan)

        self.editKdIklan = QLineEdit(self.formLayoutWidget)
        self.editKdIklan.setObjectName(u"editKdIklan")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editKdIklan)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 160, 131, 25))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(145, 160, 131, 25))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 160, 131, 25))
        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(145, 190, 131, 25))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 220, 401, 25))
        self.tabelPembayaran = QTableWidget(Form)
        if (self.tabelPembayaran.columnCount() < 5):
            self.tabelPembayaran.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelPembayaran.setObjectName(u"tabelPembayaran")
        self.tabelPembayaran.setGeometry(QRect(10, 250, 401, 171))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Pembayaran", None))
        self.labelIdBayar.setText(QCoreApplication.translate("Form", u"ID Bayar", None))
        self.labelBiaya.setText(QCoreApplication.translate("Form", u"Biaya Iklan", None))
        self.labelRekTujuan.setText(QCoreApplication.translate("Form", u"Rek Tujuan", None))
        self.labelNamaRek.setText(QCoreApplication.translate("Form", u"Nama Rekening", None))
        self.labelNominal.setText(QCoreApplication.translate("Form", u"Nominal Transfer", None))
        self.labelKdIklan.setText(QCoreApplication.translate("Form", u"Kode Iklan", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("Form", u"Ketik untuk mencari...", None))
        ___qtablewidgetitem = self.tabelPembayaran.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Bayar", None));
        ___qtablewidgetitem1 = self.tabelPembayaran.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nominal", None));
        ___qtablewidgetitem2 = self.tabelPembayaran.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nama Rek", None));
        ___qtablewidgetitem3 = self.tabelPembayaran.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Rek Tujuan", None));
        ___qtablewidgetitem4 = self.tabelPembayaran.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Iklan", None));
    # retranslateUi

