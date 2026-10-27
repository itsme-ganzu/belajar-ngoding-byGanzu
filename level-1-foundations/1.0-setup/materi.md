# 1.0: Setup dan Program Pertama

**Outcome:** lu bisa jalanin file Python sendiri dan jelasin apa yang terjadi.

## Apa itu program?
Program = daftar instruksi yang dijalankan komputer, urut dari atas ke bawah. Python adalah bahasa buat nulis instruksi itu.

## Setup
1. Install Python 3 dari situs resmi python.org. Di Windows, centang **"Add Python to PATH"** saat install.
2. Install editor teks. VS Code umum dipakai, tapi editor apa pun boleh.
3. Cek: buka terminal, ketik `python --version` (atau `python3 --version` di Mac/Linux). Harus muncul versi 3.x.
   - *Catatan Windows*: Kalau ketik `python` malah membuka Microsoft Store, artinya centang PATH terlewat saat instalasi atau alias Windows aktif. Buka Settings Windows > "Manage app execution aliases" > matikan alias untuk "App Installer" (python.exe).

> Setup sering jadi titik mentok pertama. Ini normal. Kalau error, tempel pesan error ke tutor.
> Langkah persis bisa beda per sistem operasi dan versi. Kalau tampilan lu beda, cek situs resmi.

## Jalanin file
1. Bikin folder `belajar`, di dalamnya file `hello.py` berisi:
```python
print("Halo, dunia!")
```
2. Di terminal, masuk ke folder itu (`cd belajar`), lalu ketik `python hello.py`.
3. Harus muncul: `Halo, dunia!`

`print(...)` = perintah buat menampilkan sesuatu. Teks di dalam tanda kutip disebut **string**.

## Latihan
Lihat `latihan/soal.md`.

## Checkpoint
Lihat `checkpoint.md`. Jawab ke tutor dengan kata-kata lu sendiri.
