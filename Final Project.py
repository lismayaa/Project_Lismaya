print("FINAL PROJECT KELOMPOK")
print("Kelas\t : 19.1C.37 SISTEM INFORMASI")
print("=" * 80)
print("Kelompok")

print("\tNo             Nama              Nim")
print("\t.1.    Indra Ardiansyah        19200437")
print("\t.2.    Lismaya                 19200204")
print("\t.3.    Dita Natasya Putri      19200961")
print("\t.4.    Farid Rishardi          19200531")
print("=" * 80)
print("\n")
print("-" * 80)
teks1 = "~ Resto YUK MAMPIR ~"
teks2 = "RT 003/ RW 005, Jl. Yang Lurus, DIPINANG"
x = teks1.center(70)
y = teks2.center(70)
print(x)
print(y)
print("=" * 80)


def mainmenu():
    print('Halaman kasir "Yuk Mampir"')
    username = input('Masukan username kasir anda : ')
    password = input('Masukan password: ')

    if username == 'admin' and password == '0987':
        print('Login yuk mampir berhasil...>>>\n\n')


    else:
        print('Login yuk mampir gagal coba lagi iya..<<<')
        mainmenu()


if __name__ == '__main__':
    mainmenu()


def menuUtama():
    global n

    print()
    n = (input("Masukkan Nama Konsumen : "))
    print("Selamat Datang di Resto Yuk Mampir")
    print("Nama Konsumen : ", n)
    print("""Masukkan Pilihan
    1. Makanan dan Minuman
    2. Keluar""")
    print('')


menuUtama()


def menuUtama1():
    print("""Masukkan Pilihan
    1. Makanan dan Minuman
    2. Keluar""")
    print('')


class makanan():
    def SUSHI(self, x, menu1, harga1, jumlah1):
        print("")
        print("    ", menu1, "\t", x, "\t    Rp.", harga1, "\t    Rp.", jumlah1)
        return jumlah1

    def RAMEN(self, x, menu1, harga1, jumlah1):
        print("")
        print("    ", menu1, "\t", x, "\t    Rp.", harga1, "\t    Rp.", jumlah1)
        return jumlah1

    def BULGOGI(self, x, menu1, harga1, jumlah1):
        print("")
        print("    ", menu1, "\t", x, "\t    Rp.", harga1, "\t    Rp.", jumlah1)
        return jumlah1

    def SASHIMI(self, x, menu1, harga1, jumlah1):
        print("")
        print("    ", menu1, "\t", x, "\t    Rp.", harga1, "\t    Rp.", jumlah1)
        return jumlah1

    def BIMBIMBAP(self, x, menu1, harga1, jumlah1):
        print("")
        print("    ", menu1, "\t", x, "\t    Rp.", harga1, "\t    Rp.", jumlah1)
        return jumlah1


class minuman(makanan):
    def XIBOBA(self, z, menu2, harga2, jumlah2):
        print("")
        print("    ", menu2, "\t", z, "\t    Rp.", harga2, "\t    Rp.", jumlah2)
        return jumlah2

    def OCHA(self, z, menu2, harga2, jumlah2):
        print("")
        print("    ", menu2, "\t", z, "\t    Rp.", harga2, "\t    Rp.", jumlah2)
        return jumlah2

    def BANANA_MILK(self, z, menu2, harga2, jumlah2):
        print("")
        print("    ", menu2, "\t", z, "\t    Rp.", harga2, "\t    Rp.", jumlah2)
        return jumlah2

    def MATCHA(self, z, menu2, harga2, jumlah2):
        print("")
        print("    ", menu2, "\t", z, "\t    Rp.", harga2, "\t    Rp.", jumlah2)
        return jumlah2

    def YOGHURT(self, z, menu2, harga2, jumlah2):
        print("")
        print("    ", menu2, "\t", z, "\t    Rp.", harga2, "\t    Rp.", jumlah2)
        return jumlah2


