# Latihan 1.3

Bikin dua file di folder ini.

## Soal 1: `jawaban_1.py`
Program meminta input sebuah bilangan bulat positif `N`.
Hitung jumlah total penjumlahan dari `1` sampai `N` (`1 + 2 + ... + N`), lalu tampilkan dengan format persis:
```
Jumlah: <angka>
```

Contoh 1:
Input: `5`
Perhitungan: 1 + 2 + 3 + 4 + 5 = 15
Output: `Jumlah: 15`

Contoh 2:
Input: `1`
Output: `Jumlah: 1`

*(Petunjuk: ingat batas akhir `range(1, N + 1)`)*

## Soal 2: `jawaban_2.py`
Program simulasi tebak PIN sederhana. PIN rahasia toko adalah `1234`.
- Minta input PIN dari user.
- Jika PIN salah, tampilkan `PIN salah, coba lagi.` dan minta input lagi berulang kali.
- Jika PIN benar (`1234`), tampilkan `Akses diterima!` dan program berhenti.

Contoh interaksi terminal:
```
PIN salah, coba lagi.
PIN salah, coba lagi.
Akses diterima!
```
(Jika user salah memasukkan PIN sebanyak 2 kali sebelum memasukkan `1234` yang benar).

## Tes
Dari folder `latihan`:
```
python test_1_3.py
```
Kalau tes gagal, baca pesan error di terminal sebelum bertanya ke tutor.
