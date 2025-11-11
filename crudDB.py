import mysql.connector

class my_cruddb:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'tugasvisual3_2310010302'
        )

    def simpanKategori(self, kd, nama):
        alamat = self.conn.cursor()
        alamat.execute("insert into kategori (kd_kategori, nm_kategori) value(%s,%s)",(kd, nama))
        self.conn.commit()
        alamat.close()

    def ubahKategori(self, kd, nama):
        alamat = self.conn.cursor()
        alamat.execute("update kategori set nm_kategori=%s where kd_kategori=%s",(nama, kd))
        self.conn.commit()
        alamat.close()

    def hapusKategori(self, kd):
        alamat = self.conn.cursor()
        alamat.execute("delete from kategori where kd_kategori=%s", (kd,))
        self.conn.commit()
        alamat.close()

    def dataKategori(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("select * from kategori order by kd_kategori asc")
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariKategori(self, param):
        sql = "select * from kategori where kd_kategori like %s or nm_kategori like %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanKota(self, kd, nama):
        alamat = self.conn.cursor()
        alamat.execute("insert into kota (kd_kota, nama_kota) value(%s,%s)",(kd, nama))
        self.conn.commit()
        alamat.close()

    def ubahKota(self, kd, nama):
        alamat = self.conn.cursor()
        alamat.execute("update kota set nama_kota=%s where kd_kota=%s",(nama, kd))
        self.conn.commit()
        alamat.close()

    def hapusKota(self, kd):
        alamat = self.conn.cursor()
        alamat.execute("delete from kota where kd_kota=%s", (kd,))
        self.conn.commit()
        alamat.close()

    def dataKota(self):
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute("select * from kota order by kd_kota asc")
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariKota(self, param):
        sql = "select * from kota where kd_kota like %s or nama_kota like %s"
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql,[f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanMember(self, kd, nama, email, hp, kd_kota):
        alamat = self.conn.cursor()
        sql = "insert into member (kd_member, nm_member, alamat_email, hp_telp, kd_kota) value(%s,%s,%s,%s,%s)"
        alamat.execute(sql,(kd, nama, email, hp, kd_kota))
        self.conn.commit()
        alamat.close()

    def ubahMember(self, kd, nama, email, hp, kd_kota):
        alamat = self.conn.cursor()
        sql = "update member set nm_member=%s, alamat_email=%s, hp_telp=%s, kd_kota=%s where kd_member=%s"
        alamat.execute(sql,(nama, email, hp, kd_kota, kd))
        self.conn.commit()
        alamat.close()

    def hapusMember(self, kd):
        alamat = self.conn.cursor()
        alamat.execute("delete from member where kd_member=%s", (kd,))
        self.conn.commit()
        alamat.close()

    def dataMember(self):
        alamat = self.conn.cursor(dictionary = True)
        sql = """
            SELECT m.*, k.nama_kota
            FROM member m
            LEFT JOIN kota k ON m.kd_kota = k.kd_kota
            ORDER BY m.kd_member ASC
        """
        alamat.execute(sql)
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariMember(self, param):
        p = f"%{param}%"
        sql = """
            SELECT m.*, k.nama_kota
            FROM member m
            LEFT JOIN kota k ON m.kd_kota = k.kd_kota
            WHERE m.kd_member LIKE %s OR m.nm_member LIKE %s OR m.alamat_email LIKE %s OR m.hp_telp LIKE %s OR k.nama_kota LIKE %s
        """
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql, [p, p, p, p, p])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanIklan(self, kd, judul, harga, kd_kategori, kd_member):
        alamat = self.conn.cursor()
        sql = "insert into iklan (kd_iklan, judul_iklan, harga, kd_kategori, kd_member) value(%s,%s,%s,%s,%s)"
        alamat.execute(sql,(kd, judul, harga, kd_kategori, kd_member))
        self.conn.commit()
        alamat.close()

    def ubahIklan(self, kd, judul, harga, kd_kategori, kd_member):
        alamat = self.conn.cursor()
        sql = "update iklan set judul_iklan=%s, harga=%s, kd_kategori=%s, kd_member=%s where kd_iklan=%s"
        alamat.execute(sql,(judul, harga, kd_kategori, kd_member, kd))
        self.conn.commit()
        alamat.close()

    def hapusIklan(self, kd):
        alamat = self.conn.cursor()
        alamat.execute("delete from iklan where kd_iklan=%s", (kd,))
        self.conn.commit()
        alamat.close()

    def dataIklan(self):
        alamat = self.conn.cursor(dictionary = True)
        sql = """
            SELECT i.kd_iklan, i.judul_iklan, i.harga, k.nm_kategori, m.nm_member
            FROM iklan i
            LEFT JOIN kategori k ON i.kd_kategori = k.kd_kategori
            LEFT JOIN member m ON i.kd_member = m.kd_member
            ORDER BY i.kd_iklan ASC
        """
        alamat.execute(sql)
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariIklan(self, param):
        p = f"%{param}%"
        sql = """
            SELECT i.kd_iklan, i.judul_iklan, i.harga, k.nm_kategori, m.nm_member
            FROM iklan i
            LEFT JOIN kategori k ON i.kd_kategori = k.kd_kategori
            LEFT JOIN member m ON i.kd_member = m.kd_member
            WHERE i.kd_iklan LIKE %s OR i.judul_iklan LIKE %s OR k.nm_kategori LIKE %s OR m.nm_member LIKE %s
        """
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql, [p, p, p, p])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanPembayaran(self, id, biaya, rek, namarek, nominal, kd_iklan):
        alamat = self.conn.cursor()
        sql = "insert into pembayaran (ID_bayar, biaya_iklan, rek_tujuan, nama_rek, nominal, kd_iklan) value(%s,%s,%s,%s,%s,%s)"
        alamat.execute(sql,(id, biaya, rek, namarek, nominal, kd_iklan))
        self.conn.commit()
        alamat.close()

    def ubahPembayaran(self, id, biaya, rek, namarek, nominal, kd_iklan):
        alamat = self.conn.cursor()
        sql = "update pembayaran set biaya_iklan=%s, rek_tujuan=%s, nama_rek=%s, nominal=%s, kd_iklan=%s where ID_bayar=%s"
        alamat.execute(sql,(biaya, rek, namarek, nominal, kd_iklan, id))
        self.conn.commit()
        alamat.close()

    def hapusPembayaran(self, id):
        alamat = self.conn.cursor()
        alamat.execute("delete from pembayaran where ID_bayar=%s", (id,))
        self.conn.commit()
        alamat.close()

    def dataPembayaran(self):
        alamat = self.conn.cursor(dictionary = True)
        sql = """
            SELECT p.*, i.judul_iklan
            FROM pembayaran p
            LEFT JOIN iklan i ON p.kd_iklan = i.kd_iklan
            ORDER BY p.ID_bayar ASC
        """
        alamat.execute(sql)
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariPembayaran(self, param):
        p = f"%{param}%"
        sql = """
            SELECT p.*, i.judul_iklan
            FROM pembayaran p
            LEFT JOIN iklan i ON p.kd_iklan = i.kd_iklan
            WHERE p.ID_bayar LIKE %s OR p.nama_rek LIKE %s OR i.judul_iklan LIKE %s
        """
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql, [p, p, p])
        record = alamat.fetchall()
        alamat.close()
        return record

    def simpanPesan(self, kd, pengirim, email, isi, kd_member):
        alamat = self.conn.cursor()
        sql = "insert into pesan_inbox (kd_pesan_inb, nm_pengirim, email_pengirim, isi_pesan_inb, kd_member) value(%s,%s,%s,%s,%s)"
        alamat.execute(sql,(kd, pengirim, email, isi, kd_member))
        self.conn.commit()
        alamat.close()

    def ubahPesan(self, kd, pengirim, email, isi, kd_member):
        alamat = self.conn.cursor()
        sql = "update pesan_inbox set nm_pengirim=%s, email_pengirim=%s, isi_pesan_inb=%s, kd_member=%s where kd_pesan_inb=%s"
        alamat.execute(sql,(pengirim, email, isi, kd_member, kd))
        self.conn.commit()
        alamat.close()

    def hapusPesan(self, kd):
        alamat = self.conn.cursor()
        alamat.execute("delete from pesan_inbaox where kd_pesan_inb=%s", (kd,))
        self.conn.commit()
        alamat.close()

    def dataPesan(self):
        alamat = self.conn.cursor(dictionary = True)
        sql = """
            SELECT p.*, m.nm_member
            FROM pesan_inbox p
            LEFT JOIN member m ON p.kd_member = m.kd_member
            ORDER BY p.tgl_kirim DESC
        """
        alamat.execute(sql)
        record = alamat.fetchall()
        alamat.close()
        return record

    def CariPesan(self, param):
        p = f"%{param}%"
        sql = """
            SELECT p.*, m.nm_member
            FROM pesan_inbox p
            LEFT JOIN member m ON p.kd_member = m.kd_member
            WHERE p.nm_pengirim LIKE %s OR p.email_pengirim LIKE %s OR p.isi_pesan_inb LIKE %s OR m.nm_member LIKE %s
        """
        alamat = self.conn.cursor(dictionary = True)
        alamat.execute(sql, [p, p, p, p])
        record = alamat.fetchall()
        alamat.close()
        return record
