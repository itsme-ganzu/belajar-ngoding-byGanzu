# Latihan 1.5

Bikin dua file di folder ini.

## Soal 1: `jawaban_1.py`
1. Tulis sebuah fungsi bernama `analisis_nilai(daftar_angka)` yang menerima sebuah List of integer (kumpulan angka), lalu me-`return` sebuah dictionary dengan format:
   ```python
   {"tertinggi": <angka_tertinggi>, "rata_rata": <nilai_rata_rata>}
   ```
   *(Catatan: rata-rata dihitung dari total dibagi jumlah elemen)*
2. Di luar fungsi, program meminta satu baris input berisi angka-angka yang dipisahkan koma dari user (contoh input: `70,80,90` atau `70, 80, 90`), ubah menjadi List of integer, panggil fungsi tersebut, lalu tampilkan:
   ```
   Tertinggi: 90
   Rata-rata: 80.0
   ```

## Soal 2: `jawaban_2.py`
Simulasi kasir kantin mini.
Tersedia menu barang dan harganya dalam bentuk dictionary:
```python
MENU = {
    "kopi": 15000,
    "teh": 5000,
    "roti": 10000
}
```
Program meminta input satu nama pesanan dari user.
- Tangani huruf besar-kecil dan spasi liar (contoh user ngetik `  KOPI  ` atau `Teh`, program tetap mengenali).
- Jika menu ada, tampilkan: `Harga: <harga>`
- Jika menu tidak ada di daftar, tampilkan: `Menu tidak ditemukan`

Contoh 1:
Input: `Kopi`
Output: `Harga: 15000`

Contoh 2:
Input: `Burger`
Output: `Menu tidak ditemukan`

## Tes
Dari folder `latihan`:
```
python test_1_5.py
```
Kalau tes gagal, baca pesan error di terminal sebelum bertanya ke tutor.
