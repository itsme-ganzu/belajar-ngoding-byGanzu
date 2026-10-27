# 2.4: Version Control dengan Git & GitHub

**Outcome:** lu bisa mencatat riwayat perubahan kode, tidak takut kodingan rusak karena bisa kembali ke versi sebelumnya (*undo*), dan bisa memamerkan kodemu di GitHub.

---

## 1. Apa itu Git vs GitHub?
- **Git**: Software pelacak riwayat file di laptopmu (seperti tombol *Time Machine* atau *Save Point* di game).
- **GitHub**: Website awan (cloud) untuk menyimpan salinan repositori Git lu agar bisa dilihat orang lain, kolaborasi, dan jadi portofolio.

---

## 2. Siklus Kerja Harian Git (The Holy Trinity)

Setiap kali lu selesai menambah fitur atau memperbaiki bug:

1. **Cek status:**
   ```bash
   git status
   ```
2. **Kumpulkan perubahan ke keranjang (*Stage*):**
   ```bash
   git add .
   ```
3. **Simpan permanen dengan pesan catatan (*Commit*):**
   ```bash
   git commit -m "feat: tambah fungsi hitung diskon di kasir"
   ```
4. **Kirim ke GitHub (*Push*):**
   ```bash
   git push origin main
   ```

---

## 3. Format Pesan Commit yang Profesional
Jangan tulis commit ngawur seperti `"update"`, `"fix"`, atau `"bismillah jalan"`.
Gunakan pola standar industri:
- `feat: ...` (fitur baru)
- `fix: ...` (memperbaiki bug)
- `docs: ...` (mengubah dokumentasi README)
- `refactor: ...` (merapikan struktur kode tanpa mengubah fungsi)
