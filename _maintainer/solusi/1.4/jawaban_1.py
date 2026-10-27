def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

suhu_c = float(input())
hasil_f = celcius_ke_fahrenheit(suhu_c)
print(f"Fahrenheit: {hasil_f}")
