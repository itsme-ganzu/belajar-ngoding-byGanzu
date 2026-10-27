# 1.6: Baca Error dan Debugging

**Outcome:** lu nggak takut lagi lihat teks merah di terminal, paham cara membaca pesan error (Traceback), dan bisa membetulkan bug mandiri.

## 1. Jangan Panik Lihat Warna Merah
Pesan error di terminal bukan tanda lu bodoh. Pesan error itu adalah **komputer berusaha ngasih tahu persis di mana dan kenapa dia bingung**.

## 2. Cara Membaca Traceback
Traceback selalu dibaca dari **PALING BAWAH**.

Contoh error:
```text
Traceback (most recent call last):
  File "program.py", line 4, in <module>
    print(umur + 1)
TypeError: can only concatenate str (not "int") to str
```

Langkah membacanya:
1. **Lihat baris paling bawah:** `TypeError: can only concatenate str (not "int") to str`.
   - Artinya: Python mencoba menggabungkan teks dengan angka, padahal tidak bisa.
2. **Lihat baris di atasnya:** `File "program.py", line 4`.
   - Artinya: Masalahnya terjadi di file `program.py` pada baris ke-4.

## 3. Jenis-Jenis Error yang Paling Sering Muncul

### A. `SyntaxError` (Salah Tata Bahasa)
Terjadi saat lu salah ngetik aturan Python (lupa titik dua `:`, lupa tutup kurung `)`, atau salah ketik kata kunci).
```python
if x == 5   # Lupa titik dua di ujung!
```

### B. `NameError` (Variabel Tidak Dikenal)
Terjadi karena salah eja nama variabel, atau memanggil variabel yang belum pernah dibuat.
```python
nama = "Budi"
print(nma)  # NameError: name 'nma' is not defined (typo!)
```

### C. `TypeError` (Salah Tipe Data)
Operasi yang tidak cocok untuk tipe data tertentu.
```python
panjang = len(100)  # TypeError: object of type 'int' has no len()
```

### D. `IndexError` (Indeks Kejauhan)
Mengakses nomor urut list yang tidak ada.
```python
angka = [1, 2]
print(angka[5])  # IndexError: list index out of range
```

### E. `KeyError` (Key Kamus Tidak Ada)
Mengambil data di dictionary dengan key yang belum terdaftar.
```python
user = {"nama": "Ali"}
print(user["email"])  # KeyError: 'email'
```

## 4. Teknik Debugging: "Print Debugging"
Kalau hasil programmu aneh tapi tidak mengeluarkan error merah:
Sisipkan `print()` di setiap tahapan untuk mengecek isi variabelnya!
```python
print(f"[DEBUG] isi variabel x sekarang: {x}")
```

## Latihan
Lihat `latihan/soal.md`.

## Checkpoint
Lihat `checkpoint.md`.
