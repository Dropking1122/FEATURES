# 📚 Panduan Dokumentasi REVD Projects

Panduan lengkap untuk menambah dan mengelola dokumentasi project di repositori FEATURES.

---

## 📁 Struktur Folder

```
/workspaces/FEATURES
├── 01-POS-SUPPLIER-REVD/
│   ├── README.md           # Ringkasan project
│   ├── FEATURES.md         # Fitur lengkap (dibuka pertama kali)
│   ├── images/             # Tempat semua gambar, screenshot
│   └── docs/               # Dokumen teknis, panduan, dll
├── 02-REVDWABOT/
│   ├── README.md           
│   ├── FEATURES.md         
│   ├── images/             
│   └── docs/               
├── 03-ABSENSIQR-REVD/
│   ├── README.md           
│   ├── FEATURES.md         
│   ├── images/             
│   └── docs/               
└── 04-PROJECT-WEB-CLC/
    ├── README.md           
    ├── FEATURES.md         
    ├── images/             
    └── docs/
```

---

## 🖼️ Cara Menambahkan Gambar

### 1. Menyimpan File Gambar

Simpan semua gambar di folder `images/` masing-masing project:
- `/01-POS-SUPPLIER-REVD/images/dashboard.png`
- `/02-REVDWABOT/images/wabot-menu.png`
- Dst.

### 2. Menampilkan Gambar di Markdown

#### Format Dasar:
```markdown
![Nama Gambar](./images/nama-file.png)
```

#### Contoh Implementasi:
```markdown
## 📸 Dashboard

![Screenshot Dashboard POS](./images/dashboard.png)

Di sini Anda bisa lihat statistik penjualan harian, total profit, dan grafik penjualan bulanan.
```

#### Gambar dengan Ukuran:
```markdown
<img src="./images/screenshot.png" width="600" alt="Deskripsi Gambar" />
```

#### Gambar dengan Link (Klik untuk Buka Besar):
```markdown
[![Dashboard POS](./images/dashboard-thumb.png)](./images/dashboard.png)
```

---

## 📝 Template FEATURES.md

Gunakan struktur ini saat membuat/update FEATURES.md:

```markdown
# 📋 [Nama Project] - Dokumentasi Fitur

> [Deskripsi singkat project]

---

## ✅ Fitur Unggulan

### 🎯 Kategori Fitur 1
- Fitur detail 1
- Fitur detail 2

### 🎯 Kategori Fitur 2
- Fitur detail 1
- Fitur detail 2

---

## 📸 Screenshot

![Deskripsi Screenshot](./images/screenshot.png)

---

## 🛠️ Teknologi

- **Backend:** [Teknologi]
- **Frontend:** [Teknologi]
- **Database:** [Teknologi]

---

## 📞 Kontak

- Repository: [Link GitHub]
- Developer: [Name]
```

---

## 🖼️ Format Nama File Gambar

Gunakan penamaan yang konsisten dan deskriptif:

```
dashboard.png              # Dashboard utama
login-screen.png          # Layar login
feature-1-demo.png        # Demo fitur tertentu
user-management.png       # Manajemen pengguna
settings-panel.png        # Panel pengaturan
report-example.png        # Contoh laporan
```

**Hindari:**
- ❌ `Screenshot_001.png`
- ❌ `IMG_20250519.jpg`
- ❌ `temp-file-2.png`

**Lebih baik:**
- ✅ `pos-dashboard.png`
- ✅ `inventory-management.png`
- ✅ `sales-report.png`

---

## 📄 Jenis-Jenis Dokumen

### README.md
- **Tujuan:** Ringkasan project & entry point
- **Isi:** Fitur utama, teknologi, link ke FEATURES.md
- **Tidak perlu:** Detail teknis panjang

### FEATURES.md
- **Tujuan:** Dokumentasi fitur lengkap (yang akan dibaca first)
- **Isi:** Semua fitur dengan penjelasan detail
- **Boleh:** Gambar, tabel, list panjang

### docs/ folder
Gunakan untuk dokumen tambahan:
- `INSTALLATION.md` - Cara install & setup
- `CONFIGURATION.md` - Panduan konfigurasi
- `API-DOCUMENTATION.md` - Dokumentasi API
- `TROUBLESHOOTING.md` - FAQ & masalah umum
- `DATABASE-SCHEMA.md` - Schema database
- `DEPLOYMENT.md` - Cara deploy
- Dll

---

## 🔄 Workflow Menambah Dokumentasi

