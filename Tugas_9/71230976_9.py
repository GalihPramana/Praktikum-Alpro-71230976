# -*- coding: utf-8 -*-
"""71230976_9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fMCPSM8TuByHtAalVZ5DPifgLgxJ_v65
"""

#Latihan 9.1
angka = [12,45,25,46,75,32,123]
setbil = set()
urutan = []
for i in angka:
    if i not in setbil:
        urutan.append(i)
    urutan.sort(reverse = 1)
print(urutan[:3])

#Latihan 9.2
nilai = []
while True:
    try:
        angka = float(input("Masukkan Angka (untuk selesai,ketik done): "))
        nilai.append(angka)
    except :
        break

if nilai:
    print(f"Nilai minimum: {min(nilai)}")
    print(f"Nilai maksimum: {max(nilai)}")
else:
    print("Tidak ada nilai yang dimasukkan.")

#Latihan 9.2
filename = "berita.txt"
kata = []

with open(filename, 'r') as handle:
    line = handle.read()
    line_S = line.split()
    kata.extend(line_S)

print("===== ISI BERITA =====\n", line)
print("===== KATA UNIK =====\n", kata)
