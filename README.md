# 🚀 SPAMWAHD - Auto Chat Tool

**A simple and efficient automated messaging tool for WhatsApp** 🔧💬

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Issues](https://img.shields.io/github/issues/KiandrAHD/SPAMWAHD---Auto-Chat-Tool?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KiandrAHD/SPAMWAHD---Auto-Chat-Tool/issues)
[![Stars](https://img.shields.io/github/stars/KiandrAHD/SPAMWAHD---Auto-Chat-Tool?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KiandrAHD/SPAMWAHD---Auto-Chat-Tool/stargazers)

---

## ⚠️ DISCLAIMER - BACA DULU YA!

> [!WARNING]
> ### 🛑 PERINGATAN PENTING
>
> **Alat ini dibuat HANYA untuk tujuan EDUKASI dan PENGUJIAN LOKAL.**
>
> - 🚫 **DILARANG** menggunakan alat ini untuk mengirim spam, pesan massal yang mengganggu, atau aktivitas yang melanggar **Kebijakan WhatsApp**.
> - ⚠️ **Risiko Pemblokiran Akun**: Penggunaan alat ini secara tidak wajar atau berlebihan dapat menyebabkan **akun WhatsApp Anda diblokir / di-ban secara permanen** oleh WhatsApp.
> - 🧪 Gunakan hanya pada **grup percobaan**, chat pribadi milik Anda sendiri, atau lingkungan pengujian yang aman.
> - 👨‍💻 Pengembang **tidak bertanggung jawab** atas penyalahgunaan, kerugian, atau dampak yang ditimbulkan dari penggunaan alat ini.

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
| :--- | :--- |
| 📨 **Pesan Otomatis** | Mengirim pesan secara berulang tanpa perlu mengetik manual berulang kali. |
| ⏱️ **Jeda Waktu (Delay)** | Memberikan jeda acak antar pengiriman untuk mensimulasikan aktivitas manusia. |
| 📝 **Kustomisasi Teks** | Bebas menentukan teks pesan yang ingin dikirim. |
| 🔢 **Atur Jumlah Pesan** | Menentukan berapa kali pesan akan dikirim. |
| 🖱️ **CLI Sederhana** | Antarmuka berbasis Command Line yang mudah dan ringan. |
| 🚦 **Mode Aman (Failsafe)** | Fitur `FAILSAFE` aktif - gerakkan kursor ke pojok layar untuk menghentikan program darurat. |
| ⌨️ **Interupsi Manual** | Tekan `Ctrl + C` kapan saja untuk menghentikan proses pengiriman. |

---

## 🧰 Tech Stack & Prasyarat

### 🐍 Bahasa Pemrograman
- **[Python](https://www.python.org/) 3.8+**

### 📦 Library yang Dibutuhkan
- **[PyAutoGUI](https://pyautogui.readthedocs.io/)** - Untuk mengontrol mouse & keyboard secara otomatis.
- `time` (built-in) - Untuk jeda waktu.
- `random` (built-in) - Untuk delay acak.
- `os` (built-in) - Untuk membersihkan layar terminal.

### 🖥️ Prasyarat Sistem
- ✅ **Python 3.8+** sudah terinstall.
- ✅ **Pip** (Python Package Manager).
- ✅ **Browser** (Chrome / Firefox / Edge) untuk membuka **WhatsApp Web**.
- ✅ **Akun WhatsApp** yang aktif (sudah terscan QR di WhatsApp Web).
- ✅ **Koneksi Internet** yang stabil.

---

## 🚀 Panduan Instalasi & Penggunaan

### 📥 1. Clone Repository

Buka terminal / command prompt, lalu jalankan:

```bash
git clone https://github.com/KiandrAHD/SPAMWAHD---Auto-Chat-Tool.git
cd SPAMWAHD---Auto-Chat-Tool
```

### ⚙️ 2. Install Dependensi

Install library `pyautogui`:

```bash
pip install pyautogui
```

> 💡 **Tips**: Disarankan menggunakan **virtual environment** (venv) agar tidak mengganggu environment global:
> ```bash
> python -m venv venv
> # Windows
> venv\Scripts\activate
> # MacOS / Linux
> source venv/bin/activate
> pip install pyautogui
> ```

### 🏃 3. Jalankan Skrip

```bash
python spam_wa.py
```

### 📋 Langkah Penggunaan (Step by Step)

1. ▶️ **Jalankan skrip** dengan perintah di atas.
2. 📨 **Masukkan pesan** yang ingin dikirim, lalu tekan `Enter`.
3. 🔢 **Masukkan jumlah** berapa kali pesan akan dikirim.
4. 🖱️ **Buka WhatsApp Web** di browser, pilih chat tujuan, lalu **arahkan kursor** ke kolom chat (program memberi waktu 5 detik).
5. 📌 **Posisi kursor akan dikunci** - jangan pindahkan kursor setelah proses dimulai.
6. ⏳ Tunggu hitung mundur 3 detik, lalu **proses pengiriman otomatis dimulai**.
7. ✅ Setelah selesai, total pesan yang terkirim akan ditampilkan di layar.

### 🛑 Cara Menghentikan Program

| Metode | Cara |
| :--- | :--- |
| ⌨️ **Ctrl + C** | Hentikan proses secara manual di terminal. |
| 🖱️ **Failsafe** | Gerakkan kursor dengan cepat ke **pojok kiri atas layar** untuk memicu penghentian darurat. |

---

## 📁 Struktur Folder Proyek

```
SPAMWAHD---Auto-Chat-Tool/
│
├── 📄 spam_wa.py          # Skrip utama: logika otomatisasi pengiriman pesan
├── 📄 README.md           # Dokumentasi proyek (file ini)
└── 📄 LICENSE             # Lisensi proyek (MIT License)
```

### 📄 Penjelasan File

| File | Fungsi |
| :--- | :--- |
| **spam_wa.py** | File utama yang berisi seluruh logika program - menerima input pesan, menangkap posisi kursor, melakukan klik & ketik otomatis, serta menangani jeda waktu dan error handling. |
| **README.md** | Dokumentasi proyek yang menjelaskan cara instalasi, penggunaan, dan informasi penting lainnya. |
| **LICENSE** | Berisi lisensi resmi proyek (MIT License). |

---

## 🛠️ Customization (Opsional)

Kamu bisa mengubah perilaku skrip dengan memodifikasi beberapa bagian di `spam_wa.py`:

```python
# Ubah rentang jeda waktu antar pesan (dalam detik)
delay = random.uniform(0.4, 1.0)  # Misal: 1.0 - 3.0 agar lebih pelan

# Matikan / aktifkan failsafe
pyautogui.FAILSAFE = True  # Ubah ke False jika ingin menonaktifkan (tidak disarankan!)
```

---

## ⚖️ Lisensi

Proyek ini dilisensikan di bawah **MIT License** - silakan lihat file [LICENSE](LICENSE) untuk detail lengkap.

```

MIT License

Copyright (c) 2026 KiandrAHD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 👨‍💻 Penulis & Kredit

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/KiandrAHD">
        <img src="https://github.com/KiandrAHD.png" width="80" height="80" style="border-radius: 50%;" alt="KiandrAHD"/><br />
        <b>KiandrAHD</b>
      </a>
      <br />
      🧑‍💻 Creator & Developer
      <br />
      <a href="https://github.com/KiandrAHD">🔗 GitHub</a>
    </td>
  </tr>
</table>

---

## 🙏 Dukungan

Jika proyek ini bermanfaat, jangan lupa untuk:

- ⭐ **Star** repository ini
- 🍴 **Fork** untuk pengembangan lebih lanjut
- 🐛 **Report issue** jika menemukan bug

---

<div align="center">

**Dibuat dengan ❤️ dan ☕ untuk tujuan edukasi**

© 2026 [KiandrAHD](https://github.com/KiandrAHD) - MIT License

</div>