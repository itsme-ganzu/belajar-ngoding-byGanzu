def hitung_rata_rata(angka_list):
    if not angka_list or len(angka_list) == 0:
        return 0
    total = sum([int(x) for x in angka_list if str(x).strip()])
    return total / len(angka_list)

teks = input().strip()
if not teks:
    print("Rata-rata: 0")
else:
    daftar = [x.strip() for x in teks.split(",") if x.strip()]
    hasil = hitung_rata_rata(daftar)
    print(f"Rata-rata: {hasil}")
