# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pesan_inbox.ui'
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
        self.labelKdPesan = QLabel(self.formLayoutWidget)
        self.labelKdPesan.setObjectName(u"labelKdPesan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelKdPesan)

        self.editKdPesan = QLineEdit(self.formLayoutWidget)
        self.editKdPesan.setObjectName(u"editKdPesan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editKdPesan)

        self.labelNmPengirim = QLabel(self.formLayoutWidget)
        self.labelNmPengirim.setObjectName(u"labelNmPengirim")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelNmPengirim)

        self.editNmPengirim = QLineEdit(self.formLayoutWidget)
        self.editNmPengirim.setObjectName(u"editNmPengirim")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNmPengirim)

        self.labelEmailPengirim = QLabel(self.formLayoutWidget)
        self.labelEmailPengirim.setObjectName(u"labelEmailPengirim")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelEmailPengirim)

        self.editEmailPengirim = QLineEdit(self.formLayoutWidget)
        self.editEmailPengirim.setObjectName(u"editEmailPengirim")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editEmailPengirim)

        self.labelIsiPesan = QLabel(self.formLayoutWidget)
        self.labelIsiPesan.setObjectName(u"labelIsiPesan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelIsiPesan)

        self.editIsiPesan = QLineEdit(self.formLayoutWidget)
        self.editIsiPesan.setObjectName(u"editIsiPesan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editIsiPesan)

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
        self.tabelPesan = QTableWidget(Form)
        if (self.tabelPesan.columnCount() < 5):
            self.tabelPesan.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPesan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPesan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPesan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPesan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelPesan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelPesan.setObjectName(u"tabelPesan")
        self.tabelPesan.setGeometry(QRect(10, 230, 401, 171))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Pesan Inbox", None))
        self.labelKdPesan.setText(QCoreApplication.translate("Form", u"Kode Pesan", None))
        self.labelNmPengirim.setText(QCoreApplication.translate("Form", u"Nama Pengirim", None))
        self.labelEmailPengirim.setText(QCoreApplication.translate("Form", u"Email Pengirim", None))
        self.labelIsiPesan.setText(QCoreApplication.translate("Form", u"Isi Pesan", None))
        self.labelKdMember.setText(QCoreApplication.translate("Form", u"Kode Member", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("Form", u"Ketik untuk mencari...", None))
        ___qtablewidgetitem = self.tabelPesan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Pesan", None));
        ___qtablewidgetitem1 = self.tabelPesan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tanggal", None));
        ___qtablewidgetitem2 = self.tabelPesan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Pengirim", None));
        ___qtablewidgetitem3 = self.tabelPesan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Isi Pesan", None));
        ___qtablewidgetitem4 = self.tabelPesan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Member", None));
    # retranslateUi

