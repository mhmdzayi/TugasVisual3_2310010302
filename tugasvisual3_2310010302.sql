-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 11, 2025 at 07:48 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugasvisual3_2310010302`
--

-- --------------------------------------------------------

--
-- Table structure for table `iklan`
--

CREATE TABLE `iklan` (
  `kd_iklan` varchar(10) NOT NULL,
  `judul_iklan` varchar(255) NOT NULL,
  `harga` int(11) DEFAULT 0,
  `deskripsi` text DEFAULT NULL,
  `tgl_pasang` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `kd_kategori` varchar(10) DEFAULT NULL,
  `kd_kota` varchar(10) DEFAULT NULL,
  `kd_member` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kategori`
--

CREATE TABLE `kategori` (
  `kd_kategori` varchar(10) NOT NULL,
  `nm_kategori` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kategori`
--

INSERT INTO `kategori` (`kd_kategori`, `nm_kategori`) VALUES
('112', 'Motor'),
('122', 'Mobil'),
('123', 'Handphone');

-- --------------------------------------------------------

--
-- Table structure for table `kota`
--

CREATE TABLE `kota` (
  `kd_kota` varchar(10) NOT NULL,
  `nama_kota` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kota`
--

INSERT INTO `kota` (`kd_kota`, `nama_kota`) VALUES
('B', 'Jakarta'),
('DA', 'Banjarmasin');

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `kd_member` varchar(10) NOT NULL,
  `nm_member` varchar(150) NOT NULL,
  `alamat_email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `hp_telp` varchar(20) DEFAULT NULL,
  `tgl_daftar` date DEFAULT NULL,
  `kd_kota` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`kd_member`, `nm_member`, `alamat_email`, `password`, `hp_telp`, `tgl_daftar`, `kd_kota`) VALUES
('465', 'Zaini', 'zzz4in1@gmail.com', '', '081521794673', NULL, 'DA'),
('947', 'Lukman', 'lkkman@gmail.com', '', '081525639901', NULL, 'B');

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran`
--

CREATE TABLE `pembayaran` (
  `ID_bayar` varchar(10) NOT NULL,
  `biaya_iklan` int(11) DEFAULT NULL,
  `rek_tujuan` varchar(50) DEFAULT NULL,
  `nama_rek` varchar(100) DEFAULT NULL,
  `nominal` int(11) DEFAULT NULL,
  `kd_iklan` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pesan_inbox`
--

CREATE TABLE `pesan_inbox` (
  `kd_pesan_inb` varchar(10) NOT NULL,
  `tgl_kirim` datetime DEFAULT current_timestamp(),
  `nm_pengirim` varchar(150) DEFAULT NULL,
  `email_pengirim` varchar(100) DEFAULT NULL,
  `isi_pesan_inb` text DEFAULT NULL,
  `kd_member` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `iklan`
--
ALTER TABLE `iklan`
  ADD PRIMARY KEY (`kd_iklan`),
  ADD KEY `kd_kategori` (`kd_kategori`),
  ADD KEY `kd_kota` (`kd_kota`),
  ADD KEY `kd_member` (`kd_member`);

--
-- Indexes for table `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`kd_kategori`);

--
-- Indexes for table `kota`
--
ALTER TABLE `kota`
  ADD PRIMARY KEY (`kd_kota`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`kd_member`),
  ADD UNIQUE KEY `alamat_email` (`alamat_email`),
  ADD KEY `kd_kota` (`kd_kota`);

--
-- Indexes for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD PRIMARY KEY (`ID_bayar`),
  ADD KEY `kd_iklan` (`kd_iklan`);

--
-- Indexes for table `pesan_inbox`
--
ALTER TABLE `pesan_inbox`
  ADD PRIMARY KEY (`kd_pesan_inb`),
  ADD KEY `kd_member` (`kd_member`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `iklan`
--
ALTER TABLE `iklan`
  ADD CONSTRAINT `iklan_ibfk_1` FOREIGN KEY (`kd_kategori`) REFERENCES `kategori` (`kd_kategori`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `iklan_ibfk_2` FOREIGN KEY (`kd_kota`) REFERENCES `kota` (`kd_kota`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `iklan_ibfk_3` FOREIGN KEY (`kd_member`) REFERENCES `member` (`kd_member`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `member`
--
ALTER TABLE `member`
  ADD CONSTRAINT `member_ibfk_1` FOREIGN KEY (`kd_kota`) REFERENCES `kota` (`kd_kota`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD CONSTRAINT `pembayaran_ibfk_1` FOREIGN KEY (`kd_iklan`) REFERENCES `iklan` (`kd_iklan`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `pesan_inbox`
--
ALTER TABLE `pesan_inbox`
  ADD CONSTRAINT `pesan_inbox_ibfk_1` FOREIGN KEY (`kd_member`) REFERENCES `member` (`kd_member`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
