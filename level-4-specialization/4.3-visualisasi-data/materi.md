# 4.3: Visualisasi Data (Matplotlib & Seaborn)

**Outcome:** lu mampu mengubah baris-baris data angka yang membosankan menjadi grafik visual yang bercerita kepada stakeholder bisnis.

---

## 1. Tiga Grafik Wajib Data Analyst

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

### A. Grafik Garis (Tren Waktu)
Cocok untuk melihat pertumbuhan omzet harian/bulanan:
```python
plt.figure(figsize=(10, 5))
plt.plot(df["tanggal"], df["omzet"], marker="o", color="blue")
plt.title("Tren Penjualan Toko Tahun 2026")
plt.xlabel("Bulan")
plt.ylabel("Omzet (Rupiah)")
plt.grid(True)
plt.savefig("tren_penjualan.png")
```

### B. Grafik Batang (Perbandingan Kategori)
Cocok untuk membandingkan performa antar cabang/kategori produk:
```python
sns.barplot(data=df, x="kategori", y="total_terjual", palette="viridis")
plt.title("Produk Terlaris")
plt.savefig("produk_terlaris.png")
```

### C. Histogram (Distribusi Data)
Melihat sebaran usia pelanggan atau nominal belanja (apakah mayoritas belanja kecil atau besar):
```python
sns.histplot(df["nominal_belanja"], bins=20, kde=True)
plt.title("Distribusi Nominal Belanja")
plt.savefig("distribusi_belanja.png")
```
