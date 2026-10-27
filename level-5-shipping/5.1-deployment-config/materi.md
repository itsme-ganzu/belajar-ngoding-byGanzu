# 5.1: Konfigurasi Deployment & Environment Variables

**Outcome:** kodinganmu bisa dipindahkan dari laptop lokal dan berjalan stabil di server internet publik tanpa mengekspos kredensial rahasia.

---

## 1. Perbedaan "Laptop Gue" vs "Server Produksi"
Di laptop lokal, lu bisa klik tombol *Run* di VS Code.
Tapi di server cloud (Linux):
- Tidak ada layar visual.
- Program harus berjalan 24 jam nonstop di background (*daemon/service*).
- Konfigurasi server tidak boleh di-hardcode di file Python.

---

## 2. Prinsip "12-Factor App": Config in Environment
Jangan pernah menulis database URL atau token langsung di file:
```python
# CARA BENAR:
import os

PORT = int(os.environ.get("PORT", 8000))
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///toko.db")
```

Di server produksi (misal: Railway, Render, atau VPS Ubuntu), variabel tersebut disetel lewat menu *Dashboard Environment Variables*.
