# -*- coding: utf-8 -*-
"""71230976_12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JHc45jo9VXxcpxIYpcQ9RgrOiTTBCG_x
"""

#latman 12.1
inkategori = int(input("Masukkan Jumlah Kategori: "))
data_apk = {}

for i in range(inkategori):
    nama_kategori = input("Masukkan Nama Kategori: ")
    print("Masukkan 5 nama aplikasi di kategori", nama_kategori)
    apk = list()

    for j in range(5):
        nama_apk = input("Masukkan Nama Aplikasi: ")
        apk.append(nama_apk)
    data_apk[nama_kategori] = apk
print(data_apk)
print()

daftar_apk_lst = list()
for apk in data_apk.values():
    daftar_apk_lst.append(set(apk))
print(daftar_apk_lst)
print()

hasil = daftar_apk_lst
for x in range(1,inkategori):
    unik = hasil[x-1] ^ hasil[x]
    print("Aplikasi Yang Hanya Muncul Di 1 Kategori Saja: ", unik)

aplikasi_di_dua_kategori = set()
for x in range(inkategori-1):
    for y in range(x+1, inkategori):
        aplikasi_di_dua_kategori |= hasil[x] & hasil[y]

print("Aplikasi Yang Muncul Di Tepat Dua Kategori Saja: ", aplikasi_di_dua_kategori)

#latman 12.2
data = input("Masukkan kalimat: ")
data_list = list(data)
print("List ke Set")
print("sebelum ->",data_list)
print("sesudah ->",set(data_list))
print()
data_set = set(data)
print("Set ke List")
print("sebelum ->",data_set)
print("sesudah ->",list(data_set))
print()
data_tuple = tuple(data)
print("Tuple ke Set")
print("Sebelum ->",data_tuple)
print("Sesudah ->",set(data_tuple))
print()
print("Set ke Tuple")
print("sebelum ->",data_set)
print("sesudah ->",tuple(data_set))

#latman 12.3
teks1 = input("Masukkan file teks 1: ")
teks2 = input("Masukkan file teks 2: ")
try:
    handle = open(teks1, 'r')
    handle2 = open(teks2, 'r')
except:
    print("File cannot be opened")
    exit()
a = set()

for teks in handle:
    tekslow = teks.lower()
    tekspl = tekslow.split()
    for b in tekspl:
        a.add(b)
for teks in handle2:
    tekslow = teks.lower()
    tekspl = tekslow.split()
    for b in tekspl:
        a.add(b)
print(a)