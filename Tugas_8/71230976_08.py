# -*- coding: utf-8 -*-
"""71230976_08.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GsvJLzRg5E6qlRRkkVOVU7ciB21_5fI4
"""

#Latihan Mandiri 8.1
def banding_teks():
    file1 = input("Input file pertama: ")
    file2 = input("Input file kedua: ")

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        x = max(len(lines1), len(lines2))

        for i in range(x):
            if lines1[i] != lines2[i]:
                print(f"Perbedaan ada di {i+1}:")
                print(f"  File 1: {lines1[i].strip()}")
                print(f"  File 2: {lines2[i].strip()}")
banding_teks()

#Latihan Mandiri 8.2
with open("soal.txt", "r") as pertanyaan:
    for index, baris in enumerate(pertanyaan, start=1):
        i = baris.strip().split(" || ")
        print(f"{i[0]}")
        jawab = input("Jawab: ")
        if jawab.lower() == i[1].lower():
            print("Jawaban Benar")
        else:
            print("Jawaban Salah")
