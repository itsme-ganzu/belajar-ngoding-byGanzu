# 1.4: Fungsi (Function)

**Outcome:** lu bisa membungkus logika program ke dalam fungsi dengan `def`, paham bedanya `return` vs `print`, serta paham konsep parameter dan scope.

## Kenapa butuh fungsi?
Bayangkan lu punya rumus hitung diskon yang rumit. Kalau di tokomu rumus itu dipakai di halaman kasir, keranjang belanja, dan struk pembayaran, lu nggak mau copy-paste rumus itu 3 kali. Jika rumusnya berubah, lu harus ubah di 3 tempat berbeda.

Fungsi membungkus logika ke dalam satu nama. Tinggal panggil namanya kapan pun lu butuh.

## 1. Anatomi Fungsi: `def`, Parameter, dan `return`
```python
def sapa(nama):
    return f"Halo, {nama}!"
```
- `def`: kata kunci untuk mendefinisikan fungsi (singkatan dari *define*).
- `sapa`: nama fungsi buatan lu.
- `(nama)`: **parameter**, yaitu variabel penampung data yang dikirim ke dalam fungsi.
- `return`: mengembalikan nilai hasil kerja fungsi ke pemanggilnya.

Cara memanggilnya:
```python
pesan = sapa("Budi")
print(pesan)  # Mencetak: Halo, Budi!
```

## 2. Paling Krusial: `return` vs `print`
Ini kesalahan nomor satu pemula dalam memahami fungsi:
- `print(...)` **hanya menampilkan teks** di layar hitam terminal. Hasilnya menguap begitu saja dan tidak bisa dihitung lagi.
- `return ...` **mengirimkan data kembali** sehingga nilainya bisa disimpan ke variabel atau dihitung lebih lanjut.

Perhatikan jebakan ini:
```python
# CONTOH SALAH (Pakai print di dalam fungsi)
def tambah_salah(a, b):
    print(a + b)

hasil = tambah_salah(3, 4)  # Layar mencetak 7, tapi variabel hasil bernilai None!
# print(hasil * 2)  --> BAKAL ERROR (TypeError: unsupported operand type for NoneType)

# CONTOH BENAR (Pakai return)
def tambah_benar(a, b):
    return a + b

hasil = tambah_benar(3, 4)
print(hasil * 2)  # Mencetak: 14 (bisa dihitung lagi!)
```

## 3. Scope: Variabel Lokal vs Global
Variabel yang lu bikin di dalam fungsi bersifat **lokal**. Variabel itu lahir saat fungsi dipanggil, dan langsung mati saat fungsi selesai.

```python
def buat_angka():
    rahasia = 99
    return rahasia

buat_angka()
# print(rahasia)  --> ERROR! (NameError: name 'rahasia' is not defined)
```
Dunia luar tidak kenal siapa itu `rahasia`.

## Latihan
Lihat `latihan/soal.md`.

## Checkpoint
Lihat `checkpoint.md`.
