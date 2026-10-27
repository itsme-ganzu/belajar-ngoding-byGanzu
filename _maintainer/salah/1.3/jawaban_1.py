n = int(input())
total = 0
# Salah: off-by-one, range(1, n) tidak menyertakan n
for i in range(1, n):
    total = total + i
print(f"Jumlah: {total}")
