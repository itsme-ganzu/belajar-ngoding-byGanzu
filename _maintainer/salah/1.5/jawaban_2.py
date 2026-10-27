MENU = {
    "kopi": 15000,
    "teh": 5000,
    "roti": 10000
}

# Salah: tidak pakai .strip() atau .lower(), sehingga gagal di input huruf besar / berspasi
pesanan = input()

if pesanan in MENU:
    print(f"Harga: {MENU[pesanan]}")
else:
    print("Menu tidak ditemukan")
