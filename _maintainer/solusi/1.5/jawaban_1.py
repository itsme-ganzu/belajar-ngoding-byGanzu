def analisis_nilai(daftar_angka):
    tertinggi = max(daftar_angka)
    rata_rata = sum(daftar_angka) / len(daftar_angka)
    return {
        "tertinggi": tertinggi,
        "rata_rata": rata_rata
    }

teks = input()
angka_list = [int(x.strip()) for x in teks.split(",") if x.strip()]
hasil = analisis_nilai(angka_list)
print(f"Tertinggi: {hasil['tertinggi']}")
print(f"Rata-rata: {hasil['rata_rata']}")
