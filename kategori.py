# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class kategori(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        ui_file_name = "kategori.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Tidak bisa membuka {ui_file_name}")
            sys.exit(-1)

        loader = QUiLoader()
        self.formKategori = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        # Hubungkan tombol
        self.formKategori.btnSimpan.clicked.connect(self.doSimpanKategori)
        self.formKategori.btnUbah.clicked.connect(self.doUbahKategori)
        self.formKategori.btnHapus.clicked.connect(self.doHapusKategori)
        self.formKategori.editCari.textChanged.connect(self.doCariKategori)
        self.formKategori.btnBersih.clicked.connect(self.doBersih) # <-- TAMBAHAN

        self.tampilDataKategori()
        self.setWindowTitle("Data Kategori")

    def doSimpanKategori(self):
        # ... (Kode simpan Anda di sini, tidak berubah) ...
        if not self.formKategori.editKdKategori.text().strip():
            QMessageBox.information(None,"Informasi","Kode Kategori belum di isi")
            self.formKategori.editKdKategori.setFocus()
        elif not self.formKategori.editNmKategori.text().strip():
            QMessageBox.information(None,"Informasi","Nama Kategori belum di isi")
            self.formKategori.editNmKategori.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formKategori.editKdKategori.text()
                tempNama = self.formKategori.editNmKategori.text()
                self.crud.simpanKategori(tempID, tempNama)
                self.tampilDataKategori()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")

    def doUbahKategori(self):
        # ... (Kode ubah Anda di sini, tidak berubah) ...
        tempID = self.formKategori.editKdKategori.text()
        tempNama = self.formKategori.editNmKategori.text()
        self.crud.ubahKategori(tempID, tempNama)
        self.tampilDataKategori()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusKategori(self):
        # ... (Kode hapus Anda di sini, tidak berubah) ...
        tempID = self.formKategori.editKdKategori.text()
        self.crud.hapusKategori(tempID)
        self.tampilDataKategori()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    # <-- TAMBAHAN (Fungsi Baru) -->
    def doBersih(self):
        self.formKategori.editKdKategori.clear()
        self.formKategori.editNmKategori.clear()
        self.formKategori.editKdKategori.setFocus()

    def tampilDataKategori(self):
        # ... (Kode tampil data Anda di sini, tidak berubah) ...
        baris = self.crud.dataKategori()
        self.formKategori.tabelKategori.setRowCount(0)
        for r in baris:
            i = self.formKategori.tabelKategori.rowCount()
            self.formKategori.tabelKategori.insertRow(i)
            self.formKategori.tabelKategori.setItem(i,0,QTableWidgetItem(r["kd_kategori"]))
            self.formKategori.tabelKategori.setItem(i,1,QTableWidgetItem(r["nm_kategori"]))

    def doCariKategori(self):
        # ... (Kode cari Anda di sini, tidak berubah) ...
        cari = self.formKategori.editCari.text()
        baris = self.crud.CariKategori(cari)
        self.formKategori.tabelKategori.setRowCount(0)
        for r in baris:
            i = self.formKategori.tabelKategori.rowCount()
            self.formKategori.tabelKategori.insertRow(i)
            self.formKategori.tabelKategori.setItem(i,0,QTableWidgetItem(r["kd_kategori"]))
            self.formKategori.tabelKategori.setItem(i,1,QTableWidgetItem(r["nm_kategori"]))

# ... (kode if __name__ == "__main__": opsional) ...
