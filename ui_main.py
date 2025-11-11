# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionIklan = QAction(MainWindow)
        self.actionIklan.setObjectName(u"actionIklan")
        self.actionKategori = QAction(MainWindow)
        self.actionKategori.setObjectName(u"actionKategori")
        self.actionKota = QAction(MainWindow)
        self.actionKota.setObjectName(u"actionKota")
        self.actionIMember = QAction(MainWindow)
        self.actionIMember.setObjectName(u"actionIMember")
        self.actionPembayaran = QAction(MainWindow)
        self.actionPembayaran.setObjectName(u"actionPembayaran")
        self.actionPesanInbox = QAction(MainWindow)
        self.actionPesanInbox.setObjectName(u"actionPesanInbox")
        self.actionMember = QAction(MainWindow)
        self.actionMember.setObjectName(u"actionMember")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 17))
        self.menuMenu_Utama = QMenu(self.menubar)
        self.menuMenu_Utama.setObjectName(u"menuMenu_Utama")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Utama.menuAction())
        self.menuMenu_Utama.addSeparator()
        self.menuMenu_Utama.addAction(self.actionIklan)
        self.menuMenu_Utama.addAction(self.actionKategori)
        self.menuMenu_Utama.addAction(self.actionKota)
        self.menuMenu_Utama.addAction(self.actionMember)
        self.menuMenu_Utama.addAction(self.actionPembayaran)
        self.menuMenu_Utama.addAction(self.actionPesanInbox)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionIklan.setText(QCoreApplication.translate("MainWindow", u"Iklan", None))
        self.actionKategori.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        self.actionKota.setText(QCoreApplication.translate("MainWindow", u"Kota", None))
        self.actionIMember.setText(QCoreApplication.translate("MainWindow", u"Member", None))
        self.actionPembayaran.setText(QCoreApplication.translate("MainWindow", u"Pembayaran", None))
        self.actionPesanInbox.setText(QCoreApplication.translate("MainWindow", u"PesanInbox", None))
        self.actionMember.setText(QCoreApplication.translate("MainWindow", u"Member", None))
        self.menuMenu_Utama.setTitle(QCoreApplication.translate("MainWindow", u"Menu Utama", None))
    # retranslateUi

