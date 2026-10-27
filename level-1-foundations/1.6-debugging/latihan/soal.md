# Latihan 1.6

Di latihan ini tugas lu adalah menjadi "Detektif Kode". Perbaiki kode yang error.

Bikin dua file di folder ini.

## Soal 1: `jawaban_1.py`
Seseorang menulis fungsi `hitung_rata_rata(angka_list)` seperti ini tapi programnya selalu crash dengan `ZeroDivisionError` saat list kosong, dan crash `TypeError` saat inputnya string angka:
```python
def hitung_rata_rata(angka_list):
    total = 0
    for x in angka_list:
        total = total + int(x)
    if len(angka_list) == 0:
        return 0
    return total / len(angka_list)
```
Tugasmu: Tulis fungsi `hitung_rata_rata(angka_list)` yang aman:
- Jika list kosong `[]`, langsung return `0` (jangan sampai terjadi pembagian dengan nol!).
- Elemen di dalam list bisa berupa integer atau string angka (misal `["10", "20"]` atau `[10, 20]`), pastikan semuanya diubah ke integer dengan aman.
- Return nilai rata-ratanya.

Di bawah fungsi, baca input satu baris angka yang dipisahkan koma (contoh input: `10,20,30` atau kosong), panggil fungsi dan tampilkan:
```
Rata-rata: <hasil>
```
*(Jika input kosong, tampilkan `Rata-rata: 0`)*

## Soal 2: `jawaban_2.py`
Toko buku punya fungsi pencari harga buku:
```python
KATALOG = {
    "python": 50000,
    "javascript": 60000,
    "sql": 45000
}
```
Program sering crash dengan pesan `KeyError` kalau pembeli mencari buku yang tidak ada.
Tulis program yang:
- Menerima input judul buku dari user (bersihkan spasi liar dan buat lowercase).
- Gunakan pengecekan kondisi yang aman (misal `if judul in KATALOG:`) agar **TIDAK PERNAH TERJADI KeyError**.
- Jika buku ada, tampilkan: `Harga: <harga>`
- Jika buku tidak ada, tampilkan: `Buku tidak tersedia`

## Tes
Dari folder `latihan`:
```
python test_1_6.py
```