class TOTAL(makanan):

    def total(self, totalsemua, pajak):
        print("_" * 60)
        print("")
        print("ppn 10%      :\t\t\t\t    Rp. ", pajak)
        print("Subtotal     :\t\t\t\t    Rp. ", totalsemua)
        print("_" * 60)

    def Bayar(self, bayar):
        self.bayar = bayar

    def Metode(self):
        if debit == ("bni") or debit == ("BNI"):
            print("BNI")
        elif debit == ("bca") or debit == ("BCA"):
            print("BCA")
        else:
            print("MANDIRI")

    def getMetode(self):
        global debit

        pilih = (input("Metode Pembayaran [CASH / DEBIT] \t    :  "))
        if pilih == ("C") or pilih == ("c"):
            pass
        elif pilih == ("D") or pilih == ("d"):
            debit = (input("Metode Pembayaran [BNI/BCA/MANDIRI]\t    : "))
            if debit == ("bni") or debit == ("BNI"):
                print("")
            elif debit == ("bca") or debit == ("BCA"):
                print("")
            elif debit == ("mandiri") or debit == ("MANDIRI"):
                print("")
        else:
            print("Maaf Kode Yang Anda Masukkan Salah")
            print("Coba Lagi <<<", main())
        print("_" * 60)

    def getKembalian(self):
        kembalian = (int(self.bayar - totalsemua))
        print("Uang Kembali :\t\t\t\t    Rp. ", kembalian)
        print("=" * 60)
        return kembalian


def back_menu():
    back = input("\nApakah Anda Ingin Memesan Lagi ? [Y/T] :    ")
    if back == ("Y") or back == ("y"):
        menuUtama1()
        Pilihan_makanan()
        tanya()
        struk_makan()
        struk_minum()
        main()
        back_menu()
        print('')
    else:
        print("\t    <<<Terima Kasih Telah Mampir Ditempat Kami>>> ")
        print("\t      <<Selamat Jalan & Semoga Sampai Tujuan>>  ")
        exit()


def pilihan_minuman():
    global pilihan_minum
    global z
    global harga2
    global jumlah2
    global menu2

    mn = minuman()
    print("==========================================")
    print("   No        Menu             Harga     ")
    print("==========================================")
    print("   1.        XIBOBA           Rp.22000")
    print("   2.        OCHA             Rp.27000")
    print("   3.        BANANA MILK      Rp.20000")
    print("   4.        MATCHA           Rp.19000")
    print("   5.        YOGHURT          Rp.24500")
    pilihan_minum = (str(input("Masukkan Pilihan Anda : ")))
    if pilihan_minum == ("1"):
        mn = minuman()
        menu2 = "XIBOBA"
        harga2 = 22000
        z = (int(input("Jumlah Gelas : ")))
        jumlah2 = z * 22000

    elif pilihan_minum == ("2"):
        mn = minuman()
        menu2 = "OCHA"
        harga2 = 27000
        z = (int(input("Jumlah Gelas : ")))
        jumlah2 = z * 27000

    elif pilihan_minum == ("3"):
        mn = minuman()
        menu2 = "BANANA MILK"
        harga2 = 20000
        z = (int(input("Jumlah Gelas : ")))
        jumlah2 = z * 20000

    elif pilihan_minum == ("4"):
        mn = minuman()
        menu2 = "MATCHA"
        harga2 = 19000
        z = (int(input("Jumlah Gelas : ")))
        jumlah2 = z * 19000

    elif pilihan_minum == ("5"):
        mn = minuman()
        menu2 = "YOGHURT"
        harga2 = 24500
        z = (int(input("Jumlah Gelas : ")))
        jumlah2 = z * 24500
    else:
        print("Maaf menu yang Anda pilih tidak tersedia")
        print("Silahkan masukan ulang pilihan Anda")
        print('')
        pilihan_minuman()


