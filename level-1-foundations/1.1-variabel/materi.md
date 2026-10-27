# 1.1: Variabel, Tipe Data, Input/Output

**Outcome:** lu bisa nyimpen data di variabel, nerima input, ngitung, dan nampilin hasil.

## Variabel
Variabel = kotak berlabel buat nyimpen nilai.
```python
nama = "Budi"
umur = 20
```
`=` artinya "simpan nilai di kanan ke variabel di kiri", bukan "sama dengan" ala matematika.

## Tipe data dasar
- `str` (teks): `"Budi"`
- `int` (bilangan bulat): `20`
- `float` (desimal): `3.5`

Cek tipe: `type(umur)`.

## Output
```python
print("Halo,", nama)
print(f"Umur: {umur}")   # f-string: variabel disisipin pakai {}
```

## Input
```python
nama = input("Siapa nama lu? ")
```
**Penting:** `input()` selalu menghasilkan **string**, bahkan kalau lu ngetik angka. Buat ngitung, ubah dulu:
```python
umur = int(input("Umur? "))
print(umur + 1)
```
Kalau lupa `int(...)`, `"20" + 1` bakal error. Ini salah satu error pertama yang sering dialami pemula.

## Operasi hitung
`+  -  *  /` (tambah, kurang, kali, bagi desimal).
Operator khusus:
- `//` (pembagian bulat/buang koma): `7 // 2` hasilnya `3`
- `%` (sisa bagi / modulo): `7 % 3` hasilnya `1` (karena 7 dibagi 3 dapat 2, sisa 1)
- `**` (pangkat): `2 ** 3` hasilnya `8`

Coba satu-satu di file kecil dan tebak hasilnya dulu sebelum jalanin.

## Latihan
Lihat `latihan/soal.md`.

## Checkpoint
Lihat `checkpoint.md`.
