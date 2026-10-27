# Latihan 1.2

Bikin dua file di folder ini.

## Soal 1: `jawaban_1.py`
Program minta input **suhu air** (dalam angka bulat).
- Jika suhu `<= 0`: tampilkan `Beku`
- Jika suhu `1` sampai `99` (inklusif): tampilkan `Cair`
- Jika suhu `>= 100`: tampilkan `Uap`

Contoh:
Input: `25`
Output: `Cair`

## Soal 2: `jawaban_2.py`
Program minta input **total belanja** (angka bulat).
Aturan diskon toko:
- Jika belanja minimal `100000` (seratus ribu atau lebih), dapat diskon 10%.
- Jika kurang dari `100000`, tidak ada diskon (diskon 0%).

Tampilkan total akhir yang harus dibayar (angka bulat).
Format output persis: `Bayar: <angka>`

Contoh 1:
Input: `150000`
Output: `Bayar: 135000`

Contoh 2:
Input: `50000`
Output: `Bayar: 50000`

*(Petunjuk: untuk diskon 10%, potongan harga = `int(total * 0.1)`. Bayar = `total - potongan`)*

## Tes
Dari folder `latihan`:
```
python test_1_2.py
```
Kalau gagal, baca pesan error di terminal sebelum bertanya ke tutor.
