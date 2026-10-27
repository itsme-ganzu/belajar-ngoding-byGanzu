# 3.1: Anatomi dan Batasan LLM dalam Koding

**Outcome:** lu paham bagaimana AI (LLM) bekerja di balik layar, tahu kapan AI bisa dipercaya, dan tahu titik-titik di mana AI paling sering menipumu (halusinasi kode).

---

## 1. LLM Bukan Jin Ajaib, Tapi "Prediktor Kata"
AI seperti ChatGPT atau Claude tidak "berpikir" atau "menjalankan kode" di dalam kepalanya.
AI bekerja dengan memprediksi token/kata berikutnya yang paling mungkin muncul secara statistik berdasarkan miliaran baris kode yang pernah dia baca di internet.

---

## 2. Tiga Titik Kegagalan Paling Sering (AI Blindspots)

### A. Halusinasi Library & Fungsi Palsu
Jika lu meminta AI menyelesaikan tugas yang spesifik, AI sering kali mengarang nama fungsi atau parameter yang sebenarnya tidak pernah ada di library aslinya.
* *Contoh:* AI merekomendasikan `import pandas as pd; pd.read_magical_data()` padahal method itu khayalan.

### B. Masalah "Pengetahuan Kedaluwarsa" (*Stale APIs*)
Dokumentasi library software selalu berubah tiap tahun. AI sering memberikan kode yang sudah *deprecated* (usang) atau tidak lagi jalan di versi library terbaru.

### C. Bias "Yes-Man" (Tunduk pada Premis Salah)
Jika lu memberikan pertanyaan yang salah: *"Kenapa fungsi X gue crash saat dikasih angka negatif?"*, AI sering kali mengarang alasan rumit dan memvalidasi logikamu, padahal kesalahan aslinya ada di salah ketik nama variabel di baris lain.

---

## 3. Aturan Emas: "Zero-Trust AI"
Jangan pernah memasukkan kode buatan AI ke dalam proyekmu sebelum:
1. Lu membaca dan bisa menjelaskan setiap barisnya dengan kata-katamu sendiri.
2. Kode tersebut sudah lolos tes otomatis (`pytest`) yang lu buat sendiri.
