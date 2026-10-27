# 1.7: File dan CSV

**Outcome:** lu bisa membaca data dari file teks/CSV dan menyimpan hasil olahan data ke file permanen di komputer, sehingga data tidak hilang saat program ditutup.

## 1. Menyimpan dan Membaca File Teks Sederhana
Selalu gunakan pola `with open(...)` agar file otomatis tertutup dengan aman setelah selesai digunakan:

### Menulis ke File (`"w"` = write)
```python
with open("catatan.txt", "w", encoding="utf-8") as f:
    f.write("Halo dari Python!\n")
    f.write("Baris kedua.\n")
```

### Membaca Seluruh Isi File (`"r"` = read)
```python
with open("catatan.txt", "r", encoding="utf-8") as f:
    isi = f.read()
    print(isi)
```

## 2. Membaca Baris per Baris
Kalau filenya berisi banyak data transaksi atau daftar nama:
```python
with open("daftar_nama.txt", "r", encoding="utf-8") as f:
    for baris in f:
        print(f"Nama: {baris.strip()}")  # .strip() untuk buang enter (\n) di ujung
```

## 3. Apa itu CSV?
**CSV** singkatan dari *Comma-Separated Values*. Ini format data tabel paling populer di dunia (bisa dibuka di Excel / Google Sheets).

Contoh isi file `transaksi.csv`:
```csv
nama,nominal
kopi,15000
roti,10000
teh,5000
```

## 4. Mengolah CSV Tanpa Library Rumit
Di Level 1 ini, lu bisa mengolah CSV cukup pakai teknik `split(",")` yang sudah dipelajari di Modul 1.5:

```python
total = 0

with open("transaksi.csv", "r", encoding="utf-8") as f:
    header = f.readline()  # Lewati baris judul kolom pertama
    for baris in f:
        baris = baris.strip()
        if baris:
            kolom = baris.split(",")
            barang = kolom[0]
            harga = int(kolom[1])
            total = total + harga

print(f"Total pengeluaran: {total}")
```

## Latihan
Lihat `latihan/soal.md`.

## Checkpoint
Lihat `checkpoint.md`.