### 1. Update FEATURES.md
```bash
# Edit file FEATURES.md untuk project tertentu
# Tambahkan fitur baru atau update yang sudah ada
```

### 2. Tambahkan Gambar (Opsional)
```bash
# Copy gambar ke folder images/
cp screenshot.png /workspaces/FEATURES/01-POS-SUPPLIER-REVD/images/
```

### 3. Embed Gambar di Markdown
```markdown
![Deskripsi Screenshot](./images/screenshot.png)
```

### 4. Commit & Push
```bash
cd /workspaces/FEATURES
git add .
git commit -m "Update dokumentasi [Project Name]: tambah fitur X"
git push
```

---

## 💡 Tips & Best Practices

### ✅ DO:
- ✅ Gunakan folder `images/` untuk semua gambar
- ✅ Beri nama file gambar yang deskriptif
- ✅ Tambahkan alt text (`![alt text]`) di semua gambar
- ✅ Update README.md saat ada project baru
- ✅ Gunakan emoji untuk visual yang menarik
- ✅ Organize dokumen dengan heading yang jelas

### ❌ DON'T:
- ❌ Jangan simpan gambar di root folder
- ❌ Jangan gunakan path absolut (gunakan relative path)
- ❌ Jangan upload file besar (> 5MB)
- ❌ Jangan hapus folder `images/` atau `docs/`
- ❌ Jangan gunakan special character di nama file

---

## 🎨 Emoji yang Sering Digunakan

```
🎯 Target / Goal
✅ Fitur / Selesai
❌ Tidak / Error
📸 Screenshot / Gambar
📋 Dokumentasi / List
🛠️ Teknologi / Tools
🔧 Konfigurasi
📊 Dashboard / Analytics
💼 Business / Professional
🤖 Bot / Automation
💳 Payment / Transaksi
👥 User / Team
🌐 Web / Internet
📱 Mobile / App
⏱️ Time / Schedule
📈 Growth / Chart
🔐 Security / Auth
📞 Contact / Support
🌟 Best / Premium
🔄 Process / Flow
📦 Package / Delivery
🎓 Learning / Tutorial
```

---

## 📞 Pertanyaan yang Sering Diajukan

### Q: Bagaimana cara upload gambar yang sudah ada?
**A:** 
1. Simpan file gambar ke folder `images/` masing-masing project
2. Gunakan syntax markdown: `![Deskripsi](./images/nama-file.png)`
3. Commit & push ke repository

### Q: Berapa ukuran maksimal gambar?
**A:** Sebaiknya jangan lebih dari 5MB per file. Gunakan format PNG/JPG yang sudah di-compress.

### Q: Bisa pakai gambar eksternal (URL)?
**A:** Bisa, tapi **tidak recommended** karena:
- ❌ Gambar hilang jika URL berubah
- ❌ Loading lebih lambat
- ✅ Lebih baik simpan lokal di folder `images/`

### Q: Gimana kalau ingin nambah project baru?
**A:**
1. Buat folder `05-PROJECT-NAME` di `/workspaces/FEATURES`
2. Buat subfolder `images/` dan `docs/`
3. Buat file `README.md` dan `FEATURES.md`
4. Update main `README.md` dengan link ke project baru

---

## 🚀 Contoh Penambahan Gambar

### Sebelum:
```markdown
## 📸 Dashboard

Dashboard menampilkan ringkasan penjualan hari ini, total profit, dan grafik penjualan bulanan.
```

### Sesudah:
```markdown
## 📸 Dashboard

![Dashboard POS Supplier](./images/dashboard.png)

Dashboard menampilkan:
- Total penjualan hari ini dengan jumlah uang masuk
- Total profit hari ini (pendapatan - modal)
- Grafik penjualan bulanan untuk tracking trend

Anda dapat melihat semua informasi penting dalam satu layar tanpa perlu scroll jauh.
```

---

## 🔗 Template Link antar File

```markdown
# Link ke file di project yang sama
[Lihat FEATURES.md](./FEATURES.md)
[Lihat dokumentasi instalasi](./docs/INSTALLATION.md)
[Lihat gambar dashboard](./images/dashboard.png)

# Link ke file di project lain
[Lihat POS-SUPPLIER-REVD](../01-POS-SUPPLIER-REVD/README.md)
[Lihat REVDWABOT](../02-REVDWABOT/FEATURES.md)

# Link ke file di root
[Kembali ke README utama](../README.md)
```

---

**Last Updated:** May 2026  
**Maintained By:** Dropking1122
