# 1.3: Loop (Perulangan)

**Outcome:** lu bisa mengulang instruksi berkali-kali tanpa copy-paste kode, tahu kapan pakai `for` vs `while`, dan paham cara kerja akumulator.

## Kenapa butuh loop?
Bayangkan lu mau mencetak angka 1 sampai 5. Tanpa loop, lu harus nulis `print(1)` sampai 5 baris. Kalau disuruh mencetak sampai 1000? Copy-paste bakal bikin kode berantakan. Loop menyelesaikan masalah ini.

## 1. Perulangan `for` dan fungsi `range()`
Gunakan `for` jika lu **sudah tahu** berapa kali pengulangan dilakukan.

```python
for i in range(5):
    print(f"Putaran ke-{i}")
```
Output:
```
Putaran ke-0
Putaran ke-1
Putaran ke-2
Putaran ke-3
Putaran ke-4
```
> **Penting (Indeks mulai dari 0):** `range(5)` menghasilkan 5 angka: mulai dari `0` dan berhenti **sebelum** `5`.

### Menentukan batas awal dan akhir
Kalau mau mulai dari angka 1 sampai 5:
```python
for i in range(1, 6):
    print(i)
```
Artinya: mulai dari `1`, berhenti sebelum `6` (yaitu `5`).

## 2. Pola Akumulator (Menghitung Total)
Ini salah satu pola paling sering dipakai dalam koding: menjumlahkan nilai berulang kali.

```python
total = 0  # 1. Siapkan wadah di LUAR loop

for angka in [10, 20, 30]:
    total = total + angka  # 2. Tambahkan setiap putaran

print(f"Total akhir: {total}")
```
> **Jebakan:** Jangan menaruh `total = 0` di DALAM loop, karena wadah akan ter-reset jadi 0 lagi setiap kali putaran berjalan!

## 3. Perulangan `while`
Gunakan `while` jika pengulangan harus jalan terus **selama suatu kondisi bernilai True**, dan lu belum tahu pasti kapan akan berhenti (misal: menunggu tebakan user benar).

```python
angka = 1
while angka <= 3:
    print(angka)
    angka = angka + 1  # Wajib ada agar kondisi bisa jadi False!
```

> **Awas Infinite Loop:** Jika lupa baris `angka = angka + 1`, nilai `angka` akan selalu 1 (`1 <= 3` selalu `True`), dan program akan jalan selamanya sampai komputer ngelag.
> Kalau kejadian, tekan tombol **Ctrl + C** di terminal untuk menghentikan paksa.

## 4. Keluar Paksa: `break`
Kata kunci `break` dipakai buat keluar dari loop detik itu juga saat kondisi tertentu terpenuhi.

```python
while True:
    kata = input("Ketik 'stop' buat berhenti: ")
    if kata == "stop":
        break
print("Program selesai.")
```

## Latihan
Lihat `latihan/soal.md`.

## Checkpoint
Lihat `checkpoint.md`.
