# 5.2: Portofolio GitHub & Etika Kontribusi Open Source

**Outcome:** profil GitHub-mu terlihat profesional di mata recruiter / tech lead, dan kamu tahu cara berkontribusi ke repositori orang lain via Pull Request (PR).

---

## 1. Anatomi README Portofolio yang Memikat Recruiter
Recruiter tidak punya waktu membaca 1.000 baris kodemu. Mereka membaca `README.md`.

Setiap proyek portofolio wajib memiliki:
1. **Satu Kalimat Penjelas (Elevator Pitch):** Masalah apa yang diselesaikan aplikasi ini?
2. **Screenshot / GIF Demo:** Bukti visual bahwa aplikasimu benar-benar hidup.
3. **Teknologi yang Dipakai:** (Contoh: Python 3.12, SQLite, Pandas, Pytest).
4. **Petunjuk Menjalankan Cepat (*Quickstart*):** Cuma 3 langkah: `git clone`, `pip install`, `python main.py`.

---

## 2. Cara Berkontribusi ke Open Source (Langkah Pull Request)

1. **Fork Repositori**: Klik tombol *Fork* di repo target untuk membuat salinan di akunmu.
2. **Clone ke Laptop**: `git clone <link-repo-fork-lu>`.
3. **Bikin Branch Baru**:
   ```bash
   git checkout -b fix-typo-dokumentasi
   ```
4. **Lakukan Perubahan & Commit**: Pastikan semua tes bawaan repo tetap lulus hijau!
5. **Push ke Fork**:
   ```bash
   git push origin fix-typo-dokumentasi
   ```
6. **Buka Pull Request (PR)**: Masuk ke halaman GitHub repo asli, klik tombol hijau **"Compare & Pull Request"**, tulis deskripsi perubahanmu dengan sopan.
