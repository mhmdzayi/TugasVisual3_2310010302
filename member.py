# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class member(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        ui_file_name = "member.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Tidak bisa membuka {ui_file_name}")
            sys.exit(-1)

        loader = QUiLoader()
        self.formMember = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.formMember.btnSimpan.clicked.connect(self.doSimpanMember)
        self.formMember.btnUbah.clicked.connect(self.doUbahMember)
        self.formMember.btnHapus.clicked.connect(self.doHapusMember)
        self.formMember.editCari.textChanged.connect(self.doCariMember)
        self.formMember.btnBersih.clicked.connect(self.doBersih) # <-- TAMBAHAN

        self.tampilDataMember()
        self.setWindowTitle("Data Member")

    def doSimpanMember(self):
        # ... (kode simpan) ...
        if not self.formMember.editKdMember.text().strip():
            QMessageBox.information(None,"Informasi","Kode Member belum di isi")
            self.formMember.editKdMember.setFocus()
        elif not self.formMember.editNmMember.text().strip():
            QMessageBox.information(None,"Informasi","Nama Member belum di isi")
            self.formMember.editNmMember.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formMember.editKdMember.text()
                tempNama = self.formMember.editNmMember.text()
                tempEmail = self.formMember.editEmail.text()
                tempHP = self.formMember.editHpTelp.text()
                tempKdKota = self.formMember.editKdKota.text()

                self.crud.simpanMember(tempID, tempNama, tempEmail, tempHP, tempKdKota)
                self.tampilDataMember()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")

    def doUbahMember(self):
        # ... (kode ubah) ...
        tempID = self.formMember.editKdMember.text()
        tempNama = self.formMember.editNmMember.text()
        tempEmail = self.formMember.editEmail.text()
        tempHP = self.formMember.editHpTelp.text()
        tempKdKota = self.formMember.editKdKota.text()

        self.crud.ubahMember(tempID, tempNama, tempEmail, tempHP, tempKdKota)
        self.tampilDataMember()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusMember(self):
        # ... (kode hapus) ...
        tempID = self.formMember.editKdMember.text()
        self.crud.hapusMember(tempID)
        self.tampilDataMember()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    # <-- TAMBAHAN (Fungsi Baru) -->
    def doBersih(self):
        self.formMember.editKdMember.clear()
        self.formMember.editNmMember.clear()
        self.formMember.editEmail.clear()
        self.formMember.editHpTelp.clear()
        self.formMember.editKdKota.clear()
        self.formMember.editKdMember.setFocus()

    def tampilDataMember(self):
        # ... (kode tampil data) ...
        baris = self.crud.dataMember()
        self.formMember.tabelMember.setRowCount(0)
        for r in baris:
            i = self.formMember.tabelMember.rowCount()
            self.formMember.tabelMember.insertRow(i)
            self.formMember.tabelMember.setItem(i,0,QTableWidgetItem(r["kd_member"]))
            self.formMember.tabelMember.setItem(i,1,QTableWidgetItem(r["nm_member"]))
            self.formMember.tabelMember.setItem(i,2,QTableWidgetItem(r["alamat_email"]))
            self.formMember.tabelMember.setItem(i,3,QTableWidgetItem(r["hp_telp"]))
            self.formMember.tabelMember.setItem(i,4,QTableWidgetItem(r["nama_kota"]))

    def doCariMember(self):
        # ... (kode cari) ...
        cari = self.formMember.editCari.text()
        baris = self.crud.CariMember(cari)
        self.formMember.tabelMember.setRowCount(0)
        for r in baris:
            i = self.formMember.tabelMember.rowCount()
            self.formMember.tabelMember.insertRow(i)
            self.formMember.tabelMember.setItem(i,0,QTableWidgetItem(r["kd_member"]))
            self.formMember.tabelMember.setItem(i,1,QTableWidgetItem(r["nm_member"]))
            self.formMember.tabelMember.setItem(i,2,QTableWidgetItem(r["alamat_email"]))
            self.formMember.tabelMember.setItem(i,3,QTableWidgetItem(r["hp_telp"]))
            self.formMember.tabelMember.setItem(i,4,QTableWidgetItem(r["nama_kota"]))
