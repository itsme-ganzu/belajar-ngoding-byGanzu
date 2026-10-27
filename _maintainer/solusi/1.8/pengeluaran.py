import os

FILE_NAME = "data_pengeluaran.csv"

while True:
    print("=== PENCATAT PENGELUARAN ===")
    print("1. Tambah Transaksi")
    print("2. Lihat Total")
    print("3. Keluar")
    pilihan = input().strip()

    if pilihan == "1":
        nama = input().strip()
        nominal = input().strip()
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{nama},{nominal}\n")
        print("Berhasil dicatat!")
    elif pilihan == "2":
        total = 0
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split(",")
                        total += int(parts[1])
        print(f"Total pengeluaran: {total}")
    elif pilihan == "3":
        print("Sampai jumpa!")
        break
