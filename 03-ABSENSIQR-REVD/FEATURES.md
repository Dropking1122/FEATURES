# Catatan Lengkap Fitur — AbsensiQR REVD

> Aplikasi absensi berbasis QR Code untuk pencatatan kehadiran **siswa sekolah** secara real-time dan akurat.

---

## 1. Autentikasi & Manajemen Akun

- **Login** dengan username/email dan password
- **Dua level akses:**
  - **Admin** — akses penuh ke semua fitur, manajemen siswa dan guru
  - **Guru** — scan absensi, lihat laporan kelas yang diampu
- **Logout** dengan invalidasi sesi
- **Reset password** via email

---

## 2. Manajemen Data Siswa

### Data Siswa
| Field | Keterangan |
|-------|------------|
| NIS (Nomor Induk Siswa) | Kode unik setiap siswa |
| Nama Lengkap | Nama siswa |
| Kelas | Kelas yang diikuti (X, XI, XII, dll) |
| Jurusan | Jurusan / program studi |
| Angkatan | Tahun masuk |
| Nomor HP | Kontak siswa/orang tua |
| Foto | Foto profil siswa |

### Operasi
- **Tambah siswa** baru dengan form lengkap
- **Edit data siswa** — semua field bisa diubah
- **Hapus siswa** dengan konfirmasi
- **Import massal** dari file Excel (.xlsx / .csv)
- **Export** data siswa ke Excel
- **Pencarian real-time** berdasarkan nama atau NIS
- **Filter berdasarkan kelas** dan angkatan

---

## 3. QR Code Siswa

- Setiap siswa otomatis mendapat **QR Code unik** saat terdaftar
- QR Code berisi identitas siswa (NIS + hash unik)
- **Cetak QR Code** individual atau massal (PDF)
- QR Code bisa ditampilkan di layar HP / kartu pelajar
- QR Code tidak bisa dipalsukan (menggunakan enkripsi)

---

## 4. Proses Absensi (Scan QR)

### Cara Kerja
1. Guru / petugas buka halaman scan absensi
2. Kamera perangkat aktif otomatis
3. Arahkan kamera ke QR Code siswa
4. Sistem langsung mengenali siswa dan mencatat kehadiran
5. Muncul konfirmasi: nama siswa + waktu scan + status

### Status Kehadiran
| Status | Keterangan |
|--------|------------|
| **Hadir** | Scan tepat waktu |
| **Terlambat** | Scan lewat batas waktu masuk |
| **Izin** | Diinput manual oleh guru/admin |
| **Sakit** | Diinput manual dengan keterangan |
| **Alpha** | Tidak hadir tanpa keterangan |

### Fitur Scan
- Scan menggunakan **kamera HP/tablet/laptop** (browser)
- Scan bisa dilakukan untuk satu kelas sekaligus
- Siswa yang sudah scan tidak bisa scan ulang di hari yang sama
- Notifikasi bunyi saat scan berhasil / gagal

---

## 5. Dashboard

- **Total siswa hadir hari ini** — angka kehadiran keseluruhan
- **Persentase kehadiran** — grafik donut per kelas
- **Siswa belum absen** — daftar siswa yang belum scan hari ini
- **Grafik kehadiran mingguan** — bar chart 7 hari terakhir
- **Statistik per kelas** — tabel ringkasan per kelas
- **Riwayat scan terbaru** — 10 absensi terakhir real-time

---

## 6. Manajemen Kelas

- **Tambah / edit / hapus** data kelas
- **Assign guru wali kelas** per kelas
- **Lihat daftar siswa** per kelas
- Kelas bisa berupa: kelas reguler, ekstrakurikuler, atau mata pelajaran tertentu

---

## 7. Absensi per Mata Pelajaran

- Guru bisa buka sesi absensi untuk **mata pelajaran tertentu**
- Siswa scan QR untuk tiap mata pelajaran
- Laporan kehadiran bisa difilter per mata pelajaran
- Cocok untuk sekolah yang kehadiran dihitung per jam pelajaran

---

## 8. Input Manual Kehadiran

- Admin / guru bisa input status kehadiran manual
- Input massal untuk seluruh kelas (misal: hari libur / acara sekolah)
- Ubah status absensi yang sudah tersimpan
- Tambah keterangan / catatan untuk setiap absensi

---

## 9. Laporan Kehadiran

### Filter Laporan
- Per **tanggal** (harian)
- Per **minggu** (mingguan)
- Per **bulan** (bulanan)
- Per **kelas** dan per **siswa**
- Per **mata pelajaran**

### Isi Laporan
- Daftar absensi lengkap dengan status per siswa
- Rekap: total hadir, terlambat, izin, sakit, alpha
- Persentase kehadiran tiap siswa
- Siswa dengan kehadiran di bawah batas minimum (alert)

### Export Laporan
- Export ke **Excel (.xlsx)** — format siap cetak
- Export ke **PDF** — layout rapih untuk dokumen sekolah
- Laporan rekap per kelas untuk wali kelas
- Laporan rekap per siswa untuk orang tua

---

## 10. Notifikasi & Alert

- **Alert siswa dengan kehadiran rendah** — notifikasi ke guru/admin
- **Notifikasi real-time** saat ada siswa terlambat
- Batas minimum kehadiran bisa dikonfigurasi (misal: minimal 75%)
- Kirim notifikasi ke nomor HP orang tua (WhatsApp) jika dikonfigurasi

---

## 11. Pengaturan Sistem

- **Nama sekolah** dan informasi header
- **Jam masuk** sekolah (batas "tepat waktu" vs "terlambat")
- **Jam pulang** (untuk absensi keluar)
- **Hari aktif sekolah** (Senin-Jumat / Senin-Sabtu)
- **Logo sekolah** untuk header laporan
- **Batas minimum kehadiran** (dalam persen)

---

## 12. UI/UX

- **Bahasa Indonesia** di seluruh antarmuka
- **Responsive / Mobile-friendly** — optimal di HP, tablet, dan desktop
- **Real-time update** tanpa reload halaman
- **Dark / Light mode** (opsional)
- **Loading indicator** saat proses scan
- **Notifikasi berhasil/gagal** yang jelas saat scan QR

---

## Ringkasan Fitur per Role

| Fitur | Guru | Admin |
|-------|:----:|:-----:|
| Scan QR absensi siswa | ✅ | ✅ |
| Input manual kehadiran | ✅ | ✅ |
| Lihat laporan kelas diampu | ✅ | ✅ |
| Lihat semua laporan | ❌ | ✅ |
| Manajemen data siswa | ❌ | ✅ |
| Manajemen kelas | ❌ | ✅ |
| Pengaturan sistem | ❌ | ✅ |
| Export laporan semua kelas | ❌ | ✅ |
| Manajemen akun guru | ❌ | ✅ |
| Generate / cetak QR Code | ❌ | ✅ |

---

**Last Updated:** May 2026
