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


class Test12(unittest.TestCase):
    # Tes Soal 1: Suhu
    def test_suhu_beku_nol(self):
        self.assertIn("Beku", jalankan("jawaban_1.py", "0\n"))

    def test_suhu_beku_minus(self):
        self.assertIn("Beku", jalankan("jawaban_1.py", "-5\n"))

    def test_suhu_cair_tengah(self):
        self.assertIn("Cair", jalankan("jawaban_1.py", "25\n"))

    def test_suhu_cair_batas(self):
        self.assertIn("Cair", jalankan("jawaban_1.py", "99\n"))

    def test_suhu_uap_seratus(self):
        self.assertIn("Uap", jalankan("jawaban_1.py", "100\n"))

    def test_suhu_uap_lebih(self):
        self.assertIn("Uap", jalankan("jawaban_1.py", "150\n"))

    # Tes Soal 2: Diskon
    def test_diskon_dapat(self):
        self.assertIn("Bayar: 135000", jalankan("jawaban_2.py", "150000\n"))

    def test_diskon_pas_seratus_ribu(self):
        self.assertIn("Bayar: 90000", jalankan("jawaban_2.py", "100000\n"))

    def test_diskon_tidak_dapat(self):
        self.assertIn("Bayar: 50000", jalankan("jawaban_2.py", "50000\n"))

    def test_diskon_hampir_seratus_ribu(self):
        self.assertIn("Bayar: 99000", jalankan("jawaban_2.py", "99000\n"))


if __name__ == "__main__":
    unittest.main()
