# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Rabu, 28 April 2021 
# Deskripsi   : Program menentukan hubungan dua garis

a1 = int(input('masukkan a1: '))
b1 = int(input('masukkan b1: '))
c1 = int(input('masukkan c1: '))
a2 = int(input('masukkan a2: '))
b2 = int(input('masukkan b2: '))
c2 = int(input('masukkan c2: '))

m1 = (-a1)/b1
m2 = (-a2)/b2

if m1 == m2:
    print('kedua garis sejajar')
elif m1*m2 == -1:
    print('kedua garis tegak lurus')
else:
    print('kedua garis tidak sejajar dan tidak tegak lurus')