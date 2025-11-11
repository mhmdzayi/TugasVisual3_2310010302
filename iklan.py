# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class iklan(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        ui_file_name = "iklan.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Tidak bisa membuka {ui_file_name}")
            sys.exit(-1)

        loader = QUiLoader()
        self.formIklan = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.formIklan.btnSimpan.clicked.connect(self.doSimpanIklan)
        self.formIklan.btnUbah.clicked.connect(self.doUbahIklan)
        self.formIklan.btnHapus.clicked.connect(self.doHapusIklan)
        self.formIklan.editCari.textChanged.connect(self.doCariIklan)
        self.formIklan.btnBersih.clicked.connect(self.doBersih) # <-- TAMBAHAN

        self.tampilDataIklan()
        self.setWindowTitle("Data Iklan")

    def doSimpanIklan(self):
        # ... (kode simpan) ...
        if not self.formIklan.editKdIklan.text().strip():
            QMessageBox.information(None,"Informasi","Kode Iklan belum di isi")
            self.formIklan.editKdIklan.setFocus()
        elif not self.formIklan.editJudul.text().strip():
            QMessageBox.information(None,"Informasi","Judul Iklan belum di isi")
            self.formIklan.editJudul.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formIklan.editKdIklan.text()
                tempJudul = self.formIklan.editJudul.text()
                tempHarga = self.formIklan.editHarga.text()
                tempKdKat = self.formIklan.editKdKategori.text()
                tempKdMem = self.formIklan.editKdMember.text()

                self.crud.simpanIklan(tempID, tempJudul, tempHarga, tempKdKat, tempKdMem)
                self.tampilDataIklan()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")

    def doUbahIklan(self):
        # ... (kode ubah) ...
        tempID = self.formIklan.editKdIklan.text()
        tempJudul = self.formIklan.editJudul.text()
        tempHarga = self.formIklan.editHarga.text()
        tempKdKat = self.formIklan.editKdKategori.text()
        tempKdMem = self.formIklan.editKdMember.text()

        self.crud.ubahIklan(tempID, tempJudul, tempHarga, tempKdKat, tempKdMem)
        self.tampilDataIklan()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusIklan(self):
        # ... (kode hapus) ...
        tempID = self.formIklan.editKdIklan.text()
        self.crud.hapusIklan(tempID)
        self.tampilDataIklan()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    # <-- TAMBAHAN (Fungsi Baru) -->
    def doBersih(self):
        self.formIklan.editKdIklan.clear()
        self.formIklan.editJudul.clear()
        self.formIklan.editHarga.clear()
        self.formIklan.editKdKategori.clear()
        self.formIklan.editKdMember.clear()
        self.formIklan.editKdIklan.setFocus()

    def tampilDataIklan(self):
        # ... (kode tampil data) ...
        baris = self.crud.dataIklan()
        self.formIklan.tabelIklan.setRowCount(0)
        for r in baris:
            i = self.formIklan.tabelIklan.rowCount()
            self.formIklan.tabelIklan.insertRow(i)
            self.formIklan.tabelIklan.setItem(i,0,QTableWidgetItem(r["kd_iklan"]))
            self.formIklan.tabelIklan.setItem(i,1,QTableWidgetItem(r["judul_iklan"]))
            self.formIklan.tabelIklan.setItem(i,2,QTableWidgetItem(str(r["harga"])))
            self.formIklan.tabelIklan.setItem(i,3,QTableWidgetItem(r["nm_kategori"]))
            self.formIklan.tabelIklan.setItem(i,4,QTableWidgetItem(r["nm_member"]))

    def doCariIklan(self):
        # ... (kode cari) ...
        cari = self.formIklan.editCari.text()
        baris = self.crud.CariIklan(cari)
        self.formIklan.tabelIklan.setRowCount(0)
        for r in baris:
            i = self.formIklan.tabelIklan.rowCount()
            self.formIklan.tabelIklan.insertRow(i)
            self.formIklan.tabelIklan.setItem(i,0,QTableWidgetItem(r["kd_iklan"]))
            self.formIklan.tabelIklan.setItem(i,1,QTableWidgetItem(r["judul_iklan"]))
            self.formIklan.tabelIklan.setItem(i,2,QTableWidgetItem(str(r["harga"])))
            self.formIklan.tabelIklan.setItem(i,3,QTableWidgetItem(r["nm_kategori"]))
            self.formIklan.tabelIklan.setItem(i,4,QTableWidgetItem(r["nm_member"]))
