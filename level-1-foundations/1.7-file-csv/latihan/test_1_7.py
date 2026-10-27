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


class Test17(unittest.TestCase):
    # Tes Soal 1: Tulis catatan
    def test_soal1_tulis_file(self):
        output = jalankan("jawaban_1.py", "apel,jeruk,mangga\n")
        self.assertIn("Berhasil ditulis ke buah.txt", output)
        file_hasil = DIR / "buah.txt"
        self.assertTrue(file_hasil.exists(), "File buah.txt belum terbentuk")
        with open(file_hasil, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        self.assertEqual(lines, ["apel", "jeruk", "mangga"])
        if file_hasil.exists():
            file_hasil.unlink()

    # Tes Soal 2: Rekap CSV
    def test_soal2_rekap_csv(self):
        csv_dummy = DIR / "data_dummy.csv"
        with open(csv_dummy, "w", encoding="utf-8") as f:
            f.write("kategori,biaya\n")
            f.write("makan,25000\n")
            f.write("transport,15000\n")
            f.write("kopi,10000\n")

        try:
            output = jalankan("jawaban_2.py", "data_dummy.csv\n")
            self.assertIn("Total biaya: 50000", output)
        finally:
            if csv_dummy.exists():
                csv_dummy.unlink()


if __name__ == "__main__":
    unittest.main()
