# Latihan 1.8: Ujian Mini Proyek Level 1

Buat satu file bernama `pengeluaran.py` di folder ini.

## Alur Program:
Program harus berjalan terus-menerus menggunakan loop `while` sampai user memilih menu `3`.

1. Jika user memilih `1`:
   - Minta input `nama`
   - Minta input `nominal`
   - Buka `data_pengeluaran.csv` mode `"a"` dan tambahkan baris `nama,nominal\n`
   - Cetak `Berhasil dicatat!`
2. Jika user memilih `2`:
   - Baca file `data_pengeluaran.csv` (jika ada)
   - Hitung total uang yang dikeluarkan
   - Cetak persis format: `Total pengeluaran: <angka>` (contoh: `Total pengeluaran: 40000`)
3. Jika user memilih `3`:
   - Cetak `Sampai jumpa!` dan keluar dari perulangan.

## Tes Mandiri:
Dari folder `latihan`:
```
python test_1_8.py
```
Pastikan semua tes lulus (`OK`) sebelum lu maju ke Modul Jembatan!
