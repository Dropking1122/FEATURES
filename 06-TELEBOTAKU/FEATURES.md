# Dokumentasi Lengkap Fitur — TELEBOTAKU (OpenWRT Telegram Bot)

> Bot Telegram modular berbasis Python untuk monitoring dan manajemen router OpenWRT secara remote via Telegram.

---

## 1. Gambaran Umum

TELEBOTAKU berjalan langsung di router OpenWRT sebagai service background. Setiap fitur diimplementasi sebagai plugin shell script yang terpisah — mudah ditambah, diubah, atau dihapus tanpa mengubah kode utama.

**Stack Teknologi:**
- **Python 3** + **Telethon** (Telegram MTProto API)
- **Shell Script** untuk setiap plugin fitur
- **config.ini** untuk konfigurasi
- **OpenWRT init.d** untuk service management

---

## 2. Sistem Plugin

Bot menggunakan arsitektur plugin modular. Semua plugin tersimpan di `/root/REVDBOT/plugins/`:

| Plugin | File | Deskripsi |
|--------|------|-----------|
| System Monitor | `system.sh` | Info sistem real-time (CPU, RAM, suhu, uptime) |
| Memory Cleaner | `clear_ram.sh` | Bersihkan cache RAM |
| Network Stats | `vnstat.sh` | Statistik penggunaan jaringan |
| Speed Test | `speedtest.sh` | Test kecepatan internet |
| Ping Test | `ping.sh` | Test konektivitas ke target |
| WiFi Control | `wifi_control.sh` | On/Off WiFi, ganti password |
| Bandwidth Monitor | `bandwidth.sh` | Monitor bandwidth realtime |
| Block MAC | `block_mac.sh` | Blokir/unblokir perangkat via MAC address |
| Alert Monitor | `alert_monitor.sh` | Deteksi dan notifikasi device baru |
| Backup Config | `backup_config.sh` | Backup konfigurasi sistem ke Telegram |
| User List | `userlist.sh` | Daftar perangkat yang terhubung |
| Firewall Status | `firewall.sh` | Status firewall & aturan aktif |
| System Reboot | `reboot.sh` | Restart router |
| Bot Update | `update.sh` | Update bot dari GitHub |
| Bot Uninstall | `uninstall.sh` | Hapus bot dari sistem |

### Menambah Plugin Baru
1. Buat script baru di `/root/REVDBOT/plugins/`
2. Beri permission: `chmod +x nama_plugin.sh`
3. Tambahkan handler di `bot_openwrt.py` jika perlu

---

## 3. Daftar Perintah Lengkap

| Perintah | Fungsi | Akses |
|----------|--------|-------|
| `/start` | Mulai bot, tampilkan menu utama | Semua |
| `/help` | Tampilkan bantuan | Semua |
| `/system` | Info sistem lengkap | Semua |
| `/clearram` | Bersihkan cache RAM | Semua |
| `/network` | Statistik jaringan (vnStat) | Semua |
| `/speedtest` | Test kecepatan internet | Semua |
| `/ping [target]` | Ping ke target tertentu | Semua |
| `/bandwidth` | Monitor bandwidth realtime | Semua |
| `/userlist` | Daftar perangkat terhubung | Semua |
| `/wifi` | Status WiFi saat ini | Semua |
| `/wifi on` | Nyalakan WiFi | Admin |
| `/wifi off` | Matikan WiFi | Admin |
| `/wifi pass <password>` | Ganti password WiFi | Admin |
| `/block <MAC>` | Blokir perangkat via MAC | Admin |
| `/unblock <MAC>` | Unblokir perangkat | Admin |
| `/blocklist` | Daftar perangkat yang diblokir | Semua |
| `/alert` | Menu Alert System | Semua |
| `/backup` | Backup konfigurasi sistem | Admin |
| `/reboot` | Restart router | Admin |
| `/update` | Update bot dari GitHub | Admin |
| `/uninstall` | Hapus bot dari sistem | Admin |

---

## 4. Interface Menu Bot

