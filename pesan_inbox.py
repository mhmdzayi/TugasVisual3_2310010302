# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class pesan_inbox(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        ui_file_name = "pesan_inbox.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Tidak bisa membuka {ui_file_name}")
            sys.exit(-1)

        loader = QUiLoader()
        self.formPesan = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.formPesan.btnSimpan.clicked.connect(self.doSimpanPesan)
        self.formPesan.btnUbah.clicked.connect(self.doUbahPesan)
        self.formPesan.btnHapus.clicked.connect(self.doHapusPesan)
        self.formPesan.editCari.textChanged.connect(self.doCariPesan)
        self.formPesan.btnBersih.clicked.connect(self.doBersih) # <-- TAMBAHAN

        self.tampilDataPesan()
        self.setWindowTitle("Data Pesan Inbox")

    def doSimpanPesan(self):
        # ... (kode simpan) ...
        if not self.formPesan.editKdPesan.text().strip():
            QMessageBox.information(None,"Informasi","Kode Pesan belum di isi")
            self.formPesan.editKdPesan.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formPesan.editKdPesan.text()
                tempPengirim = self.formPesan.editNmPengirim.text()
                tempEmail = self.formPesan.editEmailPengirim.text()
                tempIsi = self.formPesan.editIsiPesan.text()
                tempKdMem = self.formPesan.editKdMember.text()

                self.crud.simpanPesan(tempID, tempPengirim, tempEmail, tempIsi, tempKdMem)
                self.tampilDataPesan()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")

    def doUbahPesan(self):
        # ... (kode ubah) ...
        tempID = self.formPesan.editKdPesan.text()
        tempPengirim = self.formPesan.editNmPengirim.text()
        tempEmail = self.formPesan.editEmailPengirim.text()
        tempIsi = self.formPesan.editIsiPesan.text()
        tempKdMem = self.formPesan.editKdMember.text()

        self.crud.ubahPesan(tempID, tempPengirim, tempEmail, tempIsi, tempKdMem)
        self.tampilDataPesan()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusPesan(self):
        # ... (kode hapus) ...
        tempID = self.formPesan.editKdPesan.text()
        self.crud.hapusPesan(tempID)
        self.tampilDataPesan()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    # <-- TAMBAHAN (Fungsi Baru) -->
    def doBersih(self):
        self.formPesan.editKdPesan.clear()
        self.formPesan.editNmPengirim.clear()
        self.formPesan.editEmailPengirim.clear()
        self.formPesan.editIsiPesan.clear()
        self.formPesan.editKdMember.clear()
        self.formPesan.editKdPesan.setFocus()

    def tampilDataPesan(self):
        # ... (kode tampil data) ...
        baris = self.crud.dataPesan()
        self.formPesan.tabelPesan.setRowCount(0)
        for r in baris:
            i = self.formPesan.tabelPesan.rowCount()
            self.formPesan.tabelPesan.insertRow(i)
            self.formPesan.tabelPesan.setItem(i,0,QTableWidgetItem(r["kd_pesan_inb"]))
            self.formPesan.tabelPesan.setItem(i,1,QTableWidgetItem(str(r["tgl_kirim"])))
            self.formPesan.tabelPesan.setItem(i,2,QTableWidgetItem(r["nm_pengirim"]))
            self.formPesan.tabelPesan.setItem(i,3,QTableWidgetItem(r["isi_pesan_inb"]))
            self.formPesan.tabelPesan.setItem(i,4,QTableWidgetItem(r["nm_member"]))

    def doCariPesan(self):
        # ... (kode cari) ...
        cari = self.formPesan.editCari.text()
        baris = self.crud.CariPesan(cari)
        self.formPesan.tabelPesan.setRowCount(0)
        for r in baris:
            i = self.formPesan.tabelPesan.rowCount()
            self.formPesan.tabelPesan.insertRow(i)
            self.formPesan.tabelPesan.setItem(i,0,QTableWidgetItem(r["kd_pesan_inb"]))
            self.formPesan.tabelPesan.setItem(i,1,QTableWidgetItem(str(r["tgl_kirim"])))
            self.formPesan.tabelPesan.setItem(i,2,QTableWidgetItem(r["nm_pengirim"]))
            self.formPesan.tabelPesan.setItem(i,3,QTableWidgetItem(r["isi_pesan_inb"]))
            self.formPesan.tabelPesan.setItem(i,4,QTableWidgetItem(r["nm_member"]))
