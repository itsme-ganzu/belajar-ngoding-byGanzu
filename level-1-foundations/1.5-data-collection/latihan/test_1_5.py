import os
import subprocess
import sys
import unittest
from pathlib import Path

DIR = Path(os.environ.get("JAWABAN_DIR", Path(__file__).parent))


def jalankan(nama_file, masukan):
    path = DIR / nama_file
    if not path.exists():
        raise AssertionError(f"File {nama_file} belum ada di folder {DIR}")
    hasil = subprocess.run([sys.executable, str(path)], input=masukan,
                           capture_output=True, text=True, timeout=10)
    if hasil.returncode != 0:
        raise AssertionError(f"Program error:\n{hasil.stderr}")
    return hasil.stdout


class Test15(unittest.TestCase):
    # Tes Soal 1: Analisis Nilai
    def test_soal1_program_tiga_angka(self):
        output = jalankan("jawaban_1.py", "70,80,90\n")
        self.assertIn("Tertinggi: 90", output)
        self.assertIn("Rata-rata: 80", output)

    def test_soal1_program_dengan_spasi(self):
        output = jalankan("jawaban_1.py", "50,  100,  75\n")
        self.assertIn("Tertinggi: 100", output)
        self.assertIn("Rata-rata: 75", output)

    def test_soal1_program_satu_angka(self):
        output = jalankan("jawaban_1.py", "85\n")
        self.assertIn("Tertinggi: 85", output)
        self.assertIn("Rata-rata: 85", output)

    # Tes Soal 2: Kasir Kantin Mini
    def test_soal2_kopi_standar(self):
        output = jalankan("jawaban_2.py", "kopi\n")
        self.assertIn("Harga: 15000", output)

    def test_soal2_kopi_uppercase_dan_spasi(self):
        output = jalankan("jawaban_2.py", "   KOPI   \n")
        self.assertIn("Harga: 15000", output)

    def test_soal2_teh(self):
        output = jalankan("jawaban_2.py", "Teh\n")
        self.assertIn("Harga: 5000", output)

    def test_soal2_tidak_ada(self):
        output = jalankan("jawaban_2.py", "Pizza\n")
        self.assertIn("Menu tidak ditemukan", output)


if __name__ == "__main__":
    unittest.main()
