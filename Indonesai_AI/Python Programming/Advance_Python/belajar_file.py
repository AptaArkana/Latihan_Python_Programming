# Bacalah data yang ada di file data.txt
# Lalu tambahkan teks "Bahasa Pemrograman Python memiliki masa depan yang cerah"
# Pastikan tidak menghilangkan data yang sudah ada di file tersebut!

with open('./data.txt', mode='+a', encoding='utf-8') as f:
    f.write('\n# Bahasa Pemrograman Python memiliki masa depan yang cerah')