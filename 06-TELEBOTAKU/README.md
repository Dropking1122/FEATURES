# 6️⃣ TELEBOTAKU — OpenWRT Telegram Bot

**🤖 Bot Telegram untuk Monitoring & Manajemen Router OpenWRT**

Bot Telegram modular berbasis Python untuk memonitor dan mengontrol router OpenWRT langsung dari Telegram — tanpa perlu akses SSH manual.

---

## 📋 Daftar File

- **[FEATURES.md](./FEATURES.md)** — Dokumentasi lengkap semua fitur & perintah bot
- **[images/](./images/)** — Screenshot dan aset visual
- **[docs/](./docs/)** — Dokumentasi teknis tambahan

---

## 🎯 Tentang Project

TELEBOTAKU adalah bot Telegram yang berjalan langsung di router OpenWRT. Cocok untuk admin jaringan atau pengguna rumahan yang ingin memantau dan mengelola router dari mana saja via Telegram — cukup kirim perintah, bot langsung merespons.

Bot ini cocok untuk:
- Admin jaringan RT/RW Net atau warnet
- Pengguna router OpenWRT di rumah / kantor
- Siapa saja yang ingin monitoring router dari HP

---

## ✨ Fitur Utama

- 📊 **Monitoring Sistem** — CPU, RAM, suhu, uptime real-time
- 🌐 **Statistik Jaringan** — vnStat, ping test, speed test, bandwidth monitor
- 📶 **Kontrol WiFi** — On/Off WiFi, ganti password langsung dari chat
- 🚫 **Block Device** — Blokir/unblokir perangkat berdasarkan MAC address
- 🔔 **Alert System** — Notifikasi otomatis saat ada device baru terhubung
- 💾 **Backup Config** — Backup konfigurasi router, kirim file ke Telegram
- 🔌 **Sistem Plugin** — Modular, mudah tambah/hapus fitur
- 🔄 **Auto Update** — Update bot langsung dari Telegram

---

## 🛠️ Teknologi

| Komponen | Detail |
|----------|--------|
| **Runtime** | Python 3 (OpenWRT) |
| **Library** | Telethon (Telegram MTProto) |
| **Platform** | OpenWRT / Router Linux |
| **Plugin** | Shell Script (.sh) |
| **Config** | config.ini |
| **Service** | /etc/init.d/revd (OpenWRT init) |

---

## 🚀 Instalasi Cepat

```bash
opkg update && (cd /tmp && curl -sLko revd_installer.sh \
  https://raw.githubusercontent.com/Dropking1122/telebotaku/main/revd_installer.sh \
  && chmod +x revd_installer.sh && sh revd_installer.sh)
```

Ikuti instruksi konfigurasi yang muncul (Bot Token, Admin ID, API ID & Hash).

---

## 📖 Baca Lengkapnya

👉 **[Lihat semua fitur detail → FEATURES.md](./FEATURES.md)**

---

## 🔗 Kontak

- **Telegram:** [@ValltzID](https://t.me/ValltzID)
- **Instagram:** [@revd.cloud](https://instagram.com/revd.cloud)
