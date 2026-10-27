def hitung_parkir(jam):
    if jam <= 2:
        return 5000
    else:
        return 5000 + ((jam - 2) * 2000)

lama = int(input())
total = hitung_parkir(lama)
print(f"Biaya: {total}")
