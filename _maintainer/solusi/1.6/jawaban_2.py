KATALOG = {
    "python": 50000,
    "javascript": 60000,
    "sql": 45000
}

judul = input().strip().lower()

if judul in KATALOG:
    print(f"Harga: {KATALOG[judul]}")
else:
    print("Buku tidak tersedia")
