def analisis_nilai(daftar_angka):
    # Salah: rumus rata-rata salah (tidak membagi dengan len)
    return {
        "tertinggi": max(daftar_angka),
        "rata_rata": sum(daftar_angka)
    }

teks = input()
angka_list = [int(x.strip()) for x in teks.split(",") if x.strip()]
hasil = analisis_nilai(angka_list)
print(f"Tertinggi: {hasil['tertinggi']}")
print(f"Rata-rata: {hasil['rata_rata']}")
