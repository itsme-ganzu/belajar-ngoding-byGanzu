# 4.2: Data Wrangling & Cleaning dengan Pandas

**Outcome:** lu bisa memuat dataset jutaan baris ke dalam memori, membersihkan data yang rusak/kosong, dan melakukan transformasi data secara cepat.

---

## 1. Memuat Data ke DataFrame
DataFrame adalah struktur tabel 2 dimensi super cepat di Python:
```python
import pandas as pd

# Membaca data dari CSV atau Excel
df = pd.read_csv("penjualan.csv")

# Melihat 5 baris teratas dan info kolom
print(df.head())
print(df.info())
```

---

## 2. Membersihkan Data Kotor (*Data Cleaning*)

### A. Menangani Nilai Kosong (*Missing Values / NaN*)
```python
# Cek berapa banyak kolom yang bolong
print(df.isnull().sum())

# Opsi 1: Buang baris yang kosong
df_bersih = df.dropna()

# Opsi 2: Isi nilai kosong dengan nilai rata-rata
df["umur"] = df["umur"].fillna(df["umur"].median())
```

### B. Transformasi & Kolom Baru
```python
# Menghitung margin keuntungan
df["keuntungan"] = df["harga_jual"] - df["harga_modal"]

# Filter transaksi besar saja
transaksi_vip = df[df["total_bayar"] >= 500000]
```