def Pilihan_makanan():
    global pilihan_makan
    global x
    global harga1
    global jumlah1
    global menu1

    mk = makanan()
    print("==========================================")
    print("   No        Menu             Harga     ")
    print("==========================================")
    print("   1.        SUSHI            Rp.28000")
    print("   2.        RAMEN            Rp.36000")
    print("   3.        BULGOGI          Rp.34000")
    print("   4.        SASHIMI          Rp.33000")
    print("   5.        BIMBIMBAP        Rp.32000")
    print("   6.        Minuman")

    pilihan_makan = (str(input("Masukkan Pilihan Anda : ")))
    if pilihan_makan == ("1"):
        mk = makanan()
        menu1 = "SUSHI"
        harga1 = 28000
        x = (int(input("Jumlah Porsi : ")))
        jumlah1 = x * 28000

    elif pilihan_makan == ("2"):
        mk = makanan()
        menu1 = "RAMEN"
        harga1 = 36000
        x = (int(input("Jumlah Porsi : ")))
        jumlah1 = x * 36000

    elif pilihan_makan == ("3"):
        mk = makanan()
        menu1 = "BULGOGI"
        harga1 = 34000
        x = (int(input("Jumlah Porsi : ")))
        jumlah1 = x * 34000

    elif pilihan_makan == ("4"):
        mk = makanan()
        menu1 = "SASHIMI"
        harga1 = 33000
        x = (int(input("Jumlah Porsi : ")))
        jumlah1 = x * 33000

    elif pilihan_makan == ("5"):
        mk = makanan()
        menu1 = "BIMBIMBAP"
        harga1 = 32000
        x = (int(input("Jumlah Porsi : ")))
        jumlah1 = x * 32000

    elif pilihan_makan == ("6"):
        pilihan_minuman()
    else:
        print("Maaf menu yang Anda pilih tidak tersedia")
        print("Silahkan masukan ulang pilihan Anda")
        print('')
        Pilihan_makanan()


def selamat_datang():
    a = input("Masukkan Pilihan : ")
    if a == ("1"):
        Pilihan_makanan()
    elif a == ("2"):
        exit()
    else:
        print("Maaf Kode Yang Anda Masukkan Salah")
        print("Silahkan Input Ulang Kode Anda")
        print("")
        selamat_datang()


selamat_datang()


def Total():
    global jumlahsemua
    global pajak
    global totalsemua
    jumlahsemua = 0
    pajak = 0
    totalsemua = 0

    to = TOTAL()
    jumlahsemua = jumlahsemua + (jumlah1 + jumlah2)
    pajak = pajak + (jumlahsemua * 0.1)
    totalsemua = jumlahsemua + pajak

    to.total(totalsemua, pajak)


def struk_minum():
    mn = minuman()
    if pilihan_minum == ("1"):
        mn.XIBOBA(z, menu2, harga2, jumlah2)
    elif pilihan_minum == ("2"):
        mn.OCHA(z, menu2, harga2, jumlah2)
    elif pilihan_minum == ("3"):
        mn.BANANA_MILK(z, menu2, harga2, jumlah2)
    elif pilihan_minum == ("4"):
        mn.MATCHA(z, menu2, harga2, jumlah2)
    elif pilihan_minum == ("5"):
        mn.YOGHURT(z, menu2, harga2, jumlah2)
    Total()


def struk_makan():
    print("-" * 60)
    teks1 = "~ Resto YUK MAMPIR ~"
    teks2 = "RT 003/ RW 005, Jl. Yang Lurus, DIPINANG"
    b = teks1.center(60)
    y = teks2.center(60)
    print(b)
    print(y)
    print("=" * 60)
    print("Nama Konsumen : ", n)
    print("-" * 60)
    print("\t\t\t Dine In")
    print("-" * 60)
    print("    Menu         Qty         Harga              Total")
    print("_" * 60)
    mk = makanan()
    if pilihan_makan == ("1"):
        mk.SUSHI(x, menu1, harga1, jumlah1)
    elif pilihan_makan == ("2"):
        mk.RAMEN(x, menu1, harga1, jumlah1)
    elif pilihan_makan == ("3"):
        mk.BULGOGI(x, menu1, harga1, jumlah1)
    elif pilihan_makan == ("4"):
        mk.SASHIMI(x, menu1, harga1, jumlah1)
    elif pilihan_makan == ("5"):
        mk.BULGOGI(x, menu1, harga1, jumlah1)
    elif pilihan_makan == ("6"):
        struk_minum()


def tanya():
    back = input("Apakah Anda ingin memesan minuman? [y/t]: ")
    if back == ("Y") or back == ("y"):
        pilihan_minuman()
        struk_makan()
        struk_minum()
        print('')
    elif back == ("T") or back == ("t"):
        struk_makan()
    else:
        print("\t    <<<Terima Kasih Telah Mampir Ditempat Kami>>> ")
        print("\t      <<Selamat Jalan & Semoga Sampai Tujuan>>  ")
        struk_makan()
        exit()


tanya()

to = TOTAL()


def main():
    to.getMetode()
    to.Metode()
    print("--------")
    to.Bayar(int(input("Uang Bayar   :\t\t\t\t    Rp. ")))
    to.getKembalian()


main()
back_menu()
