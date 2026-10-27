total = int(input())
if total >= 100000:
    bayar = total - int(total * 0.1)
else:
    bayar = total
print(f"Bayar: {bayar}")
