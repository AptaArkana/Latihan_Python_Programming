# Buatlah operasi loop yang akan mencetak angka GENAP dari 1-120
# Lalu gunakan statement continue agar operasi tidak mencetak angka 12, 56 dan 78
# Dan juga gunakan statement break agar operasi berhenti hanya sampai di angka 100

def print_angka():
    for angka in range (1,121):
        if angka % 2 == 0:
            if angka in [12, 56, 78]:
                continue
            if angka == 100:
                break

            print('ini angka ke -', angka)
        else: continue

a = print_angka()