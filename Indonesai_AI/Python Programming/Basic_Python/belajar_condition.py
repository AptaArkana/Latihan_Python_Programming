# Buatlah satu logika kondisi yang menentukan jika harga laptop sekian maka 
# saya akan mempertimbangkan lagi jika harga handphone sekian maka saya akan beli keduanya atau tidak
# Gunakan teknik NESTED IF!

harga_laptop = 4000
harga_handphone = 5000

if harga_laptop <= 5000:
    if harga_handphone <= 4000:
        print("Saya akan pertimbangkan beli keduanya")
    else:
        print("Saya akan beli laptop saja.")
else:
    print("Saya tidak beli laptop maupun handphone")