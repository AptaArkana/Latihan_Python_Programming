# Instruksi cetak di bawah menyebabkan program terhenti karena mengalami IndexError
# Tangani error tersebut dengan teknik Error Handling yang sudah dipelajari
# Setelah itu, jalankan program dan pastikan tidak ada lagi pemberitahuan error pada program

list = [1, 3, 5, 7, 9, 11, 13, 15]
try:
    print(list[20])
except IndexError:
    print('Maaf, index yang dipinta melebihi batas range')