# 🚀 Quick Start Guide

Panduan cepat untuk memulai dengan repositori FEATURES.

---

## 📖 Membaca Dokumentasi

### 1️⃣ Baca README.md Utama Dulu
```bash
# Di root folder /workspaces/FEATURES
cat README.md
```

Ini memberikan overview dari semua 4 project yang tersedia.

### 2️⃣ Pilih Project yang Ingin Dipelajari

Buka salah satu folder project:
- `01-POS-SUPPLIER-REVD/` — Sistem POS untuk Supplier
- `02-REVDWABOT/` — WhatsApp Bot Penjualan Otomatis
- `03-ABSENSIQR-REVD/` — Aplikasi Absensi QR Code
- `04-PROJECT-WEB-CLC/` — Website Project Management

### 3️⃣ Baca FEATURES.md untuk Detail Lengkap

Setiap folder memiliki `FEATURES.md` yang berisi penjelasan lengkap semua fitur.

```bash
# Contoh:
cat 01-POS-SUPPLIER-REVD/FEATURES.md
```

### 4️⃣ Lihat Gambar & Screenshot

Setiap project punya folder `images/` dengan screenshot aplikasi.

```bash
# Buka folder gambar
open 01-POS-SUPPLIER-REVD/images/
# atau
ls 02-REVDWABOT/images/
```

---

## 🖼️ Menampilkan Gambar di GitHub

Gambar-gambar akan otomatis ditampilkan ketika Anda:

1. **Buka FEATURES.md di GitHub**
   - URL akan seperti: `github.com/Dropking1122/FEATURES/blob/main/01-POS-SUPPLIER-REVD/FEATURES.md`
   - Gambar akan ter-render otomatis

2. **Klik link ke folder project**
   - Dari main README.md, klik link ke project
   - Gambar akan ditampilkan dengan markdown

3. **Format Markdown yang Digunakan**
   ```markdown
   ![Deskripsi](./images/nama-gambar.png)
   ```

---

## 📝 Menambah Dokumentasi Baru

### A. Update Fitur Existing

1. Edit file `FEATURES.md` di folder project
2. Tambah fitur baru atau update yang sudah ada
3. Jika ada gambar, simpan di folder `images/`
4. Commit & push

```bash
cd /workspaces/FEATURES
git add 01-POS-SUPPLIER-REVD/FEATURES.md
git commit -m "Update dokumentasi POS: tambah fitur baru"
git push
```

### B. Tambah Gambar ke Dokumentasi

1. **Siapkan file gambar** (PNG, JPG, maksimal 5MB)

2. **Copy ke folder images**
   ```bash
   cp screenshot.png /workspaces/FEATURES/01-POS-SUPPLIER-REVD/images/
   ```

3. **Tambahkan di FEATURES.md**
   ```markdown
   ![Deskripsi Gambar](./images/screenshot.png)
   ```

4. **Commit & push**
   ```bash
   cd /workspaces/FEATURES
   git add .
   git commit -m "Tambah screenshot dashboard POS"
   git push
   ```

### C. Tambah Dokumen Teknis

Gunakan folder `docs/` untuk dokumentasi tambahan:

```bash
# Contoh:
echo "# Panduan Instalasi..." > 01-POS-SUPPLIER-REVD/docs/INSTALLATION.md
```

---

## 🔧 Commit & Push ke GitHub

### Setup Awal (Jika belum):
```bash
cd /workspaces/FEATURES
git config user.name "Nama Anda"
git config user.email "email@example.com"
```

### Workflow Standar:
```bash
# 1. Lakukan perubahan (edit file, tambah gambar, dll)

# 2. Cek perubahan
git status

# 3. Add semua perubahan
git add .

# 4. Commit dengan pesan deskriptif
git commit -m "Deskripsi perubahan yang jelas"

# 5. Push ke GitHub
git push

# 6. Verifikasi di GitHub
# Buka: https://github.com/Dropking1122/FEATURES
```

---

## 📋 Struktur Folder Reference

