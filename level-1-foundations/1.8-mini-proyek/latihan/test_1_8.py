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
    hasil = subprocess.run([sys.executable, nama_file], input=masukan,
                           capture_output=True, text=True, timeout=10, cwd=str(DIR))
    if hasil.returncode != 0:
        raise AssertionError(f"Program error:\n{hasil.stderr}")
    return hasil.stdout


class Test18(unittest.TestCase):
    def setUp(self):
        csv_file = DIR / "data_pengeluaran.csv"
        if csv_file.exists():
            csv_file.unlink()

    def tearDown(self):
        csv_file = DIR / "data_pengeluaran.csv"
        if csv_file.exists():
            csv_file.unlink()

    def test_alur_lengkap(self):
        # 1: tambah kopi 15000
        # 1: tambah roti 10000
        # 2: cek total (harus 25000)
        # 3: keluar
        masukan = "1\nkopi\n15000\n1\nroti\n10000\n2\n3\n"
        output = jalankan("pengeluaran.py", masukan)

        self.assertIn("Berhasil dicatat!", output)
        self.assertIn("Total pengeluaran: 25000", output)
        self.assertIn("Sampai jumpa!", output)

        csv_file = DIR / "data_pengeluaran.csv"
        self.assertTrue(csv_file.exists(), "File data_pengeluaran.csv harus terbentuk")
        with open(csv_file, "r", encoding="utf-8") as f:
            konten = f.read()
        self.assertIn("kopi,15000", konten)
        self.assertIn("roti,10000", konten)


if __name__ == "__main__":
    unittest.main()
