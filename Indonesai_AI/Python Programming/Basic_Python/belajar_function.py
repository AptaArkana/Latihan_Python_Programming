# Buatlah fungsi yang akan mengevaluasi apakah modulus dari hasil kali 2 angka yang diterima bernilai 0 atau tidak
# Gunakan statement return untuk mengembalikan nilai tersebut lalu cetak hasilnya
# Beri nama cek_modulus() pada fungsi tersebut

def cek_modulus(angka1, angka2):
    #Operator untuk perkalian
    perkalian = angka1 *  angka2
    #Operator untuk modulus
    modulus = perkalian % 2

    #Kondisi cek modulus
    if modulus == 0:
        print("Hasil perkalian:", perkalian)
        print("Hasil pengecekan modulus: True")
    else:
        print("Hasil perkalian:", perkalian)
        print("Hasil pengecekan modulus: False")

angka1 = 12
angka2 = 8

a = cek_modulus(angka1, angka2)