```
/workspaces/FEATURES
├── README.md                    # Halaman utama (mulai dari sini!)
├── PANDUAN-DOKUMENTASI.md      # Panduan lengkap dokumentasi
├── SETUP-GUIDE.md              # File ini
│
├── 01-POS-SUPPLIER-REVD/       # Project 1
│   ├── README.md               # Ringkasan project
│   ├── FEATURES.md             # Fitur lengkap (dibaca setelah README)
│   ├── images/                 # Folder gambar/screenshot
│   │   ├── screenshot1.png
│   │   ├── screenshot2.png
│   │   └── ...
│   └── docs/                   # Dokumentasi teknis tambahan
│       └── INSTALLATION.md     (opsional)
│
├── 02-REVDWABOT/               # Project 2
│   ├── README.md
│   ├── FEATURES.md
│   ├── images/
│   └── docs/
│
├── 03-ABSENSIQR-REVD/          # Project 3
│   ├── README.md
│   ├── FEATURES.md
│   ├── images/
│   └── docs/
│
└── 04-PROJECT-WEB-CLC/         # Project 4
    ├── README.md
    ├── FEATURES.md
    ├── images/
    └── docs/
```

---

## ✅ Checklist Sebelum Push

Sebelum `git push`, pastikan:

- [ ] File markdown sudah diedit dengan benar
- [ ] Gambar sudah di-copy ke folder `images/`
- [ ] Markdown sudah di-update dengan link gambar
- [ ] Path gambar menggunakan relative path: `./images/nama.png`
- [ ] Tidak ada special character di nama file gambar
- [ ] Ukuran gambar tidak melebihi 5MB
- [ ] Semua perubahan sudah di-add: `git add .`
- [ ] Commit message jelas dan deskriptif

---

## 🌐 Preview di GitHub

Setelah push, dokumentasi akan terlihat di:

### Main README:
https://github.com/Dropking1122/FEATURES

### Project Spesifik:
- https://github.com/Dropking1122/FEATURES/tree/main/01-POS-SUPPLIER-REVD
- https://github.com/Dropking1122/FEATURES/tree/main/02-REVDWABOT
- Dst...

### FEATURES.md Spesifik:
- https://github.com/Dropking1122/FEATURES/blob/main/01-POS-SUPPLIER-REVD/FEATURES.md
- https://github.com/Dropking1122/FEATURES/blob/main/02-REVDWABOT/FEATURES.md
- Dst...

---

## 💡 Tips Penting

### 📸 Untuk Gambar Terlihat Bagus:
- ✅ Gunakan format PNG untuk screenshot UI
- ✅ Gunakan format JPG untuk foto
- ✅ Compress gambar sebelum upload (gunakan tools online)
- ✅ Ukuran ideal: 800x600 atau 1024x768 pixel
- ✅ Buat alt text yang deskriptif

### 📝 Untuk Markdown Terlihat Bagus:
- ✅ Gunakan heading hierarchy yang benar (#, ##, ###)
- ✅ Gunakan emoji untuk visual yang menarik
- ✅ Gunakan list/table untuk organize informasi
- ✅ Jangan terlalu banyak paragraph panjang
- ✅ Gunakan code block untuk contoh kode

### 🔗 Link yang Tepat:
- ✅ Gunakan relative path untuk file lokal: `./FEATURES.md`
- ✅ Gunakan relative path untuk gambar: `./images/name.png`
- ✅ Gunakan absolute URL untuk link eksternal: `https://github.com/...`

---

## 🆘 Troubleshooting

### Q: Gambar tidak muncul di GitHub?
**A:** 
- Pastikan path benar: `./images/nama.png` (bukan absolut)
- Pastikan file gambar sudah di-commit & push
- Coba hard refresh browser (Ctrl+F5)

### Q: Gimana commit perubahan gambar + markdown?
**A:**
```bash
git add .                                    # Add semua perubahan
git commit -m "Update: tambah screenshot"
git push
```

### Q: Bisa undo commit yang sudah push?
**A:**
```bash
git revert HEAD                  # Undo last commit
git push                         # Push undo
# atau
git reset --soft HEAD~1         # Undo last commit (keep changes)
```

---

## 📞 Bantuan Lebih Lanjut

- 📖 Baca **[PANDUAN-DOKUMENTASI.md](./PANDUAN-DOKUMENTASI.md)** untuk guide lengkap
- 📦 Cek **[README.md](./README.md)** untuk overview project
- 🔗 Kunjungi GitHub: https://github.com/Dropking1122/FEATURES

---

**Happy Documenting! 🚀**

Last Updated: May 2026

