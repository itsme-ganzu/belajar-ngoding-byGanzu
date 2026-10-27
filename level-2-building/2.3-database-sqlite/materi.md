# 2.3: Database Lokal SQLite

**Outcome:** lu bisa menyimpan data aplikasi ke database relasional SQLite menggunakan bahasa SQL standar, bukan lagi sekadar file CSV manual.

---

## 1. Kenapa Beralih dari CSV ke Database?
File CSV punya kelemahan besar:
- Lambat jika data sudah mencapai puluhan ribu baris.
- Rawan rusak jika ada 2 proses yang menulis bersamaan.
- Sulit melakukan pencarian kompleks (misal: mencari user di kota X yang belanja di atas Rp 100.000).

**SQLite** adalah database relasional kelas industri yang **sudah bawaan terpasang di Python** (tanpa perlu install server rumit). Semua data disimpan rapi dalam 1 file berekstensi `.db`.

---

## 2. 4 Operasi Inti SQL (CRUD: Create, Read, Update, Delete)

Di Python, kita menggunakan modul `sqlite3`:

```python
import sqlite3

# 1. Hubungkan ke database (otomatis bikin file jika belum ada)
conn = sqlite3.connect("toko.db")
cursor = conn.cursor()

# 2. CREATE TABLE (Bikin tabel baru jika belum ada)
cursor.execute("""
CREATE TABLE IF NOT EXISTS produk (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    harga INTEGER NOT NULL
)
""")

# 3. INSERT (Menambah data baru)
cursor.execute("INSERT INTO produk (nama, harga) VALUES (?, ?)", ("Kopi", 15000))
conn.commit()  # Wajib commit agar data tersimpan permanen!

# 4. SELECT (Membaca data)
cursor.execute("SELECT id, nama, harga FROM produk WHERE harga > ?", (10000,))
semua_data = cursor.fetchall()
for baris in semua_data:
    print(baris)  # Contoh: (1, 'Kopi', 15000)

# 5. Tutup koneksi
conn.close()
```

> **Aturan Keamanan:** Jangan pernah menggabungkan variabel langsung dengan string SQL seperti `"INSERT ... VALUES ('" + nama + "')"`. Selalu gunakan tanda tanya `?` (parameterized query) untuk mencegah serangan hacker **SQL Injection**!
