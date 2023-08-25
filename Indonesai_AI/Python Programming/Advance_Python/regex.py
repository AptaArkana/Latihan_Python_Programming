# Coba tangkap informasi domisili (Tokyo) dan informasi nomor (021 7581 6521) pada 2 teks berikut
# Gunakan modul regex (re)

import re

pattern = ['Tokyo', '021 7581 6521']

teks1 = "Saya yang berdomisili di Tokyo bisa dihubungi di nomor berikut 021 7581 6521"
teks2 = "Nomor ini tidak bisa dihubungi 021 1121 6551, karena sudah di luar area Tokyo"

def cari_kata(text):
    for patterns in pattern:
        print('Mencari "%s" in "%s" -> ' % (patterns, text), end=' ')

        if re.search(patterns, text):
            print('Ketemu')
        else:
            print('Tidak ketemu')

cari = cari_kata(teks2)
