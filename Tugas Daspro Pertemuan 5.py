print("Nama : Lismaya")
print("NIM  : 19200204")
print("="*60)
txt = "GEROBAK FRIED CHICKEN"
x = txt.center(50)
print(x)
print("-"*60)
print("Kode     Jenis Potong     Harga")
print("---------------------------------")
print("D            Dada        Rp 2.500")
print("P            Paha        Rp 2.000")
print("S            Sayap       Rp 1.500")
print("---------------------------------")

banyak_jenis = int(input("Masukan banyak jenis : "))
banyak_potong = []
kode_potong = []
jenis_potong = []
harga = []
jumlah_harga = []

i = 0
while i < banyak_jenis:
    print("Jenis ke- ", int(i+1))
    kode_potong.append(input("Kode Potong [D/P/S] : "))
    banyak_potong.append(int(input("Masukan banyak potong : ")))

    if kode_potong[i] == "D" or kode_potong[i] == "d":
        jenis_potong.append("Dada")
        harga.append(2500)
        jumlah_harga.append(banyak_potong[i]*int(2500))
    elif kode_potong[i] == "P" or kode_potong[i] == "p":
        jenis_potong.append("Paha")
        harga.append(2000)
        jumlah_harga.append(banyak_potong[i]*int(2000))
    elif kode_potong[i] == "S" or kode_potong[i] == "s":
        jenis_potong.append("Sayap")
        harga.append(1500)
        jumlah_harga.append(banyak_potong[i]*int(1500))
    else:
        jenis_potong.append("Jenis Potong Tidak Ditemukan")
        harga.append(0)
        jumlah_harga.append(banyak_potong[i]*int(0))
    i = i + 1
print("="*60)
txt1="GEROBAK FRIED CHICKEN"
y=txt1.center(50)
print(y)
print("-"*60)
print("No   Jenis       Harga       Banyak      Jumlah    ")
print("     Potong      Satuan      Beli        Harga     ")
print("-"*60)

jumlah_bayar=0
a=0
while a < banyak_jenis:
    jumlah_bayar = jumlah_bayar + jumlah_harga[a]
    print("%i   %s         %i         %i         %i" %(a+1,jenis_potong[a],harga[a],banyak_potong[a],jumlah_harga[a]))
    a=a+1

pajak = jumlah_bayar*0.1
total_bayar=jumlah_bayar + pajak
print("                 Jumlah Bayar Rp.",jumlah_bayar)
print("                 Pajak 10%    Rp.",pajak)
print("                 Total        Rp.",total_bayar)

print("=====Terima kasih anda telah membeli produk kami=====")