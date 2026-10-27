def rekap_pengeluaran(nama_file_csv):
    total = 0
    with open(nama_file_csv, "r", encoding="utf-8") as f:
        # Salah: lupa melewari header (f.readline()) sehingga mencoba int("biaya") yang memicu crash ValueError
        for baris in f:
            baris = baris.strip()
            if baris:
                parts = baris.split(",")
                total += int(parts[1])
    return total

nama_csv = input().strip()
hasil = rekap_pengeluaran(nama_csv)
print(f"Total biaya: {hasil}")
