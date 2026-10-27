# Latihan 1.4

Bikin dua file di folder ini.

## Soal 1: `jawaban_1.py`
1. Tulis sebuah fungsi bernama `celcius_ke_fahrenheit(c)` yang menerima parameter suhu Celcius (`c`), lalu me-`return` nilai suhu dalam Fahrenheit.
   - Rumus: `(c * 9/5) + 32`
2. Di luar fungsi, program meminta input suhu Celcius dari terminal, memanggil fungsi tersebut, lalu menampilkan hasil konversi.
   - Format output: `Fahrenheit: <hasil>`

Contoh 1:
Input: `0`
Output: `Fahrenheit: 32.0`

Contoh 2:
Input: `100`
Output: `Fahrenheit: 212.0`

## Soal 2: `jawaban_2.py`
1. Tulis sebuah fungsi bernama `hitung_parkir(jam)` yang menerima parameter lama parkir (dalam jam, bilangan bulat) dan me-`return` total biaya parkir:
   - Aturan:
     - Tarif dasar 2 jam pertama flat Rp 5.000 (parkir 1 jam atau 2 jam tetap Rp 5.000).
     - Tiap jam tambahan berikutnya (jam ke-3 dan seterusnya) dikenakan tambahan Rp 2.000 per jam.
   - Contoh perhitungan fungsi:
     - `hitung_parkir(1)` -> 5000
     - `hitung_parkir(2)` -> 5000
     - `hitung_parkir(3)` -> 5000 + 2000 = 7000
     - `hitung_parkir(5)` -> 5000 + (3 * 2000) = 11000
2. Di luar fungsi, program meminta input lama parkir dari terminal, memanggil fungsinya, lalu menampilkan:
   - Format output: `Biaya: <total>`

## Tes
Dari folder `latihan`:
```
python test_1_4.py
```
Kalau tes gagal, baca pesan error di terminal sebelum bertanya ke tutor.
