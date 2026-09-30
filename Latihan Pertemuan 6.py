print("DASAR PEMROGRAMAN")
print("LATIHAN PERTEMUAN 6")
print("Nama : Lismaya")
print("NIM  : 19200204")
print("----------------------------------------")
#variable yang berulang menggunakan List/matriks
list_nim = []
list_uts = []
list_uas = []
list_total = []

ulang = 2
for i in range(ulang):
    print("Data Ke-"+str(i+1))
    list_nim.append(str(input("Masukan NIM anda : ")))
    list_uts.append(int(input("Masukan Nilai UTS anda : ")))
    list_uas.append(int(input("Masukan Nilai UAS anda : ")))
#proses
for i in range(ulang):
    list_total.append((list_uas[i]+list_uts[i])/2)
#cetak
print("==========================================")
print("NIM      Nilai UTS     Nilai UAS    Total")
print("==========================================")
for i in range(ulang):
    print("%s\t%i\t\t\t%i\t\t\t%i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
print("==========================================")