### Menu Utama (Inline Keyboard)
```
╔══════════════════════════════════════════╗
║  📊 System Info    │  🔄 Reboot          ║
║  🧹 Clear RAM      │  🌐 Network Stats   ║
║  🚀 Speed Test     │  📡 Ping Test       ║
║  📶 WiFi Control   │  📊 Bandwidth       ║
║  🚫 Block Device   │  👥 User List       ║
║  💾 Backup Config  │  🔔 Alert System    ║
║  ⬆️ Update Bot     │  🗑️ Uninstall Bot  ║
╚══════════════════════════════════════════╝
```

### Contoh Output System Monitor
```
╔══════════════════════════════════════════╗
║         📊 SYSTEM MONITOR               ║
╠══════════════════════════════════════════╣
║  📡 Device: OpenWRT | REVD.CLOUD        ║
║  🔧 Model: Amlogic HG680P (S905X)       ║
║  ⏱️  Uptime: 2d 14:32:10               ║
║  🌡️  Temp: 52.3°C                      ║
║  📊 CPU: 12%                            ║
║  🧠 Memory: 128.5 MB / 512 MB           ║
╠══════════════════════════════════════════╣
║             REVD.CLOUD                  ║
╚══════════════════════════════════════════╝
```

---

## 5. Monitoring Sistem

### Yang Dipantau Real-time
- **CPU Usage** — persentase penggunaan processor
- **RAM Usage** — terpakai vs total memory
- **Suhu** — temperatur chip router (°C)
- **Uptime** — sudah berapa lama router menyala
- **Model Perangkat** — nama dan chipset router

### Clear RAM
Membersihkan cache Linux yang menumpuk:
```bash
/clearram   # via Telegram
```
Output: laporan berapa MB RAM berhasil dibebaskan.

---

## 6. Monitoring Jaringan

### Network Stats (vnStat)
Statistik penggunaan bandwidth harian/bulanan:
- Total data masuk (RX) dan keluar (TX)
- Grafik penggunaan per hari
- Rata-rata penggunaan

### Speed Test
Test kecepatan koneksi internet langsung dari router:
- Download speed (Mbps)
- Upload speed (Mbps)
- Ping/latency (ms)
- Server test yang digunakan

### Ping Test
```bash
/ping 8.8.8.8       # Ping ke Google DNS
/ping google.com    # Ping ke domain
```

### Bandwidth Monitor
Monitor penggunaan bandwidth secara realtime per interface.

---

## 7. Kontrol WiFi

Kendalikan WiFi router langsung dari Telegram:

```bash
/wifi              # Lihat status WiFi saat ini
/wifi on           # Nyalakan semua WiFi
/wifi off          # Matikan semua WiFi
/wifi pass RevdStore123   # Ganti password WiFi
```

**Catatan:** Perintah `on`, `off`, dan `pass` hanya untuk Admin.

---

## 8. Block Device (MAC Filtering)

Blokir perangkat yang tidak diinginkan terhubung ke jaringan:

```bash
/block AA:BB:CC:DD:EE:FF     # Blokir MAC address
/unblock AA:BB:CC:DD:EE:FF   # Unblokir MAC address
/blocklist                    # Lihat semua yang diblokir
```

Pemblokiran menggunakan iptables firewall — langsung aktif tanpa restart router.

---

## 9. Alert System — Deteksi Device Baru

Bot otomatis mengirim notifikasi saat ada perangkat baru yang terhubung ke jaringan:

- 🔍 **Cek Device Baru** — Periksa device yang baru connect sejak terakhir dicek
- 📋 **Riwayat Alert** — History semua device yang pernah connect
- 🔄 **Reset Known Devices** — Reset daftar device yang sudah dikenal
- 🗑️ **Hapus Riwayat** — Bersihkan log alert

---

## 10. Backup Konfigurasi

Backup seluruh konfigurasi router dan kirim file backup langsung ke chat Telegram:

```bash
/backup    # Buat backup & kirim ke Telegram (Admin only)
```

File backup dikirim dalam format `.tar.gz` berisi konfigurasi sistem OpenWRT.

---

## 11. Manajemen Service Bot

Kelola bot sebagai service OpenWRT:

