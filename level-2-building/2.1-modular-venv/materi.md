# 2.1: Modular Code & Virtual Environment

**Outcome:** lu bisa memecah kode menjadi beberapa file terpisah, mengimpor fungsi antar file, dan mengisolasi library menggunakan Virtual Environment (`venv`).

---

## 1. Kenapa Kode Harus Dipecah?
Di Level 1, semua kodingan ada di satu file `main.py`. Tapi di aplikasi nyata, proyek punya ribuan baris kode.
Kalau semua ditaruh di 1 file:
- Susah dibaca dan gampang konflik saat kerja tim.
- Logika bisnis campur aduk dengan urusan database.

Solusinya: **Modularitas** (pecah jadi file-file kecil yang punya tanggung jawab spesifik).

---

## 2. Cara Kerja Import Antar File
Misal lu punya 2 file di folder yang sama:

File `kalkulator.py`:
```python
def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b
```

File `app.py`:
```python
# Mengambil fungsi tertentu
from kalkulator import tambah, kali

print(tambah(5, 3))  # 8
print(kali(4, 2))    # 8
```

> **Aturan Sakti:** Jangan menamai file buatanmu sama dengan nama library bawaan Python (contoh: jangan bikin file bernama `math.py`, `random.py`, atau `email.py` karena Python bakal bingung).

---

## 3. Rahasia `if __name__ == "__main__":`
Pernah lihat baris ini di kode programmer lain?
```python
def proses_data():
    return "Data diproses"

if __name__ == "__main__":
    # Baris di dalam sini HANYA dijalankan kalau file ini di-run langsung
    # Tapi TIDAK AKAN dijalankan kalau file ini di-import oleh file lain!
    print(proses_data())
```
Ini berguna agar file modulmu bisa dites sendiri tanpa mengganggu file utama yang mengimpornya.

---

## 4. Virtual Environment (`venv`): Kamar Bersih Proyek Lu
Setiap proyek software butuh library luar (diinstall pakai `pip`).
- Masalah: Proyek A butuh library versi 1.0, tapi Proyek B butuh versi 2.0.
- Solusi: Bikin "kamar isolasi" khusus untuk tiap proyek namanya **Virtual Environment**.

### Cara Pakai di Terminal:
1. **Bikin environment baru:**
   ```bash
   python -m venv .venv
   ```
2. **Nyalakan kamar isolasi:**
   - Di Windows (PowerShell):
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - Di Mac / Linux:
     ```bash
     source .venv/bin/activate
     ```
   *(Tanda berhasil: ada tulisan `(.venv)` di sebelah kiri kursor terminal lu).*
3. **Catat daftar library:**
   ```bash
   pip freeze > requirements.txt
   ```
4. **Matikan jika selesai:**
   ```bash
   deactivate
   ```

---

## Latihan & Checkpoint
Buka `latihan/soal.md` dan `checkpoint.md` untuk mempraktikkan modular code!
