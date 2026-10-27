# 3.3: Code Review, Audit Keamanan, & Red Teaming AI

**Outcome:** lu mampu mengaudit dan mereview kode buatan AI, menemukan bug tersembunyi, serta mencegah kebocoran data rahasia (*secret leakage*).

---

## 1. Tiga Bahaya Keamanan Utama pada Kode Buatan AI

### A. Kebocoran API Key & Password (Hardcoded Secrets)
AI sering menaruh API key atau password langsung di dalam file kodingan:
```python
API_KEY = "sk-1234567890abcdef"  # BAHAYA BESAR! Jangan pernah di-commit ke Git!
```
**Solusi Standar Industri:**
Selalu gunakan file `.env` dan baca melalui environment variable (`os.environ.get("API_KEY")`), serta masukkan file `.env` ke dalam `.gitignore`.

### B. Kerentanan Injeksi (SQL & Command Injection)
AI kerap menggabungkan string mentah untuk query database atau menjalankan shell command:
```python
# BAHAYA:
query = f"SELECT * FROM users WHERE username = '{input_user}'"
```
Pastikan lu selalu mereview dan mengubahnya ke *parameterized query*.

### C. Ketergantungan Dependensi Beracun (Hallucinated Packages)
Peneliti keamanan siber menemukan kasus di mana hacker sengaja membuat library palsu di PyPI dengan nama-nama fungsi yang sering dihalusinasikan oleh ChatGPT. Jika lu langsung `pip install` library rekomendasi AI tanpa cek dokumentasi resmi, laptopmu bisa terkena malware!

---

## 2. Checklist Review Kode AI
Sebelum lu menyetujui (*merge*) kode dari AI:
- [ ] Apakah ada baris kode yang lu nggak paham cara kerjanya?
- [ ] Apakah ada password/token rahasia yang tertulis mentah?
- [ ] Apakah penanganan error (*edge cases*: angka minus, input kosong, koneksi putus) sudah aman?
- [ ] Apakah kode tersebut lulus tes unit mandiri?