```bash
/etc/init.d/revd start     # Jalankan bot
/etc/init.d/revd stop      # Hentikan bot
/etc/init.d/revd restart   # Restart bot
/etc/init.d/revd status    # Cek status
/etc/init.d/revd enable    # Aktifkan auto-start saat boot
/etc/init.d/revd disable   # Nonaktifkan auto-start
```

---

## 12. Update & Uninstall

### Update Bot
```bash
# Via Telegram:
/update

# Via SSH:
sh /root/REVDBOT/plugins/update.sh
```
Bot mengunduh versi terbaru dari GitHub dan restart otomatis.

### Uninstall Bot
```bash
# Via Telegram (direkomendasikan):
/uninstall
# Pilih: Keep config / Delete all / Cancel

# One-liner via SSH:
cd /tmp && curl -sLko uninstall.sh \
  https://raw.githubusercontent.com/Dropking1122/telebotaku/main/uninstall.sh \
  && chmod +x uninstall.sh && sh uninstall.sh
```

---

## 13. Struktur Direktori di Router

```
/root/REVDBOT/
├── bot_openwrt.py        ← Main bot script (Python)
├── config.ini            ← Konfigurasi (Token, Admin ID, dll)
├── bot_session.session   ← Telegram session file
└── plugins/
    ├── system.sh         ← System monitor
    ├── clear_ram.sh      ← Memory cleaner
    ├── vnstat.sh         ← Network stats
    ├── speedtest.sh      ← Speed test
    ├── ping.sh           ← Ping test
    ├── wifi_control.sh   ← WiFi control
    ├── bandwidth.sh      ← Bandwidth monitor
    ├── block_mac.sh      ← MAC blocker
    ├── alert_monitor.sh  ← Device alert
    ├── backup_config.sh  ← Config backup
    ├── userlist.sh       ← User list
    ├── firewall.sh       ← Firewall status
    ├── reboot.sh         ← System reboot
    ├── update.sh         ← Bot updater
    └── uninstall.sh      ← Bot uninstaller
```

---

## 14. Konfigurasi (config.ini)

```ini
[Telegram]
api_id     = YOUR_API_ID        ; dari my.telegram.org
api_hash   = YOUR_API_HASH      ; dari my.telegram.org
bot_token  = YOUR_BOT_TOKEN     ; dari @BotFather
admin_id   = YOUR_TELEGRAM_ID   ; dari @userinfobot

[OpenWRT]
device_name          = OpenWRT | REVD.CLOUD
auto_backup          = true
notification_enabled = true
```

---

## 15. Troubleshooting

### Bot Tidak Start
```bash
cat /root/REVDBOT/config.ini        # Cek konfigurasi
cd /root/REVDBOT && python3 bot_openwrt.py  # Jalankan manual
opkg list-installed | grep python3  # Cek dependensi
```

### Database Locked Error
```bash
/etc/init.d/revd stop
rm -f /root/REVDBOT/bot_session.session*
/etc/init.d/revd start
```

### WiFi Control Tidak Berfungsi
```bash
opkg update && opkg install wireless-tools
uci show wireless   # Cek konfigurasi wireless
wifi status
```

### Block MAC Tidak Berfungsi
```bash
/etc/init.d/firewall restart
iptables -L | grep MAC   # Cek rules
```

---

## Ringkasan Fitur per Role

| Fitur | User Biasa | Admin |
|-------|:----------:|:-----:|
| Lihat info sistem | ✅ | ✅ |
| Bersihkan RAM | ✅ | ✅ |
| Lihat statistik jaringan | ✅ | ✅ |
| Speed test & ping | ✅ | ✅ |
| Lihat status WiFi | ✅ | ✅ |
| Lihat daftar perangkat | ✅ | ✅ |
| Lihat alert & riwayat | ✅ | ✅ |
| On/Off WiFi | ❌ | ✅ |
| Ganti password WiFi | ❌ | ✅ |
| Block/unblock MAC | ❌ | ✅ |
| Backup konfigurasi | ❌ | ✅ |
| Reboot router | ❌ | ✅ |
| Update & uninstall bot | ❌ | ✅ |

---

**Last Updated:** May 2026 | **by REVD.CLOUD**
