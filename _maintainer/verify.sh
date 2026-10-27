#!/usr/bin/env bash
# Memastikan tiap tes: LULUS di solusi benar, GAGAL di solusi salah.
cd "$(dirname "$0")/.." || exit 1
ok=1
check() { # modul  folder-tes  file-tes
  JAWABAN_DIR="_maintainer/solusi/$1" python3 "$2/$3" >/dev/null 2>&1 \
    && echo "[OK]   $1 lulus di solusi benar" || { echo "[GAGAL] $1 tidak lulus di solusi benar"; ok=0; }
  JAWABAN_DIR="_maintainer/salah/$1" python3 "$2/$3" >/dev/null 2>&1 \
    && { echo "[GAGAL] $1 LULUS di solusi salah (tes terlalu lemah)"; ok=0; } || echo "[OK]   $1 gagal di solusi salah"
}
check 1.0 level-1-foundations/1.0-setup/latihan test_1_0.py
check 1.1 level-1-foundations/1.1-variabel/latihan test_1_1.py
check 1.2 level-1-foundations/1.2-kondisi/latihan test_1_2.py
check 1.3 level-1-foundations/1.3-loop/latihan test_1_3.py
check 1.4 level-1-foundations/1.4-fungsi/latihan test_1_4.py
check 1.5 level-1-foundations/1.5-data-collection/latihan test_1_5.py
check 1.6 level-1-foundations/1.6-debugging/latihan test_1_6.py
check 1.7 level-1-foundations/1.7-file-csv/latihan test_1_7.py
check 1.8 level-1-foundations/1.8-mini-proyek/latihan test_1_8.py
[ $ok = 1 ] && echo "SEMUA TES VALID" || { echo "ADA MASALAH"; exit 1; }
