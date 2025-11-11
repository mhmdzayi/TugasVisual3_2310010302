# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# 1. Import semua form (dengan nama class huruf kecil)
from iklan import iklan
from kategori import kategori
from kota import kota
from member import member
from pembayaran import pembayaran
from pesan_inbox import pesan_inbox

# 2. Samakan nama class utama
class halamanUtama(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # variabel untuk menampung file main.ui
        fileformutama = QFile("main.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        fileformutama.open(QFile.ReadOnly)
        # membuat objek loader Ui
        formloader = QUiLoader()
        self.formutama = formloader.load(fileformutama,self)
        self.setMenuBar(self.formutama.menuBar())
        self.resize(self.formutama.size())

        # 3. Hubungkan menu action (PASTIKAN NAMA INI ADA DI main.ui ANDA)
        self.formutama.actionIklan.triggered.connect(self.buka_iklan)
        self.formutama.actionKategori.triggered.connect(self.buka_kategori)
        self.formutama.actionKota.triggered.connect(self.buka_kota)
        self.formutama.actionMember.triggered.connect(self.buka_member)
        self.formutama.actionPembayaran.triggered.connect(self.buka_pembayaran)
        self.formutama.actionPesanInbox.triggered.connect(self.buka_pesan_inbox)

    # 4. Samakan struktur fungsi 'buka...'
    # Cukup .show() pada objeknya
    def buka_iklan(self):
        self.window_iklan = iklan()
        self.window_iklan.show()

    def buka_kategori(self):
        self.window_kategori = kategori()
        self.window_kategori.show()

    def buka_kota(self):
        self.window_kota = kota()
        self.window_kota.show()

    def buka_member(self):
        self.window_member = member()
        self.window_member.show()

    def buka_pembayaran(self):
        self.window_pembayaran = pembayaran()
        self.window_pembayaran.show()

    def buka_pesan_inbox(self):
        self.window_pesan_inbox = pesan_inbox()
        self.window_pesan_inbox.show()


# 5. Samakan struktur __main__
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = halamanUtama()
    widget.show()
    sys.exit(app.exec())
