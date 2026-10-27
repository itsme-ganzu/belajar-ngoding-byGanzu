KATALOG = {
    "python": 50000,
    "javascript": 60000,
    "sql": 45000
}

judul = input().strip().lower()

# Salah: langsung panggil dict tanpa pengecekan -> memicu KeyError saat buku tidak ada
print(f"Harga: {KATALOG[judul]}")
