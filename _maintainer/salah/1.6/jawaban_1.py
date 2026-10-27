# Salah: tidak mengecek list kosong sehingga memicu ZeroDivisionError saat input kosong
def hitung_rata_rata(angka_list):
    total = sum([int(x) for x in angka_list])
    return total / len(angka_list)

teks = input().strip()
daftar = [x.strip() for x in teks.split(",") if x.strip()]
hasil = hitung_rata_rata(daftar)
print(f"Rata-rata: {hasil}")
