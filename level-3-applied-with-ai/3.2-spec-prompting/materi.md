# 3.2: Technical Specification & Context Prompting

**Outcome:** lu bisa memberikan instruksi koding yang presisi ke AI sehingga menghasilkan kode yang bersih, minim bug, dan sesuai arsitektur proyekmu.

---

## 1. Rumus Prompting Software Engineer (Bukan Prompting Kasual)
Prompt orang awam:
> *"Tolong buatin gue aplikasi kasir pakai Python dong."*
Hasilnya: Kode 200 baris yang berantakan, tidak ada tes, dan tidak nyambung dengan proyekmu.

Prompt Software Engineer:
Gunakan rumus **R-C-I-E (Role, Context, Instructions, Constraints)**:

```text
[ROLE]
Bertindaklah sebagai Senior Python Engineer.

[CONTEXT]
Saya sedang membangun backend toko mini menggunakan SQLite dan Python 3.12. Struktur tabel: produk(id, nama, harga).

[INSTRUCTION]
Buatkan fungsi bernama `tambah_produk(nama: str, harga: int) -> bool` yang menyimpan data baru ke tabel produk.

[CONSTRAINTS]
1. Gunakan parameterized query (?) untuk mencegah SQL Injection.
2. Tangani potensi error jika database terkunci (gunakan try-except).
3. Jangan gunakan library eksternal, gunakan sqlite3 bawaan.
4. Tuliskan 2 contoh unit test menggunakan pytest untuk fungsi tersebut.
```

Dengan spesifikasi seketat ini, AI tidak punya celah untuk berhalusinasi atau memberikan kode asal-asalan.
