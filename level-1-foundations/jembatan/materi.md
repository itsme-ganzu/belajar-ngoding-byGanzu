# Modul Jembatan: Dari Paham Syntax ke Bikin Proyek

**Outcome:** lu keluar dari kutukan *"Tutorial Hell"* (tahu syntax tapi bengong pas buka layar kosong), tahu cara memecah ide besar jadi tugas-tugas kecil, dan tahu cara keluar saat mentok.

---

## 1. Masalah Terbesar Pemula: "Blank Canvas Paralysis"
Banyak orang selesai belajar loop, if/else, dan list, lalu bilang:
> *"Oke, gue paham syntax-nya... terus sekarang gue harus ngapain? Mau bikin apa dan mulai dari mana?"*

Masalahnya bukan lu kurang jago ngoding. Masalahnya: **lu mencoba memikirkan seluruh proyek sekaligus dalam satu detik di kepala lu.**

Komputer itu bodoh. Komputer tidak bisa mengerjakan *"Bikinin gue aplikasi toko online"*. Komputer hanya bisa menjalankan instruksi mikro: simpan angka, bandingkan nilai, ulangi proses.

---

## 2. Rumus 4 Langkah: Dekonstruksi Masalah (Problem Breakdown)

Kapan pun lu punya ide aplikasi, lakukan 4 langkah ini di atas kertas sebelum mengetik satu baris kode pun di VS Code:

### Langkah 1: Tentukan MVP (Minimum Viable Product) yang Paling Kerdil
Buang semua fitur khayalan (jangan pikirkan login Google, jangan pikirkan tampilan animasi warna-warni).
Tanya diri lu: **"Apa 1 fungsi inti yang kalau fungsi ini jalan, aplikasinya sudah ada gunanya?"**
* *Contoh Ide:* Aplikasi Pengingat Minum Obat.
* *MVP:* Program terminal yang cuma nerima nama obat dan jam, lalu nyimpen ke file teks.

### Langkah 2: Tulis Pseudocode (Bahasa Manusia Berurutan)
Tulis alur logikanya dalam bahasa Indonesia biasa, baris demi baris:
```text
1. Mulai program
2. Tampilkan menu: 1. Catat, 2. Lihat, 3. Keluar
3. Minta user milih nomor
4. Jika pilih 1:
   - Tanya nama obat
   - Simpan ke catatan.txt
5. Jika pilih 2:
   - Baca catatan.txt dan tampilkan
6. Jika pilih 3:
   - Berhenti
```

### Langkah 3: Petakan Pseudocode ke Syntax yang Lu Tahu
Sekarang terjemahkan baris bahasa Indonesia tadi ke alat Python yang cocok:
- "Tampilkan menu berulang-ulang" -> pakai `while True:`
- "Minta user milih nomor" -> pakai `input()`
- "Jika pilih 1..." -> pakai `if pilihan == "1":`
- "Simpan ke file" -> pakai `with open("catatan.txt", "a")`

### Langkah 4: Koding dari Bagian yang Paling Gampang
Jangan mulai dari fitur yang paling rumit! Mulai dari yang paling lu bisa (misal: bikin menu print-nya dulu). Begitu menu muncul, lu dapat suntikan dopamin dan rasa percaya diri untuk lanjut ke langkah berikutnya.

---

## 3. Protokol Keluar Saat Mentok (Getting Unstuck)
Semua programmer pasti mentok (*stuck*). Bedanya programmer pemula dengan senior adalah cara mereka merespons rasa mentok:

1. **Jelaskan Masalah ke Bebek Karet (*Rubber Duck Debugging*):**
   Ambil benda di meja lu (atau buka chat AI tutor lu), lalu ceritakan baris per baris: *"Gue pengen variabel ini nilainya nambah, tapi pas di print kok malah nol..."*. Sering kali saat lu mengucapkan alurnya dengan kata-kata sendiri, otak lu langsung nemu solusinya.
2. **Isolasi Masalah ke File Baru:**
   Jangan utak-atik program besarmu yang ada 100 baris. Bikin file kecil `tes_logika.py` berisi 5 baris khusus untuk menguji potongan logika yang bikin lu pusing sampai jalan.
3. **Manfaatkan AI Sebagai Teman Diskusi Logika, Bukan Mesin Contekan:**
   Tanyakan: *"Gue mau ngitung kembalian parkir dengan aturan A dan B, ini pseudocode gue. Menurut lu ada skenario yang kelewat nggak?"*

---

## Checkpoint Modul Jembatan
Buka `checkpoint.md` dan jawab langsung ke AI tutor lu!
