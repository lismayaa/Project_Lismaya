print("Nama : Satrio Lantip Pengaribowo")
print("NIM  : 19200299")
print("Nama : Lismaya")
print("NIM  : 19200204")
print("="*100)
txt = ("Data Maskapai Penerbangan ke Yogyakarta")
x = txt.center(100)
print(x)
print("Kode Maskapai      Nama Maskapai       Kode Kelas        Nama Kelas       Harga")
print("     A               Garuda                 1            Eksekutif     Rp 3.000.000")
print("                                            2            Bisnis        Rp 2.000.000")
print("                                            3            Ekonomi       Rp 1.000.000")
print("     B              Lion Air                1            Eksekutif     Rp 2.500.000")
print("                                            2            Bisnis        Rp 1.500.000")
print("                                            3            Ekonomi       Rp   800.000")
print("="*100)
nama = input("Nama Pemesanan :")
kode = input("Pilihan Kode Maskapai :")
kelas = str(input("Pilihan Kode Kelas (sesuaikan dengan list) :"))
jml_tiket = int(input("Masukan Jumlah Tiket :"))
print("="*100)
if kode == "A" or "a":
    Maskapai = "Garuda"
    if kelas == "A1" or "a1":
        Nama_Kelas = "Eksekutif"
        Harga = 3000000
        Bayar = jml_tiket * Harga
    if kelas == "A2" or "a2":
        Nama_Kelas = "Bisnis"
        Harga = 2000000
        Bayar = jml_tiket * Harga
    if kelas == "A3" or "a3":
        Nama_Kelas = "Ekonomi"
        Harga = 1000000
    else :
        Nama_Kelas = "Tidak sesuai dengan list"
        Harga = 0
        Bayar = 0
elif kode == "B" or "b":
    Maskapai = "Lion Air"
    if kelas == "B1" or "b1":
        Nama_Kelas = "Eksekutif"
        Harga = 2500000
        Bayar = jml_tiket * Harga
    if kelas == "B2" or "b2":
        Nama_Kelas = "Bisnis"
        Harga = 1500000
        Bayar = jml_tiket * Harga
    if kelas == "B3" or "b3":
        Nama_Kelas = "Ekonomi"
        Harga = 800000
        Bayar = jml_tiket * Harga
    else :
        Nama_Kelas = "Tidak sesuai dengan list"
        Harga = 0
        Bayar = 0
else :
    Maskapai = "Tidak ditemukan dalam daftar"
    Harga = 0
    Bayar = 0
txt1 = "Data Penerbangan Pemesanan Tiket Penerbangan Menuju Yogyakarta"
y = txt1.center(100)
print(y)
print("="*100)
print("Maskapai Penerbangan :", Maskapai)
print("Kelas Penerbangan :", kelas)
print("Jumlah Tiket yang Dipesan :",jml_tiket)
print("Harga Satuan Tiket :", Harga)
print("Total Pembayaran :",+ (Bayar))
print("="*40)
print("TERIMA KASIH")