# 1.2: Kondisi dan Logika Boolean

**Outcome:** program lu bisa mengambil keputusan berbeda berdasarkan kondisi tertentu.

## Logika Boolean
Tipe data boolean cuma punya dua nilai: `True` (benar) atau `False` (salah).

Kita dapat nilai ini lewat perbandingan:
- `==` sama dengan (contoh: `5 == 5` -> `True`)
- `!=` tidak sama dengan (contoh: `5 != 3` -> `True`)
- `>` lebih besar dari
- `<` lebih kecil dari
- `>=` lebih besar atau sama dengan
- `<=` lebih kecil atau sama dengan

> **Peringatan:** bedakan `=` (menyimpan nilai ke variabel) dengan `==` (mengecek apakah dua nilai sama).

## Percabangan: `if`, `elif`, `else`
```python
nilai = 75

if nilai >= 75:
    print("Selamat, lu lulus!")
else:
    print("Belum lulus, coba lagi ya.")
```

**Aturan penting (Indentasi):**
Baris di dalam `if` harus digeser ke kanan (tekan Tab atau 4 spasi). Python menggunakan spasi geser (indentasi) ini untuk tahu baris mana yang masuk ke dalam blok `if`.

## Banyak Kondisi: `elif`
Kalau pilihannya lebih dari dua:
```python
skor = 85

if skor >= 90:
    print("A")
elif skor >= 75:
    print("B")
elif skor >= 60:
    print("C")
else:
    print("Perlu remidi")
```
Python akan mengecek dari atas ke bawah. Kondisi pertama yang bernilai `True` akan dijalankan, lalu sisanya dilewati.

## Menggabungkan Logika: `and`, `or`, `not`
- `and`: dua-duanya harus `True` (contoh: `umur >= 17 and punya_ktp == True`)
- `or`: salah satu cukup `True`
- `not`: membalikkan nilai (`not True` jadi `False`)

## Latihan
Lihat `latihan/soal.md`.

## Checkpoint
Lihat `checkpoint.md`.
