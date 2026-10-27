def tulis_catatan(nama_file, daftar_teks):
    with open(nama_file, "w", encoding="utf-8") as f:
        for t in daftar_teks:
            f.write(f"{t}\n")

teks = input().strip()
items = [x.strip() for x in teks.split(",") if x.strip()]
tulis_catatan("buah.txt", items)
print("Berhasil ditulis ke buah.txt")
