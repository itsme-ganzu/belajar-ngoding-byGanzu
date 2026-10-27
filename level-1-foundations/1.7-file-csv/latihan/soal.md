# Latihan 1.7

Bikin dua file di folder ini.

## Soal 1: `jawaban_1.py`
Buat fungsi `tulis_catatan(nama_file, daftar_teks)`:
- Menerima parameter `nama_file` (nama file tujuan, misal `"output.txt"`) dan `daftar_teks` (sebuah List of string).
- Buka file tersebut dalam mode write `"w"`, tulis setiap elemen string dalam satu baris terpisah (jangan lupa tambahkan `\n`).
- Program utama: baca input satu baris kata yang dipisahkan koma (contoh: `apel,jeruk,mangga`), panggil `tulis_catatan("buah.txt", ...)`, lalu tampilkan di terminal: `Berhasil ditulis ke buah.txt`.

## Soal 2: `jawaban_2.py`
Buat fungsi `rekap_pengeluaran(nama_file_csv)`:
- Membaca file CSV yang berisi transaksi pengeluaran.
- Format CSV memiliki header di baris 1 (`kategori,biaya`).
- Contoh baris berikutnya: `makan,25000`
- Hitung total semua biaya pengeluaran.
- Kembalikan nilai total tersebut (tipe integer).
- Program utama: terima input nama file CSV dari terminal, panggil fungsinya, lalu tampilkan: `Total biaya: <total>`.

## Tes
Dari folder `latihan`:
```
python test_1_7.py
```
