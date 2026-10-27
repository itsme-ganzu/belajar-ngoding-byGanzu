# Salah: tidak menyimpan data ke CSV dan format total salah
while True:
    pilihan = input().strip()
    if pilihan == "1":
        nama = input()
        nominal = input()
        print("Berhasil dicatat!")
    elif pilihan == "2":
        print("Total pengeluaran: 0")
    elif pilihan == "3":
        print("Sampai jumpa!")
        break
