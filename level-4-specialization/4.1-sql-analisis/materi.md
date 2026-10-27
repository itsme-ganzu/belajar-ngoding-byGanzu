# 4.1: SQL Lanjutan untuk Analisis Data

**Outcome:** lu mampu menarik data spesifik, melakukan agregasi bisnis, dan menggabungkan banyak tabel relasional menggunakan SQL murni.

---

## 1. Agregasi Bisnis (`GROUP BY` & `HAVING`)
Analyst jarang melihat baris per baris. Analyst melihat ringkasan: total omzet per bulan, rata-rata belanja per kota, atau jumlah user aktif.

Contoh: Menghitung total omzet per kategori barang:
```sql
SELECT kategori, COUNT(id) AS jumlah_terjual, SUM(harga) AS total_omzet
FROM transaksi
GROUP BY kategori
HAVING total_omzet > 1000000;
```
> **Perhatian:** `WHERE` menyaring baris sebelum dihitung, sedangkan `HAVING` menyaring hasil setelah di-agregasi (`GROUP BY`).

---

## 2. Menggabungkan Banyak Tabel (`JOIN`)
Di database nyata, data produk dan data pembeli disimpan di tabel terpisah agar tidak redundan.

### `INNER JOIN` (Hanya yang Cocok di Kedua Tabel)
```sql
SELECT pesanan.id, pelanggan.nama, pesanan.total_bayar
FROM pesanan
INNER JOIN pelanggan ON pesanan.pelanggan_id = pelanggan.id;
```

### `LEFT JOIN` (Semua Data Kiri Tetap Muncul)
Berguna untuk mencari pelanggan yang belum pernah belanja sama sekali:
```sql
SELECT pelanggan.nama, pesanan.id
FROM pelanggan
LEFT JOIN pesanan ON pelanggan.id = pesanan.pelanggan_id
WHERE pesanan.id IS NULL;
```
