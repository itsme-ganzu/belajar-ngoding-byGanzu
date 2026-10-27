# 🚀 PANDUAN MULAI: Dari Nol Sampai Jalan (Baca Ini Dulu!)

Halo! Selamat datang di repo **Belajar Ngoding dari Nol**.

---

## ⚠️ KONTRAK BELAJAR (Penting Dibaca!)

Biar ekspektasi lu dan Ganzu sama-sama enak:

1. **Repo ini BUKAN kursus/les privat manusia.** 
   Ganzu tidak membuka layanan tanya-jawab koding personal. Lu adalah kapten dari perjalanan belajarmu sendiri.
2. **AI adalah Guru Lu, Lu adalah Muridnya, Repo ini adalah Silabusnya.**
   Tutor pribadi lu adalah **LLM yang biasa lu pakai** (ChatGPT, Claude, Gemini, dll). Di repo ini kami sudah mendesain sistem prompt khusus (`TUTOR.md`) yang memaksa AI menjadi guru yang sabar dan membimbing logika, bukan sekadar mesin contekan.
3. **Paham atau tidaknya lu 100% bergantung pada keaktifan lu berdialog dengan AI lu.**
   Kalau penjelasan AI terasa kaku atau terlalu rumit, jangan menyerah! Paksa AI-mu: *"Jelasin lagi dong, tapi pakai analogi tukang bakso biar gue paham!"*.
4. **Hakim kebenaran kodemu adalah Tes Otomatis.**
   Jangan percaya omongan manis AI. Percayalah pada tes otomatis (`python test_1_x.py`). Kalau terminal bilang **OK**, berarti kodemu benar. Kalau **FAIL**, ajak AI-mu membedah kesalahannya.

---

## Peta Kilat: Apa Saja yang Ada di Folder Ini?

- 📄 `BACA-INI-DULU.md` : Panduan orientasi awal (yang sedang lu baca sekarang).
- 📄 `TUTOR.md` : "Otak" sistem tutor AI. Wajib ditempel ke chat AI lu.
- 📄 `PATHWAY.md` : Peta perjalanan dari Level 1 sampai Level 5 beserta gerbang kelulusan.
- 📁 `level-1-foundations/` : Tempat belajar lu sekarang (fondasi Python dasar 1.0 s/d 1.8 + Modul Jembatan).
- 📁 `level-2` s/d `level-5` : Level lanjutan (proyek nyata, database, engineering bareng AI, data analyst, deploy).
- 📁 `_maintainer/` : Dapur penguji otomatis repo. **Abaikan folder ini.**

---

## Langkah 1: Ambil File Repo Ini ke Laptop Lu

Pilih salah satu cara yang paling nyaman:

### Pilihan A: Cara Paling Gampang (Tanpa Git - 1 Menit)
1. Di halaman utama GitHub repo ini, klik tombol hijau **Code** (di kanan atas).
2. Klik **Download ZIP**.
3. Buka file hasil unduhan di laptop lu, lalu **Extract / Unzip** ke folder yang mudah dicari (misal: `Documents` atau `Desktop`).
4. Buka folder hasil ekstrak tersebut.

### Pilihan B: Mau Sambil Belajar Git? (Keren!)
Buka Terminal/PowerShell, lalu ketik:
```bash
git clone https://github.com/itsme-ganzu/belajar-ngoding-byGanzu.git
cd belajar-ngoding-byGanzu
```

---

## Langkah 2: Aktifkan "Tutor AI" Lu (2 Menit)

Tutor AI ini jalan di platform AI apa pun (ChatGPT, Claude, atau Gemini gratisan).

### Cara Praktis (Buka Chat Baru):
1. Buka AI favorit lu di browser ([chatgpt.com](https://chatgpt.com), [claude.ai](https://claude.ai), atau [gemini.google.com](https://gemini.google.com)).
2. Mulai **Chat Baru** (*New Chat*).
3. Salin (**Copy**) seluruh teks file `TUTOR.md`, lalu **Paste** ke kolom chat AI dan kirim.
4. Salin (**Copy**) seluruh teks file `PATHWAY.md`, lalu **Paste** ke chat yang sama dan kirim.
5. Ketik kalimat sakti ini:
   > *"Halo tutor! Gue mau mulai belajar ngoding dari nol. Tolong arahkan langkah pertama gue sesuai modul 1.0!"*

*(Tips Pro: Kalau lu pakai Claude Project, ChatGPT Custom Instructions, atau Cursor, lu bisa upload file `TUTOR.md` langsung agar aktif permanen).*

---

## Langkah 3: Ritual Belajar Tiap Modul (The Game Loop)

Setiap modul di Level 1 (misal `1.0-setup`, `1.1-variabel`, dst) punya ritme belajar yang sama:

1. **Pelajari Konsep**:
   - Buka file `materi.md` di folder modul tersebut, copy dan tempel ke AI tutor lu.
   - Baca penjelasan AI, diskusikan konsepnya sampai lu benar-benar "ngeh".
2. **Bikin File Jawaban**:
   - Masuk ke subfolder `latihan/`, baca soal di `soal.md`.
   - Bikin file kodinganmu (misal `jawaban_1.py`) di dalam folder `latihan/`.
   - ⚠️ **Awas Jebakan Windows:** Kalau pakai Notepad, pastikan saat Save As ubah tipe file menjadi *All Files (*.*)* agar namamu tidak berubah jadi `jawaban_1.py.txt`. Sangat disarankan menginstal editor khusus seperti **VS Code**.
3. **Uji Kode Lu Secara Mandiri (Tes Otomatis)**:
   - 💡 **Trik Buka Terminal Cepat di Windows:**
     Buka folder `latihan` di File Explorer -> klik kolom alamat folder di atas (address bar) -> ketik `cmd` lalu tekan Enter. Jendela terminal hitam akan langsung terbuka tepat di folder tersebut!
   - Jalankan tes otomatis:
     ```bash
     python test_1_x.py
     ```
     *(Ganti `1_x` sesuai modul, misal `python test_1_0.py` atau `python test_1_1.py`)*
   - Jika muncul **OK**, selamat! Logika kodemu 100% benar.
   - Jika muncul teks merah **FAIL**, salin pesan error tersebut, tempel ke AI tutor lu, dan minta petunjuk: *"Tutor, tes gue gagal di bagian ini, maksud errornya apa ya?"*.
4. **Gerbang Checkpoint**:
   - Buka `checkpoint.md`, jawab pertanyaan tebak logika di sana langsung ke AI tutor lu dengan kata-katamu sendiri.
   - Jika tutor mengonfirmasi pemahamanmu sudah kokoh, lu resmi berhak lanjut ke modul berikutnya!

---

## 💡 Mindset Programmer yang Harus Lu Tanamkan

- **Error warna merah itu biasa:** Jangan panik saat terminal mengeluarkan teks merah panjang. Itu bukan tanda komputer marah atau lu bodoh, tapi komputer cuma ngasih petunjuk baris mana yang bikin dia bingung.
- **Jangan buru-buru:** Mengerti 1 konsep dengan mendalam jauh lebih berharga daripada ngebut 5 modul tapi begitu disuruh ngetik sendiri malah bengong.
- **Lu yang pegang kendali:** Manfaatkan AI semaksimal mungkin untuk membedah rasa penasaranmu!

👉 **Sekarang, silakan mulai dari [Langkah 1](#langkah-1-ambil-file-repo-ini-ke-laptop-lu) dan sapa Tutor AI lu!**
