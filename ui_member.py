# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'member.ui'
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
        self.labelKdMember = QLabel(self.formLayoutWidget)
        self.labelKdMember.setObjectName(u"labelKdMember")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelKdMember)

        self.editKdMember = QLineEdit(self.formLayoutWidget)
        self.editKdMember.setObjectName(u"editKdMember")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editKdMember)

        self.labelNmMember = QLabel(self.formLayoutWidget)
        self.labelNmMember.setObjectName(u"labelNmMember")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelNmMember)

        self.editNmMember = QLineEdit(self.formLayoutWidget)
        self.editNmMember.setObjectName(u"editNmMember")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNmMember)

        self.labelEmail = QLabel(self.formLayoutWidget)
        self.labelEmail.setObjectName(u"labelEmail")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelEmail)

        self.editEmail = QLineEdit(self.formLayoutWidget)
        self.editEmail.setObjectName(u"editEmail")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editEmail)

        self.labelHpTelp = QLabel(self.formLayoutWidget)
        self.labelHpTelp.setObjectName(u"labelHpTelp")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelHpTelp)

        self.editHpTelp = QLineEdit(self.formLayoutWidget)
        self.editHpTelp.setObjectName(u"editHpTelp")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editHpTelp)

        self.labelKdKota = QLabel(self.formLayoutWidget)
        self.labelKdKota.setObjectName(u"labelKdKota")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.labelKdKota)

        self.editKdKota = QLineEdit(self.formLayoutWidget)
        self.editKdKota.setObjectName(u"editKdKota")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editKdKota)

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
        self.tabelMember = QTableWidget(Form)
        if (self.tabelMember.columnCount() < 5):
            self.tabelMember.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelMember.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelMember.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelMember.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelMember.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelMember.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelMember.setObjectName(u"tabelMember")
        self.tabelMember.setGeometry(QRect(10, 230, 401, 171))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Member", None))
        self.labelKdMember.setText(QCoreApplication.translate("Form", u"Kode Member", None))
        self.labelNmMember.setText(QCoreApplication.translate("Form", u"Nama Member", None))
        self.labelEmail.setText(QCoreApplication.translate("Form", u"Email", None))
        self.labelHpTelp.setText(QCoreApplication.translate("Form", u"No. HP / Telepon", None))
        self.labelKdKota.setText(QCoreApplication.translate("Form", u"Kode Kota ", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("Form", u"Ketik untuk mencari...", None))
        ___qtablewidgetitem = self.tabelMember.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Member", None));
        ___qtablewidgetitem1 = self.tabelMember.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelMember.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem3 = self.tabelMember.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"No. Telp", None));
        ___qtablewidgetitem4 = self.tabelMember.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Kota", None));
    # retranslateUi

