# -*- coding: utf-8 -*-
"""71230976(6).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T-iPBXJIzkHvYKQpbIdSqLEgEY8liPdF
"""

#Latihan Mandiri 6.1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input("Masukkan bilangan: "))
for i in range(N - 1, 1, -1):
    if is_prime(i):
        print(f"input n = {N}, maka prima terdekat < {N} adalah {i}")
        break

#Latihan Mandiri 6.2
def faktor(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil = hasil * i
    return hasil

def faktorial(n):
    i = bilangan
    while i > 0:
        print(faktor(i), end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        i = i - 1
        print()

bilangan = int(input("bilangan = "))
faktorial(bilangan)

#Latihan Mandiri 6.3
def deret(tinggi, lebar):
    nilai = 1
    for i in range(1, tinggi+1):
        for j in range(1, lebar+1):
            print(nilai, end=" ")
            nilai = nilai + 1
        print()

tinggi = int(input("Masukkan tinggi deret: "))
lebar = int(input("Masukkan lebar deret: "))

deret(tinggi, lebar)