# 2.2: Testing Otomatis dengan Pytest

**Outcome:** lu tahu cara nulis tes otomatis sendiri menggunakan `pytest` untuk menjamin kodinganmu bebas bug sebelum di-push ke GitHub.

---

## 1. Kenapa Programmer Menggunakan Test Otomatis?
Sebelum kenal testing, cara programmer ngecek kode adalah:
- Jalanin file -> ngetik manual di terminal -> lihat layar -> ulang 50 kali.
Ini sangat lambat dan melelahkan.

Dengan **Test Automation**:
Lu cukup ketik 1 perintah `pytest`, dan komputer akan menguji 100 fungsi dalam waktu 0.2 detik!

---

## 2. Aturan Emas Pytest
Pytest bekerja secara ajaib berdasarkan konvensi penamaan:
1. Nama file tes harus berawalan `test_` (contoh: `test_kasir.py`).
2. Nama fungsi tes harus berawalan `test_` (contoh: `def test_hitung_diskon():`).
3. Gunakan kata kunci `assert` untuk mengecek kebenaran nilai.

Contoh fungsi di `kasir.py`:
```python
def hitung_diskon(total):
    if total >= 100000:
        return total * 0.9
    return total
```

File tes `test_kasir.py`:
```python
from kasir import hitung_diskon

def test_diskon_seratus_ribu():
    assert hitung_diskon(100000) == 90000

def test_tanpa_diskon():
    assert hitung_diskon(50000) == 50000
```

---

## 3. Menjalankan Pytest di Terminal
Pastikan pytest sudah terinstall (`pip install pytest`), lalu ketik:
```bash
pytest
```
- Tanda titik hijau `.` = Lulus (PASS).
- Tanda merah `F` = Gagal (FAIL), pytest akan menunjukkan persis di baris mana ekspektasimu tidak sesuai.

---

## 4. Pola Uji AAA (Arrange - Act - Assert)
Setiap tes yang bagus mengikuti 3 langkah:
1. **Arrange**: Siapkan data uji (misal: input angka 5 dan 10).
2. **Act**: Panggil fungsimu dan tampung hasilnya.
3. **Assert**: Bandingkan hasilnya dengan nilai kebenaran.
