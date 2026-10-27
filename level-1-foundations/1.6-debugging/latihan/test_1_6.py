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
        raise AssertionError(f"Program crash/error:\n{hasil.stderr}")
    return hasil.stdout


class Test16(unittest.TestCase):
    # Tes Soal 1: ZeroDivisionError & TypeError
    def test_soal1_normal(self):
        output = jalankan("jawaban_1.py", "10,20,30\n")
        self.assertIn("Rata-rata: 20", output)

    def test_soal1_input_kosong(self):
        # Memastikan tidak crash ZeroDivisionError saat input kosong
        output = jalankan("jawaban_1.py", "\n")
        self.assertIn("Rata-rata: 0", output)

    # Tes Soal 2: Pencegahan KeyError
    def test_soal2_ada(self):
        output = jalankan("jawaban_2.py", "python\n")
        self.assertIn("Harga: 50000", output)

    def test_soal2_ada_kapital(self):
        output = jalankan("jawaban_2.py", "  PYTHON  \n")
        self.assertIn("Harga: 50000", output)

    def test_soal2_tidak_ada_bebas_crash(self):
        # Memastikan tidak crash KeyError saat buku tidak ada
        output = jalankan("jawaban_2.py", "golang\n")
        self.assertIn("Buku tidak tersedia", output)


if __name__ == "__main__":
    unittest.main()
