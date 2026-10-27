import importlib.util
import os
import subprocess
import sys
import unittest
from pathlib import Path

DIR = Path(os.environ.get("JAWABAN_DIR", Path(__file__).parent))


def import_file(nama_file):
    path = DIR / nama_file
    if not path.exists():
        raise AssertionError(f"File {nama_file} belum ada di folder {DIR}")
    spec = importlib.util.spec_from_file_location(nama_file.replace(".py", ""), path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        # Menangani jika ada input() di root level saat import
        pass
    return module


def jalankan(nama_file, masukan):
    path = DIR / nama_file
    if not path.exists():
        raise AssertionError(f"File {nama_file} belum ada di folder {DIR}")
    hasil = subprocess.run([sys.executable, str(path)], input=masukan,
                           capture_output=True, text=True, timeout=10)
    if hasil.returncode != 0:
        raise AssertionError(f"Program error:\n{hasil.stderr}")
    return hasil.stdout


class Test14(unittest.TestCase):
    # Tes Soal 1: Fungsi celcius_ke_fahrenheit & program
    def test_soal1_fungsi_return(self):
        # Memastikan fungsi return nilai (bukan None)
        path = DIR / "jawaban_1.py"
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()
        self.assertIn("def celcius_ke_fahrenheit", code, "Fungsi celcius_ke_fahrenheit belum dibuat")
        self.assertIn("return", code, "Fungsi harus menggunakan return, bukan print saja")

    def test_soal1_program_nol(self):
        output = jalankan("jawaban_1.py", "0\n")
        self.assertIn("Fahrenheit: 32", output)

    def test_soal1_program_seratus(self):
        output = jalankan("jawaban_1.py", "100\n")
        self.assertIn("Fahrenheit: 212", output)

    # Tes Soal 2: Fungsi hitung_parkir & program
    def test_soal2_fungsi_return(self):
        path = DIR / "jawaban_2.py"
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()
        self.assertIn("def hitung_parkir", code, "Fungsi hitung_parkir belum dibuat")
        self.assertIn("return", code, "Fungsi harus menggunakan return")

    def test_soal2_program_satu_jam(self):
        output = jalankan("jawaban_2.py", "1\n")
        self.assertIn("Biaya: 5000", output)

    def test_soal2_program_dua_jam(self):
        output = jalankan("jawaban_2.py", "2\n")
        self.assertIn("Biaya: 5000", output)

    def test_soal2_program_tiga_jam(self):
        output = jalankan("jawaban_2.py", "3\n")
        self.assertIn("Biaya: 7000", output)

    def test_soal2_program_lima_jam(self):
        output = jalankan("jawaban_2.py", "5\n")
        self.assertIn("Biaya: 11000", output)


if __name__ == "__main__":
    unittest.main()
