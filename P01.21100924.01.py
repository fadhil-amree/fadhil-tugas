# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Rabu, 28 April 2021 
# Deskripsi   : Program indeks pengkom

x = float(input('masukkan nilai akhir Tuan Mor: '))

if x >= 80:
    index = 'A'
elif 75 <= x < 80:
    index = 'AB'
elif 70 <= x < 75 :
    index = 'B'
elif 60 <= x < 70:
    index = 'BC'
elif 50 <= x < 60:
    index = 'C'
elif 40 <= x <50:
    index = 'D'
elif x < 40:
    index = 'E'

print('Tuan Mor mendapatkan indeks ', index)
