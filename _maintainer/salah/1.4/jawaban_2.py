# Salah logika: tidak memperhitungkan 2 jam flat (langsung kali 2000 per jam)
def hitung_parkir(jam):
    return 5000 + (jam * 2000)

lama = int(input())
total = hitung_parkir(lama)
print(f"Biaya: {total}")
