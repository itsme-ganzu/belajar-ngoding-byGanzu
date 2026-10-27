# 1.8: Mini Proyek Level 1 (Pencatat Pengeluaran)

**Outcome:** lu berhasil menggabungkan SEMUA materi Level 1 (variabel, kondisi, loop, fungsi, list/dict, dan file CSV) menjadi satu aplikasi terminal yang utuh dan berguna.

> **ATURAN GERBANG LEVEL 1:**
> Kerjakan proyek ini sendiri tanpa bantuan AI tutor! Gunakan catatan materi 1.0 s/d 1.7 sebagai referensi. Jika lu stuck, ingat teknik debugging di modul 1.6.

## Spesifikasi Proyek: `pengeluaran.py`
Aplikasi ini bertugas mencatat dan merekap pengeluaran harian ke file `data_pengeluaran.csv`.

Saat program dijalankan, tampilkan menu interaktif:
```text
=== PENCATAT PENGELUARAN ===
1. Tambah Transaksi
2. Lihat Total Pengeluaran
3. Keluar
Pilih menu (1/2/3): 
```

### Menu 1: Tambah Transaksi
- Minta input nama pengeluaran (misal: `kopi`).
- Minta input nominal pengeluaran (angka bulat, misal: `15000`).
- Simpan baris baru ke file `data_pengeluaran.csv` dengan format: `nama,nominal\n`. (Gunakan mode `"a"` / append).
- Tampilkan pesan: `Berhasil dicatat!` lalu kembali ke menu utama.

### Menu 2: Lihat Total Pengeluaran
- Jika file `data_pengeluaran.csv` belum ada atau masih kosong, tampilkan: `Total pengeluaran saat ini: Rp 0`.
- Jika sudah ada data, baca semua baris, jumlahkan seluruh nominal, lalu tampilkan: `Total pengeluaran saat ini: Rp <total>`.
- Kembali ke menu utama.

### Menu 3: Keluar
- Tampilkan: `Sampai jumpa!` dan hentikan program (`break`).

## Latihan & Pengujian
Lihat `latihan/soal.md` dan jalankan `python test_1_8.py`.
