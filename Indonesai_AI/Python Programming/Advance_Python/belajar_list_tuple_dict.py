# Buatlah 2 buah dictionary yang memuat informasi 10 murid dan informasi 10 karyawan
# Lalu cetak data murid dan karyawan yang berada di-index 2 dan 9
# Setelah itu cetak semua data yang ada di dictionary tersebut dengan for loop

dict_murid = {
    '001':'andi',
    '002':'budi',
    '003':'anggun',
    '004':'fitri',
    '005':'bagus',
    '006':'jasmine',
    '007':'agus',
    '008':'tedjo',
    '009':'dina',
    '010':'sari'
}

dict_karyawan = {
    '01':'karyawan_andi',
    '02':'karyawan_budi',
    '03':'karyawan_anggun',
    '04':'karyawan_fitri',
    '05':'karyawan_bagus',
    '06':'karyawan_jasmine',
    '07':'karyawan_agus',
    '08':'karyawan_tedjo',
    '09':'karyawan_dina',
    '10':'karyawan_sari'
}

# Print indeks tertentu
print('Indeks ke 2 murid', dict_murid['002'])
print('Indeks ke 9 karyawan', dict_karyawan['09'])
print('\n')
# Print semua data didalam dict
for key, value in dict_murid.items():
    print('Indeks ke-',key, 'dari dict murid adalah',value)