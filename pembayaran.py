import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class pembayaran(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        ui_file_name = "pembayaran.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Tidak bisa membuka {ui_file_name}")
            sys.exit(-1)

        loader = QUiLoader()
        self.formPembayaran = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.formPembayaran.btnSimpan.clicked.connect(self.doSimpanPembayaran)
        self.formPembayaran.btnUbah.clicked.connect(self.doUbahPembayaran)
        self.formPembayaran.btnHapus.clicked.connect(self.doHapusPembayaran)
        self.formPembayaran.editCari.textChanged.connect(self.doCariPembayaran)
        self.formPembayaran.btnBersih.clicked.connect(self.doBersih)

        self.tampilDataPembayaran()
        self.setWindowTitle("Data Pembayaran")

    def doSimpanPembayaran(self):
        if not self.formPembayaran.editIdBayar.text().strip():
            QMessageBox.information(None,"Informasi","ID Bayar belum di isi")
            self.formPembayaran.editIdBayar.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                tempID = self.formPembayaran.editIdBayar.text()
                tempBiaya = self.formPembayaran.editBiaya.text()
                tempRek = self.formPembayaran.editRekTujuan.text()
                tempNamaRek = self.formPembayaran.editNamaRek.text()
                tempNominal = self.formPembayaran.editNominal.text()
                tempKdIklan = self.formPembayaran.editKdIklan.text()

                self.crud.simpanPembayaran(tempID, tempBiaya, tempRek, tempNamaRek, tempNominal, tempKdIklan)
                self.tampilDataPembayaran()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")

    def doUbahPembayaran(self):
        tempID = self.formPembayaran.editIdBayar.text()
        tempBiaya = self.formPembayaran.editBiaya.text()
        tempRek = self.formPembayaran.editRekTujuan.text()
        tempNamaRek = self.formPembayaran.editNamaRek.text()
        tempNominal = self.formPembayaran.editNominal.text()
        tempKdIklan = self.formPembayaran.editKdIklan.text()

        self.crud.ubahPembayaran(tempID, tempBiaya, tempRek, tempNamaRek, tempNominal, tempKdIklan)
        self.tampilDataPembayaran()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusPembayaran(self):
        tempID = self.formPembayaran.editIdBayar.text()
        self.crud.hapusPembayaran(tempID)
        self.tampilDataPembayaran()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    def doBersih(self):
        self.formPembayaran.editIdBayar.clear()
        self.formPembayaran.editBiaya.clear()
        self.formPembayaran.editRekTujuan.clear()
        self.formPembayaran.editNamaRek.clear()
        self.formPembayaran.editNominal.clear()
        self.formPembayaran.editKdIklan.clear()
        self.formPembayaran.editIdBayar.setFocus()

    def tampilDataPembayaran(self):
        baris = self.crud.dataPembayaran()
        self.formPembayaran.tabelPembayaran.setRowCount(0)
        for r in baris:
            i = self.formPembayaran.tabelPembayaran.rowCount()
            self.formPembayaran.tabelPembayaran.insertRow(i)
            self.formPembayaran.tabelPembayaran.setItem(i,0,QTableWidgetItem(r["ID_bayar"]))
            self.formPembayaran.tabelPembayaran.setItem(i,1,QTableWidgetItem(str(r["nominal"])))
            self.formPembayaran.tabelPembayaran.setItem(i,2,QTableWidgetItem(r["nama_rek"]))
            self.formPembayaran.tabelPembayaran.setItem(i,3,QTableWidgetItem(r["rek_tujuan"]))
            self.formPembayaran.tabelPembayaran.setItem(i,4,QTableWidgetItem(r["judul_iklan"]))

    def doCariPembayaran(self):
        cari = self.formPembayaran.editCari.text()
        baris = self.crud.CariPembayaran(cari)
        self.formPembayaran.tabelPembayaran.setRowCount(0)
        for r in baris:
            i = self.formPembayaran.tabelPembayaran.rowCount()
            self.formPembayaran.tabelPembayaran.insertRow(i)
            self.formPembayaran.tabelPembayaran.setItem(i,0,QTableWidgetItem(r["ID_bayar"]))
            self.formPembayaran.tabelPembayaran.setItem(i,1,QTableWidgetItem(str(r["nominal"])))
            self.formPembayaran.tabelPembayaran.setItem(i,2,QTableWidgetItem(r["nama_rek"]))
            self.formPembayaran.tabelPembayaran.setItem(i,3,QTableWidgetItem(r["rek_tujuan"]))
            self.formPembayaran.tabelPembayaran.setItem(i,4,QTableWidgetItem(r["judul_iklan"]))
