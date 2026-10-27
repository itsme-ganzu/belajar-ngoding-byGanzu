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


class Test11(unittest.TestCase):
    def test_soal1_budi(self):
        self.assertIn("Halo, Budi! Tahun depan umur kamu 21 tahun.",
                      jalankan("jawaban_1.py", "Budi\n20\n"))

    def test_soal1_dihitung_bukan_ditulis_manual(self):
        self.assertIn("Halo, Sari! Tahun depan umur kamu 31 tahun.",
                      jalankan("jawaban_1.py", "Sari\n30\n"))

    def test_soal2_total(self):
        self.assertIn("Total: 45000", jalankan("jawaban_2.py", "15000\n3\n"))

    def test_soal2_angka_lain(self):
        self.assertIn("Total: 7000", jalankan("jawaban_2.py", "3500\n2\n"))


if __name__ == "__main__":
    unittest.main()
