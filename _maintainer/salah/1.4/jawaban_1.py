# Salah: fungsi memakai print, bukan return
def celcius_ke_fahrenheit(c):
    print(f"Fahrenheit: {(c * 9/5) + 32}")

suhu_c = float(input())
celcius_ke_fahrenheit(suhu_c)
