# -*- coding: utf-8 -*-
"""71230976(4).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VEK0pPPjjbjlHb12YD-LyRjQzh1fD7Xg
"""

#Latihan 4.1
def cek_angka(a,b,c):
    if a != b and a != c and b != c and ( a + b == c or a + c == b or b + c == a):
      return True
    else:
      return False

print(cek_angka(5,3,2))
print(cek_angka(1,2,3))
print(cek_angka(4,5,4))

#Latihan 4.1
cek_angka = lambda a,b,c: True if (a!=b and a!=c and b!=c and (a + b == c or a + c == b or b + c == a)) else False
print(cek_angka(1,2,3))

#Latihan 4.2

def cek_digit_belakang(a,b,c):
    a = a%10
    b = b%10
    c = c%10
    if (a == b or a == c or b == c):
       return True
    else:
       return False

inputA =int(input("Masukkan bilangan a: "))
inputB =int(input("Masukkan bilangan b: "))
inputC =int(input("Masukkan bilangan c: "))

print("Hasil:", cek_digit_belakang(inputA,inputB,inputC))

#Latihan 4.3
celcius_to_farenheit = lambda C: (9/5*C)+32
celcius_to_reamur = lambda C:0.8*C

print(celcius_to_farenheit(100))
print(celcius_to_reamur(80))
print(celcius_to_farenheit(0))