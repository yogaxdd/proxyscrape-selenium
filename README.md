# YogaxD ProxyScrape Selenium Automation

Script otomatisasi untuk membuat akun ProxyScrape menggunakan Selenium WebDriver.

## 📋 Deskripsi

Script ini mengotomatisasi proses pembuatan akun di ProxyScrape dengan fitur:
- Auto-fill form signup
- Generate password random
- Handle verifikasi email
- User-agent rotation

## 🚀 Fitur

- ✅ Otomatis buka halaman trial ProxyScrape
- ✅ Klik tombol "Start Free Trial"
- ✅ Auto-fill email (input manual di console)
- ✅ Generate password random
- ✅ Centang "I agree" terms
- ✅ Pause untuk verifikasi captcha manual
- ✅ Auto-fill form onboarding
- ✅ Handle verifikasi email
- ✅ Rotasi User-Agent

## 📦 Prerequisites

### Python Dependencies
```bash
pip install selenium webdriver-manager undetected_chromedriver
```

### Browser
- Google Chrome (akan di-download otomatis oleh webdriver-manager)

## 🛠️ Instalasi

1. **Clone repository**
```bash
git clone <repository-url>
cd proxyscrape-selenium
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Jalankan script**
```bash
python main.py
```

## 📁 Struktur File

```
proxyscrape-selenium/
├── main.py          # Script utama otomatisasi
├── ua.txt           # Database User-Agent untuk rotasi
├── requirements.txt # Dependencies Python
└── README.md        # Dokumentasi ini
```

## 🔧 Cara Penggunaan

### 1. Jalankan Script
```bash
python main.py
```

### 2. Ikuti Instruksi Console
Script akan meminta input manual di beberapa titik:

- **Email**: Masukkan email untuk signup
- **Verifikasi Captcha**: Verifikasi "Are You Human" secara manual
- **Kode Email**: Masukkan kode verifikasi yang dikirim ke email

### 3. Flow Otomatisasi
1. Buka halaman trial ProxyScrape
2. Klik "Start Free Trial"
3. Input email di console
4. Generate password random
5. Centang terms & conditions
6. Verifikasi captcha manual
7. Klik "Sign Up"
8. Pilih "Individual" pada onboarding
9. Isi "Web Scraping and Data Extraction"
10. Input kode verifikasi email
11. Setup IP authentication
12. Add current IP address

## ⚙️ Konfigurasi

### User-Agent Rotation
Script menggunakan rotasi User-Agent dari file `ua.txt` untuk menghindari deteksi bot.

### Timeout Settings
```python
wait = WebDriverWait(driver, 30)  # 30 detik timeout
```

### Password Generation
```python
def random_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))
```

## 🐛 Troubleshooting

### Error: TimeoutException
- Pastikan koneksi internet stabil
- Cek apakah website ProxyScrape tidak berubah struktur
- Coba jalankan ulang script

### Error: Element Not Found
- Website mungkin sudah berubah selector
- Cek console untuk debug info
- Update selector di script jika diperlukan

### Error: ChromeDriver
```bash
# Reinstall webdriver-manager
pip uninstall webdriver-manager
pip install webdriver-manager
```

## 📝 Log Output

Script akan menampilkan:
- Password yang di-generate
- Status setiap langkah otomatisasi
- Error jika terjadi masalah

## 🔒 Keamanan

- Password di-generate random dan ditampilkan di console
- Email harus diinput manual (tidak disimpan di script)
- Kode verifikasi harus diinput manual

## 📄 License

Project ini dibuat untuk tujuan edukasi dan testing otomatisasi web.

## 🤝 Contributing

1. Fork repository
2. Buat feature branch
3. Commit changes
4. Push ke branch
5. Buat Pull Request

## 📞 Support

Jika ada masalah atau pertanyaan:
- Cek section Troubleshooting
- Buat issue di repository
- Pastikan semua dependencies terinstall dengan benar

---

**Note**: Script ini dibuat untuk tujuan edukasi. Pastikan penggunaan sesuai dengan Terms of Service ProxyScrape. 
