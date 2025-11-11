import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class kota(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        ui_file_name = "kota.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Tidak bisa membuka {ui_file_name}")
            sys.exit(-1)

        loader = QUiLoader()
        self.formKota = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.formKota.btnSimpan.clicked.connect(self.doSimpanKota)
        self.formKota.btnUbah.clicked.connect(self.doUbahKota)
        self.formKota.btnHapus.clicked.connect(self.doHapusKota)
        self.formKota.editCari.textChanged.connect(self.doCariKota)
        self.formKota.btnBersih.clicked.connect(self.doBersih)

        self.tampilDataKota()
        self.setWindowTitle("Data Kota")

    def doSimpanKota(self):
        if not self.formKota.editKdKota.text().strip():
            QMessageBox.information(None,"Informasi","Kode Kota belum di isi")
            self.formKota.editKdKota.setFocus()
        elif not self.formKota.editNamaKota.text().strip():
            QMessageBox.information(None,"Informasi","Nama Kota belum di isi")
            self.formKota.editNamaKota.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formKota.editKdKota.text()
                tempNama = self.formKota.editNamaKota.text()
                self.crud.simpanKota(tempID, tempNama)
                self.tampilDataKota()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")

    def doUbahKota(self):
        tempID = self.formKota.editKdKota.text()
        tempNama = self.formKota.editNamaKota.text()
        self.crud.ubahKota(tempID, tempNama)
        self.tampilDataKota()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusKota(self):
        tempID = self.formKota.editKdKota.text()
        self.crud.hapusKota(tempID)
        self.tampilDataKota()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    def doBersih(self):
        self.formKota.editKdKota.clear()
        self.formKota.editNamaKota.clear()
        self.formKota.editKdKota.setFocus()

    def tampilDataKota(self):
        baris = self.crud.dataKota()
        self.formKota.tabelKota.setRowCount(0)
        for r in baris:
            i = self.formKota.tabelKota.rowCount()
            self.formKota.tabelKota.insertRow(i)
            self.formKota.tabelKota.setItem(i,0,QTableWidgetItem(r["kd_kota"]))
            self.formKota.tabelKota.setItem(i,1,QTableWidgetItem(r["nama_kota"]))

    def doCariKota(self):
        cari = self.formKota.editCari.text()
        baris = self.crud.CariKota(cari)
        self.formKota.tabelKota.setRowCount(0)
        for r in baris:
            i = self.formKota.tabelKota.rowCount()
            self.formKota.tabelKota.insertRow(i)
            self.formKota.tabelKota.setItem(i,0,QTableWidgetItem(r["kd_kota"]))
            self.formKota.tabelKota.setItem(i,1,QTableWidgetItem(r["nama_kota"]))
