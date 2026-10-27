MENU = {
    "kopi": 15000,
    "teh": 5000,
    "roti": 10000
}

pesanan = input().strip().lower()

if pesanan in MENU:
    print(f"Harga: {MENU[pesanan]}")
else:
    print("Menu tidak ditemukan")
