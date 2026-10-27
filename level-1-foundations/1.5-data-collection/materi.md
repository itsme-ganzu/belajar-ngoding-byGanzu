# 1.5: List, Dictionary, dan Manipulasi String

**Outcome:** lu bisa mengelola banyak data sekaligus, memahami pasangan data *key-value*, serta membersihkan/memproses teks input.

## 1. List (Daftar Terurut)
Kalau punya 10 nama murid, lu tidak perlu bikin variabel `nama1`, `nama2`, dst. Pakai **List**:
```python
buah = ["apel", "jeruk", "mangga"]
```

Operasi dasar:
- **Mengambil data lewat indeks:** `buah[0]` menghasilkan `"apel"`. Indeks negatif `buah[-1]` mengambil item paling belakang (`"mangga"`).
- **Menambah data:** `buah.append("pisang")`.
- **Cek jumlah data:** `len(buah)`.
- **Perulangan pada list:**
```python
for item in buah:
    print(f"Saya suka {item}")
```

## 2. Dictionary (Kamus Key-Value)
List memakai urutan angka (0, 1, 2...). Tapi jika datanya adalah profil orang atau menu toko yang punya label nama, **Dictionary** jauh lebih pas:

```python
kontak = {
    "nama": "Budi",
    "kota": "Bandung",
    "umur": 20
}
```
- `"nama"` disebut **key** (kunci).
- `"Budi"` disebut **value** (nilai).

Operasi dasar:
- **Mengambil nilai:** `kontak["nama"]` -> `"Budi"`.
- **Menambah / mengubah:** `kontak["email"] = "budi@mail.com"`.
- **Mengecek apakah key ada:**
```python
if "kota" in kontak:
    print("Ada data kota!")
```

## 3. Manipulasi String Praktis
Saat menerima input dari user, teks sering kali berantakan (ada spasi berlebih atau campuran huruf besar-kecil).

- `.strip()`: membuang spasi kosong di ujung kiri dan kanan.
  ```python
  teks = "  halo  "
  print(teks.strip())  # "halo"
  ```
- `.lower()` / `.upper()`: mengubah ke huruf kecil atau huruf besar semua.
  ```python
  role = "ADMIN".lower()  # "admin"
  ```
- `.split(",")`: memotong string menjadi List berdasarkan tanda pemisah.
  ```python
  daftar = "10,20,30".split(",")
  print(daftar)  # ["10", "20", "30"] (tiap elemen masih berupa string)
  ```

## Latihan
Lihat `latihan/soal.md`.

## Checkpoint
Lihat `checkpoint.md`.
