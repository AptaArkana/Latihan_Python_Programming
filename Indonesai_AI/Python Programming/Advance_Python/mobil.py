# Buatlah satu class Mobil yang bisa digunakan untuk mencetak beragam tipe mobil
# Pastikan class tersebut memiliki setidaknya 3 attributes dan 3 methods

class Mobil:
    def __init__(self, merek, warna, tahun):
        self.merek = merek
        self.warna = warna
        self.tahun = tahun
        self.mesin_hidup = False

    #nyalakan mesin
    def mesin_nyala(self):
        if not self.mesin_hidup:
            self.mesin_hidup = True
            print(f"Mesin mobil {self.merek} {self.warna} tahun {self.tahun} telah dinyalakan.")
        else:
            print("Mesin sudah hidup.") 

    #matikan mesin
    def mesin_mati(self):
        if self.mesin_hidup:
            self.mesin_hidup = False
            print(f'mesin mobil {self.merek} sudah dimatikan')
        else:
           print('Mesin sudah mati') 

    #cek info mesin
    def info_mesin(self):
        status_mesin = "hidup" if self.mesin_hidup else "mati"
        return f"Mobil {self.merek} mesin {status_mesin}"
    
    #masukan gigi
    def gigi_mobil(self, gigi):
        print(f'mobil {self.merek} masuk gigi {gigi}')



mobil1 = Mobil('Toyota', 'Hitam', 2022)
print(mobil1.info_mesin())
mobil1.mesin_nyala()
print(mobil1.info_mesin())
mobil1.gigi_mobil(1)