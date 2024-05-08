# -*- coding: utf-8 -*-
"""71230976_10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uvRcKgaIu91NUg4oKhPcj44G5OUW5hP_
"""

#latman 10.1
dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Key   Value   Item")
for item_num, (key, value) in enumerate(dictionary.items(), start=1):
    print(f"{key}     {value}     {item_num}")

#latman 10.2
lista = ["red", "green", "blue"]
listb = ['#FF0000', '#008000', '#0000FF']

x = dict(zip(lista, listb))
print(x)

#latman 10.3
dictionary = dict()
namafile = input('Enter file name: ')
try:
    handle = open(namafile)
except:
    print('File cannot be opened:', namafile)
    exit()
for line in handle:
    katakata = line.split()
    if len(katakata) < 2 or katakata[0] != 'From':
        continue
    else:
        dictionary[katakata[1]] = 1 +  dictionary.get(katakata[1],0)
print(dictionary)

#latman 10.4
dictionary = {}
namafile = input('Enter file name: ')
try:
    with open(namafile) as handle:
        for line in handle:
            words = line.split()
            if len(words) > 0 and words[0] == "From:":
                domain = words[1][words[1].find("@") + 1:]
                dictionary[domain] = dictionary.get(domain, 0) + 1
except FileNotFoundError:
    print('File cannot be opened:', namafile)
    exit()

print(dictionary)