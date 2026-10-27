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


class Test13(unittest.TestCase):
    # Tes Soal 1: Jumlah akumulasi 1 s/d N
    def test_soal1_satu(self):
        self.assertIn("Jumlah: 1", jalankan("jawaban_1.py", "1\n"))

    def test_soal1_lima(self):
        self.assertIn("Jumlah: 15", jalankan("jawaban_1.py", "5\n"))

    def test_soal1_sepuluh(self):
        self.assertIn("Jumlah: 55", jalankan("jawaban_1.py", "10\n"))

    # Tes Soal 2: Tebak PIN
    def test_soal2_langsung_benar(self):
        output = jalankan("jawaban_2.py", "1234\n")
        self.assertIn("Akses diterima!", output)
        self.assertNotIn("PIN salah, coba lagi.", output)

    def test_soal2_salah_sekali(self):
        output = jalankan("jawaban_2.py", "0000\n1234\n")
        self.assertEqual(output.count("PIN salah, coba lagi."), 1)
        self.assertIn("Akses diterima!", output)

    def test_soal2_salah_berkali_kali(self):
        output = jalankan("jawaban_2.py", "9999\n1111\n4321\n1234\n")
        self.assertEqual(output.count("PIN salah, coba lagi."), 3)
        self.assertIn("Akses diterima!", output)


if __name__ == "__main__":
    unittest.main()
